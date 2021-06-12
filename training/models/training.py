from django.db import models
from django.utils.translation import gettext_lazy as _

from train_management.models import AbstractDvzoModel, Personnel
from training.models import TrainingModule


class Training(AbstractDvzoModel):
    class Meta:
        verbose_name = _("training.singular")
        verbose_name_plural = _("training.plural")

    label = models.CharField(_("training.label"), max_length=200)
    course_label = models.CharField(_("training.course_label"), max_length=200)
    module = models.ForeignKey(TrainingModule, on_delete=models.DO_NOTHING)
    responsible = models.ForeignKey(Personnel, null=True, blank=True, on_delete=models.DO_NOTHING)
    start_date = models.DateField(_("training.start_date"), null=True, blank=True)
    end_date = models.DateField(_("training.end_date"), null=True, blank=True)

    def __str__(self):
        return self.label


class TrainingDate(AbstractDvzoModel):
    class Meta:
        verbose_name = _("training_date.singular")
        verbose_name_plural = _("training_date.plural")

    label = models.CharField(_("training_date.label"), max_length=200, null=True, blank=True)
    responsible = models.ManyToManyField(Personnel, blank=True, related_name='training_date_responsible')
    start_datetime = models.DateTimeField(_("training_date.start_date"), null=True, blank=True)
    end_datetime = models.DateTimeField(_("training_date.end_date"), null=True, blank=True)
    training = models.ForeignKey(Training, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.label
