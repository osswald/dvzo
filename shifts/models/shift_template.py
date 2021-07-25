from django.db import models
from django.utils.translation import gettext_lazy as _

from train_management.models import AbstractDvzoModel, PersonnelCategory


class ShiftTemplate(AbstractDvzoModel):

    class Meta:
        verbose_name = _("shift_template.singular")
        verbose_name_plural = _("shift_template.plural")

    label = models.CharField(_("shift_template.label"), max_length=200)
    description = models.TextField(_("shift_template.description"), blank=True)
    active = models.BooleanField(_("shift_template.active"), default=True)
    category = models.ForeignKey(PersonnelCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.label
