from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Personnel(models.Model):

    class Meta:
        verbose_name = _("Personnel")
        verbose_name_plural = _("Personnel")

    class PersonnelStatus(models.TextChoices):
        ACTIVE = "active", _("Active")
        INACTIVE = "inactive", _("Inactive")

    class PersonnelMobilePublic(models.TextChoices):
        YES = "yes", _("Yes")
        NO = "no", _("No")
        UNKNOWN = "unknown", _("Unknown")

    firstname = models.CharField(_("firstname"), max_length=200)
    lastname = models.CharField(_("lastname"), max_length=200)
    email = models.CharField(_("email"), max_length=200)
    mobile_phone = PhoneNumberField(_("mobile phone"))
    status = models.CharField(_("status"),
                              max_length=80, choices=PersonnelStatus.choices)
    mobile_phone_public = models.CharField(_("mobile phone publicly available"), max_length=80,
                                           choices=PersonnelMobilePublic.choices, default=PersonnelMobilePublic.UNKNOWN)
    date_of_birth = models.DateField(_("date of birth"))

    def __str__(self):
        return "%s %s" % (self.firstname, self.lastname)
