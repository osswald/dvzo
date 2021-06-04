from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from train_management.models import AbstractDvzoModel


class PhoneNumber(AbstractDvzoModel):

    class Meta:
        verbose_name = _("phone_number.singular")
        verbose_name_plural = _("phone_number.plural")

    class PhoneNumberType(models.TextChoices):
        SBB = "sbb", _("phone_number.type.sbb")
        EMERGENCY = "emergency", _("phone_number.type.emergency")
        DVZO = "dvzo", _("phone_number.type.dvzo")
        OTHER = "other", _("phone_number.type.other")

    label = models.CharField(_("phone_number.label"), max_length=200)
    phone_number = PhoneNumberField(_("phone_number.phone_number"))
    phone_number_type = models.CharField(_("phone_number.type"), max_length=80, choices=PhoneNumberType.choices)

    def __str__(self):
        return self.label
