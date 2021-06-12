from django.db import models
from django.utils.translation import gettext_lazy as _

from train_management.models import AbstractDvzoModel
from training.models import Participant, TrainingDate


class Attendance(AbstractDvzoModel):
    class Meta:
        verbose_name = _("attendance.singular")
        verbose_name_plural = _("attendance.plural")

    training_date = models.ForeignKey(TrainingDate, on_delete=models.DO_NOTHING)
    participant = models.ForeignKey(Participant, on_delete=models.DO_NOTHING)
    attended = models.BooleanField(_("attendance.attended"))
