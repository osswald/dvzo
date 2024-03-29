from django.db import models
from django.db.models.signals import post_delete
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from train_management.models import AbstractDvzoModel
from train_management.models import DayPlanning
from train_management.models import TrainConfiguration
from train_management.models import Vehicle


class Availability(AbstractDvzoModel):
    class Meta:
        verbose_name = _("availability.singular")
        verbose_name_plural = _("availability.plural")

    class AvailabilityStatus(models.TextChoices):
        IN_USE = "in_use", _("availability.availability_status.in_use")
        ASK = "ask", _("availability.availability_status.ask")
        SERVICE = "servicing", _("availability.availability_status.servicing")
        LOCKED = "locked", _("availability.availability_status.locked")

    vehicle = models.ForeignKey(Vehicle, on_delete=models.DO_NOTHING)
    dayplanning = models.ForeignKey(DayPlanning, on_delete=models.DO_NOTHING, null=True)
    start = models.DateField(_("availability.start"))
    end = models.DateField(_("availability.end"))
    availability_status = models.CharField(
        _("availability.status"), max_length=80, choices=AvailabilityStatus.choices, default=AvailabilityStatus.SERVICE
    )

    def __str__(self):
        return self.vehicle.label


@receiver(post_delete, sender=TrainConfiguration)
def train_configuration_post_delete(sender, instance, *args, **kwargs):
    day_planning = DayPlanning.objects.get(id=instance.train.day_planning.id)
    vehicle = Vehicle.objects.get(id=instance.vehicle.id)
    Availability.objects.filter(vehicle=vehicle, dayplanning=day_planning).delete()


@receiver(post_save, sender=TrainConfiguration)
def train_configuration_post_create(sender, instance, created, *args, **kwargs):
    day_planning = DayPlanning.objects.get(id=instance.train.day_planning.id)
    vehicle = Vehicle.objects.get(id=instance.vehicle.id)
    availability_status = Availability.AvailabilityStatus.IN_USE
    date = day_planning.date
    if created:
        Availability(
            vehicle=vehicle, dayplanning=day_planning, start=date, end=date, availability_status=availability_status
        ).save()
