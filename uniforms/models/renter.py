from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from train_management.models import AbstractDvzoModel


class Renter(AbstractDvzoModel):
    class Meta:
        verbose_name = _("renter.singular")
        verbose_name_plural = _("renter.plural")

    name = models.CharField(_("renter.name"), max_length=200)
    street = models.CharField(_("renter.street"), max_length=200)
    zip = models.CharField(_("renter.zip"), max_length=200)
    city = models.CharField(_("renter.city"), max_length=200)
    phone = PhoneNumberField(_("renter.phone"))
    email = models.CharField(_("renter.email"), max_length=200)

    def __str__(self):
        return self.name
