from dateutil import relativedelta

from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from train_management.models import AbstractDvzoModel
from uniforms.models import Article, Renter


class Rent(AbstractDvzoModel):
    class Meta:
        verbose_name = _("rent.singular")
        verbose_name_plural = _("rent.plural")

    class RentReturned(models.TextChoices):
        YES = "yes", _("rent.returned.yes")
        NO = "no", _("rent.returned.no")

    renter = models.ForeignKey(Renter, on_delete=models.DO_NOTHING)
    start = models.DateField(_("rent.start"))
    end = models.DateField(_("rent.end"))
    duration = models.IntegerField(_("rent.duration"), blank=True, null=True)
    returned = models.CharField(_("rent.returned"), max_length=80, choices=RentReturned.choices,
                                default=RentReturned.NO)
    billed = models.BooleanField(_("rent.billed"))
    total_per_month = models.DecimalField(_("rent.total_per_month"), max_digits=8, decimal_places=2, null=True)
    total = models.DecimalField(_("rent.total"), max_digits=8, decimal_places=2, null=True)

    def save(self, *args, **kwargs):
        if self.end is not None:
            start = self.start
            end = self.end
            total_per_month = self.total_per_month
            duration = relativedelta.relativedelta(end, start).months
            if duration == 0:
                duration = 1
            self.duration = duration
            self.total = duration * total_per_month
            super(Rent, self).save(*args, **kwargs)


class ArticleRent(AbstractDvzoModel):
    class Meta:
        verbose_name = _("article_rent.singular")
        verbose_name_plural = _("article_rent.plural")

    rent = models.ForeignKey(Rent, on_delete=models.DO_NOTHING)
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(_("article_rent.amount"), max_digits=2, decimal_places=0)
    total_per_month = models.DecimalField(_("article_rent.total_per_month"), max_digits=8, decimal_places=2, null=True,
                                          editable=False)

    def get_total_per_month(self):
        result = self.amount * self.article.price
        return result

    def save(self, *args, **kwargs):
        self.total_per_month = self.get_total_per_month()
        super(ArticleRent, self).save(*args, **kwargs)


@receiver(post_save, sender=ArticleRent)
def do_sums_on_rent_save(sender, instance, created, *args, **kwargs):
    rent = Rent.objects.get(id=instance.rent.id)
    article_rents = ArticleRent.objects.filter(rent=rent)
    total_per_month = article_rents.aggregate(Sum('total_per_month'))
    rent.total_per_month = total_per_month['total_per_month__sum']
    rent.save()


@receiver(post_delete, sender=ArticleRent)
def do_sums_on_rent_delete(sender, instance, *args, **kwargs):
    rent = Rent.objects.get(id=instance.rent.id)
    article_rents = ArticleRent.objects.filter(rent=rent)
    total_per_month = article_rents.aggregate(Sum('total_per_month'))
    rent.total_per_month = total_per_month['total_per_month__sum']
    rent.save()
