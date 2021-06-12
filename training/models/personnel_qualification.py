from django.db import models
from django.utils.translation import gettext_lazy as _

from train_management.models import AbstractDvzoModel, Personnel
from training.models import Qualification


class PersonnelQualification(AbstractDvzoModel):
    class Meta:
        verbose_name = _("personnel_qualification.singular")
        verbose_name_plural = _("personnel_qualification.plural")

    personnel = models.ForeignKey(Personnel, on_delete=models.DO_NOTHING)
    qualification = models.ForeignKey(Qualification, on_delete=models.DO_NOTHING)
    valid_until = models.DateField(_("personnel_qualification.valid_until"))
    automatically_added = models.BooleanField(_("personnel_qualification.automatically_added"))

    def __str__(self):
        return self.qualification
