from django.db import models
from django.utils.translation import gettext_lazy as _

from train_management.models import AbstractDvzoModel, Personnel
from training.models import TrainingModule


class MedicalFitnessLevel(AbstractDvzoModel):
    class Meta:
        verbose_name = _("medical_fitness_level.singular")
        verbose_name_plural = _("medical_fitness_level.plural")

    label = models.CharField(_("medical_fitness_level.label"), max_length=200)

    def __str__(self):
        return self.label


class MedicalFitness(AbstractDvzoModel):
    class Meta:
        verbose_name = _("medical_fitness.singular")
        verbose_name_plural = _("medical_fitness.plural")

    personnel = models.ForeignKey(Personnel, on_delete=models.DO_NOTHING)
    level = models.ForeignKey(MedicalFitnessLevel, on_delete=models.DO_NOTHING)
    date = models.DateField(_("medical_fitness.date"), null=True, blank=True)

    def __str__(self):
        return self.label
