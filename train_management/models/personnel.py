from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from train_management.models import AbstractDvzoModel, PersonnelCategory


class Personnel(AbstractDvzoModel):

    class Meta:
        verbose_name = _("personnel.singular")
        verbose_name_plural = _("personnel.plural")

    class PersonnelStatus(models.TextChoices):
        ACTIVE = "active", _("personnel.personnel_status.active")
        INACTIVE = "inactive", _("personnel.personnel_status.inactive")

    class PersonnelMobilePublic(models.TextChoices):
        YES = "yes", _("personnel.personnel_mobile_public.yes")
        NO = "no", _("personnel.personnel_mobile_public.no")
        UNKNOWN = "unknown", _("personnel.personnel_mobile_public.unknown")

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    mobile_phone = PhoneNumberField(_("personnel.mobile_phone"), blank=True)
    status = models.CharField(_("personnel.status"),
                              max_length=80, choices=PersonnelStatus.choices)
    mobile_phone_public = models.CharField(_("personnel.personnel_mobile_public"), max_length=80,
                                           choices=PersonnelMobilePublic.choices, default=PersonnelMobilePublic.UNKNOWN)
    category = models.ManyToManyField(PersonnelCategory, blank=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    @property
    def username(self):
        return self.user.username

    @property
    def last_name(self):
        return self.user.last_name

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def email(self):
        return self.user.email
