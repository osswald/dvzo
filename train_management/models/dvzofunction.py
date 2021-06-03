from django.db import models
from django.utils.translation import gettext_lazy as _

from train_management.models import AbstractDvzoModel


class DvzoFunction(AbstractDvzoModel):

    class Meta:
        verbose_name = _("dvzo_function.singular")
        verbose_name_plural = _("dvzo_function.plural")

    class FunctionType(models.TextChoices):
        TRAIN = "train", _("dvzo_function.function_type.train")
        BAUMA = "bauma", _("dvzo_function.function_type.bauma")
        NEUTHAL = "neuthal", _("dvzo_function.function_type.neuthal")
        BAERETSWIL = "baeretswil", _("dvzo_function.function_type.baeretswil")
        HINWIL = "hinwil", _("dvzo_function.function_type.hinwil")

    label = models.CharField(_("dvzo_function.label"), max_length=200)
    label_short = models.CharField(_("dvzo_function.label_short"), max_length=80)
    sorting = models.IntegerField(_("dvzo_function.sorting"), null=True, blank=True)
    function_type = models.CharField(_("dvzo_function.function_type"), max_length=80, choices=FunctionType.choices)

    def __str__(self):
        return self.label
