from django.db import models
from django.utils.translation import gettext_lazy as _

from train_management.models import AbstractDvzoModel


class Qualification(AbstractDvzoModel):
    class Meta:
        verbose_name = _("qualification.singular")
        verbose_name_plural = _("qualification.plural")

    class QualificationType(models.TextChoices):
        VTE = "vte", _("qualification.type.vte")
        ZSTEBV = "zstebv", _("qualification.type.zstebv")
        DVZO = "dvzo", _("qualification.type.dvzo")

    label = models.CharField(_("qualification.label"), blank=True, max_length=200)
    description = models.TextField(_("qualification.description"))
    type = models.CharField(_("qualification.type"), max_length=80, choices=QualificationType.choices)
    valid_years = models.IntegerField(_("qualification.valid_years"))

    def __str__(self):
        return self.label
