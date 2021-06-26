from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from train_management.models import AbstractDvzoModel
from uniforms.models import Article


class StockMovement(AbstractDvzoModel):
    class Meta:
        verbose_name = _("stock_movement.singular")
        verbose_name_plural = _("stock_movement.plural")

    class StockMovementType(models.TextChoices):
        LET_OUT = "let_out", _("stock_movement.type.let_out")
        LET_IN = "let_in", _("stock_movement.type.let_in")
        RENT_OUT = "rent_out", _("stock_movement.type.rent_out")
        RENT_IN = "rent_in", _("stock_movement.type.rent_in")
        MANUAL_OUT = "manual_out", _("stock_movement.type.manual_out")
        MANUAL_IN = "manual_in", _("stock_movement.type.manual_in")

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    date = models.DateField(_("stock_movement.date"))
    amount = models.IntegerField(_("stock_movement.amount"))
    type = models.CharField(_("stock_movement.type"), max_length=80, choices=StockMovementType.choices)
    comment = models.CharField(_("stock_movement.comment"), max_length=200, blank=True, null=True)


@receiver(post_save, sender=StockMovement)
def sum_up_amount_on_save(sender, instance, created, *args, **kwargs):
    article = Article.objects.get(id=instance.article.id)
    stock_movements = StockMovement.objects.filter(article=article)
    amount = stock_movements.aggregate(Sum('amount'))
    article.amount = amount['amount__sum']
    article.save()


@receiver(post_delete, sender=StockMovement)
def sum_up_amount_on_delete(sender, instance, *args, **kwargs):
    article = Article.objects.get(id=instance.article.id)
    stock_movements = StockMovement.objects.filter(article=article)
    amount = stock_movements.aggregate(Sum('amount'))
    article.amount = amount['amount__sum']
    article.save()
