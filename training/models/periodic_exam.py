from django.db import models
from django.utils.translation import gettext_lazy as _

from train_management.models import AbstractDvzoModel, Personnel
from training.models import Qualification


class PeriodicExam(AbstractDvzoModel):
    class Meta:
        verbose_name = _("periodic_exam.singular")
        verbose_name_plural = _("periodic_exam.plural")

    personnel = models.ForeignKey(Personnel, on_delete=models.DO_NOTHING)
    qualification = models.ForeignKey(Qualification, on_delete=models.DO_NOTHING)
    date = models.DateField(_("periodic_exam.date"), null=True, blank=True)

    def __str__(self):
        return self.label
