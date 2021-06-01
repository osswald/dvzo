from django.db import models
from django.utils.translation import gettext_lazy as _

from train_management.models import AbstractDvzoModel


class Station(AbstractDvzoModel):
    class Meta:
        verbose_name = _("station.singular")
        verbose_name_plural = _("station.plural")

    didok_nr = models.CharField(_("station.didok_nr"), blank=True, max_length=200)
    label_short = models.CharField(_("station.label_short"), max_length=5)
    label = models.CharField(_("station.label"), max_length=200)
    neighbours = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.label
