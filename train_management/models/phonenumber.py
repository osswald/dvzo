from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class PhoneNumber(models.Model):

    class Meta:
        verbose_name = _("Phone number")
        verbose_name_plural = _("Phone numbers")

    class PhoneNumberType(models.TextChoices):
        SBB = "sbb", _("SBB")
        EMERGENCY = "emergency", _("Emergency")
        DVZO = "dvzo", _("DVZO")
        OTHER = "other", _("Other")

    label = models.CharField(_("label"), max_length=200)
    phone_number = PhoneNumberField(_("Phone number"))
    phone_number_type = models.CharField(_("Phone number type"), max_length=80, choices=PhoneNumberType.choices)

    def __str__(self):
        return self.label
