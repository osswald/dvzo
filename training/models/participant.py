from django.db import models
from django.utils.translation import gettext_lazy as _

from train_management.models import AbstractDvzoModel, Personnel
from training.models import Training


class Participant(AbstractDvzoModel):
    class Meta:
        verbose_name = _("participant.singular")
        verbose_name_plural = _("participant.plural")

    training = models.ForeignKey(Training, on_delete=models.DO_NOTHING)
    personnel = models.ForeignKey(Personnel, on_delete=models.DO_NOTHING)
    attended = models.BooleanField(_("participant.attended"))
    passed = models.BooleanField(_("participant.passed"))

    def __str__(self):
        return "%s %s" % (self.personnel.first_name, self.personnel.last_name)
