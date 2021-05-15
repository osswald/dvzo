from django.db import models
from django.utils.translation import gettext_lazy as _

from train_management.models import DayPlanning, FunctionPersons, Vehicle


class Train(models.Model):

    class Meta:
        verbose_name = _("train.singular")
        verbose_name_plural = _("train.plural")

    label = models.CharField(_("train.label"), max_length=200)
    km = models.IntegerField(_("train.km"), blank=True)
    day_planning = models.ForeignKey(DayPlanning, on_delete=models.CASCADE)
    function_persons = models.ManyToManyField(FunctionPersons, related_name="train")

    def __str__(self):
        return self.label

    @property
    def vehicles(self):
        return Vehicle.objects.filter(
            trainconfiguration__train=self).order_by('trainconfiguration__sorting')

    def set_composition(self, vehicles):
        TrainConfiguration.objects.filter(train=self).delete()
        for sorting, vehicle in enumerate(vehicles):
            TrainConfiguration(train=self, vehicle=vehicle, sorting=sorting).save()


class TrainConfiguration(models.Model):

    class Meta:
        verbose_name = _("train_configuration.singular")
        verbose_name_plural = _("train_configuration.plural")

    vehicle = models.ForeignKey(Vehicle, null=True, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    sorting = models.IntegerField(_("train_configuration.sorting"), blank=True, null=True)
