from django.db import models
from django.utils.translation import gettext_lazy as _

from train_management.models import AbstractDvzoModel


class TrainingModule(AbstractDvzoModel):
    class Meta:
        verbose_name = _("module.singular")
        verbose_name_plural = _("module.plural")

    label = models.CharField(_("module.label"), max_length=200)
    label_short = models.CharField(_("module.label_short"), max_length=5)
    description = models.TextField(_("module.description"), blank=True)

    def __str__(self):
        return self.label
