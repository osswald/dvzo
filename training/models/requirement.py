from django.db import models
from django.utils.translation import gettext_lazy as _

from train_management.models import AbstractDvzoModel
from training.models import MedicalFitnessLevel, PeriodicExam, Qualification, TrainingModule


class Requirement(AbstractDvzoModel):
    class Meta:
        verbose_name = _("requirement.singular")
        verbose_name_plural = _("requirement.plural")

    qualification = models.ForeignKey(Qualification, on_delete=models.DO_NOTHING)
    module = models.ManyToManyField(TrainingModule, blank=True)
    medical_fitness = models.ForeignKey(MedicalFitnessLevel, null=True, blank=True, on_delete=models.DO_NOTHING)
    periodic_exam = models.ForeignKey(PeriodicExam, null=True, blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.qualification
