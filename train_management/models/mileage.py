from django.db import models
from django.utils.translation import gettext_lazy as _

from train_management.models import Train


class Mileage(models.Model):

    class Meta:
        verbose_name = _("Mileage")
        verbose_name_plural = _("Mileages")

    date = models.DateField(_("date"))
    label = models.CharField(_("label"), max_length=200, blank=True)
    train = models.ForeignKey(Train, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.label
