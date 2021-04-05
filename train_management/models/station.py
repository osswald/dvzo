from django.db import models
from django.utils.translation import gettext_lazy as _


class Station(models.Model):
    class Meta:
        verbose_name = _("Betriebspunkt")
        verbose_name_plural = _("Betriebspunkte")

    didok_nr = models.CharField(_("DIDOK Nr."), blank=True, max_length=200)
    label_short = models.CharField(_("label short"), max_length=5)
    label = models.CharField(_("label"), max_length=200)

    def __str__(self):
        return self.label
