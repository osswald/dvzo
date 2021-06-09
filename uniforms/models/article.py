from django.db import models
from django.utils.translation import gettext_lazy as _

from train_management.models import AbstractDvzoModel


class Article(AbstractDvzoModel):
    class Meta:
        verbose_name = _("article.singular")
        verbose_name_plural = _("article.plural")

    class ArticleCategory(models.TextChoices):
        COAT = "coat", _("article.article_category.coat")
        HAT = "hat", _("article.article_category.hat")
        MISC = "misc", _("article.article_category.misc")
        SHIRT = "shirt", _("article.article_category.shirt")
        SHOES = "shoes", _("article.article_category.shoes")
        VEST = "vest", _("article.article_category.vest")
        TIE = "tie", _("article.article_category.tie")
        TROUSERS = "trousers", _("article.article_category.trousers")

    class ArticleStatus(models.TextChoices):
        ACTIVE = "active", _("article.article_status.active")
        INACTIVE = "inactive", _("article.article_status.inactive")

    label = models.CharField(_("article.label"), max_length=200)
    category = models.CharField(_("article.category"), max_length=80, choices=ArticleCategory.choices)
    status = models.CharField(_("article.status"), max_length=80, choices=ArticleStatus.choices,
                              default=ArticleStatus.ACTIVE)
    amount = models.IntegerField(_("article.amount"), null=True, blank=True)
    price = models.DecimalField(_("article.price"), max_digits=5, decimal_places=2)

    def __str__(self):
        return self.label


class HatArticle(Article):
    class Meta:
        verbose_name = _("article.hat.singular")
        verbose_name_plural = _("article.hat.plural")

    circumference = models.IntegerField(_("article.hat.circumference"), null=True, blank=True)


class ShirtArticle(Article):
    class Meta:
        verbose_name = _("article.shirt.singular")
        verbose_name_plural = _("article.shirt.plural")

    size = models.IntegerField(_("article.shirt.size"), null=True, blank=True)


class VestArticle(Article):
    class Meta:
        verbose_name = _("article.vest.singular")
        verbose_name_plural = _("article.vest.plural")

    size = models.IntegerField(_("article.vest.size"), null=True, blank=True)


class CoatArticle(Article):
    class Meta:
        verbose_name = _("article.coat.singular")
        verbose_name_plural = _("article.coat.plural")

    size = models.IntegerField(_("article.coat.size"), null=True, blank=True)


class TieArticle(Article):
    class Meta:
        verbose_name = _("article.tie.singular")
        verbose_name_plural = _("article.tie.plural")

    length = models.IntegerField(_("article.tie.length"), null=True, blank=True)


class TrousersArticle(Article):
    class Meta:
        verbose_name = _("article.trousers.singular")
        verbose_name_plural = _("article.trousers.plural")

    waist = models.IntegerField(_("article.trousers.waist"), null=True, blank=True)
    length = models.IntegerField(_("article.trousers.length"), null=True, blank=True)


class ShoesArticle(Article):
    class Meta:
        verbose_name = _("article.shoes.singular")
        verbose_name_plural = _("article.shoes.plural")

    size = models.IntegerField(_("article.shoes.size"), null=True, blank=True)


class MiscArticle(Article):
    class Meta:
        verbose_name = _("article.misc.singular")
        verbose_name_plural = _("article.misc.plural")

    class MiscArticleType(models.TextChoices):
        WHISTLE = "whistle", _("article.misc_article_type.whistle")

    type = models.CharField(_("article.misc.type"), max_length=80, choices=MiscArticleType.choices)
