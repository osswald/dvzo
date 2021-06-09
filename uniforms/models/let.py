from django.db import models
from django.utils.translation import gettext_lazy as _

from train_management.models import AbstractDvzoModel, Personnel
from uniforms.models import Article


class Let(models.Model):
    class Meta:
        verbose_name = _("let.singular")
        verbose_name_plural = _("let.plural")

    class LetReturned(models.TextChoices):
        YES = "yes", _("let.returned.yes")
        NO = "no", _("let.returned.no")

    personnel = models.ForeignKey(Personnel, on_delete=models.DO_NOTHING)
    start = models.DateField(_("let.start"))
    end = models.DateField(_("let.end"))
    returned = models.CharField(_("let.returned"), max_length=80, choices=LetReturned.choices, default=LetReturned.NO)


class ArticleLet(AbstractDvzoModel):
    class Meta:
        verbose_name = _("article_let.singular")
        verbose_name_plural = _("article_let.plural")

    let = models.ForeignKey(Let, on_delete=models.DO_NOTHING)
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    amount = models.IntegerField(_("article_let.amount"))
