from django.db import models
from django.utils.translation import gettext_lazy as _

from train_management.models import AbstractDvzoModel
from train_management.models import Train


class Mileage(AbstractDvzoModel):
    class Meta:
        verbose_name = _("mileage.singular")
        verbose_name_plural = _("mileage.plural")

    date = models.DateField(_("mileage.date"))
    label = models.CharField(_("mileage.label"), max_length=200, blank=True)
    train = models.ForeignKey(Train, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.label
