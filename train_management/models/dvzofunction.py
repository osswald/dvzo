from django.db import models
from django.utils.translation import gettext_lazy as _


class DvzoFunction(models.Model):

    class Meta:
        verbose_name = _("Function")
        verbose_name_plural = _("Functions")

    class FunctionType(models.TextChoices):
        TRAIN = "train", _("Train")
        BAUMA = "bauma", _("Bauma")
        NEUTHAL = "neuthal", _("Neuthal")
        BAERETSWIL = "baeretswil", _("Bäretswil")
        HINWIL = "hinwil", _("Hinwil")

    label = models.CharField(_("label"), max_length=200)
    label_short = models.CharField(_("label short"), max_length=80)
    sorting = models.IntegerField(null=True, blank=True)
    function_type = models.CharField(_("function_type"),
                                     max_length=80, choices=FunctionType.choices)
