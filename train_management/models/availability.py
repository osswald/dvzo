from django.db import models
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from train_management.models import DayPlanning, TrainConfiguration
from train_management.models import Vehicle


class Availability(models.Model):
    class Meta:
        verbose_name = _("Availability")
        verbose_name_plural = _("Availabilities")

    class AvailabilityStatus(models.TextChoices):
        IN_USE = "in_use", _("availability.availability_status.in_use")
        ASK = "ask", _("availability.availability_status.ask")
        SERVICE = "servicing", _("availability.availability_status.servicing")
        LOCKED = "locked", _("availability.availability_status.locked")

    vehicle = models.ForeignKey(Vehicle, on_delete=models.DO_NOTHING)
    dayplanning = models.ForeignKey(DayPlanning, on_delete=models.DO_NOTHING, null=True)
    start = models.DateField(_("availability.start"))
    end = models.DateField(_("availability.end"))
    availability_status = models.CharField(_("Status"),
                                           max_length=80,
                                           choices=AvailabilityStatus.choices,
                                           default=AvailabilityStatus.SERVICE)

    def __str__(self):
        return self.vehicle


@receiver(post_delete, sender=TrainConfiguration)
def train_configuration_post_delete(sender, instance, *args, **kwargs):
    day_planning = DayPlanning.objects.get(id=instance.train.day_planning.id)
    vehicle = Vehicle.objects.get(id=instance.vehicle.id)
    print(instance.id, "has been created")
    Availability(vehicle=vehicle, dayplanning=day_planning).delete()


@receiver(post_save, sender=TrainConfiguration)
def train_configuration_post_delete(sender, instance, created, *args, **kwargs):
    day_planning = DayPlanning.objects.get(id=instance.train.day_planning.id)
    vehicle = Vehicle.objects.get(id=instance.vehicle.id)
    availability_status = Availability.AvailabilityStatus.IN_USE
    date = day_planning.date
    if created:
        print(instance.id, "has been created")
        Availability(vehicle=vehicle, dayplanning=day_planning,
                     start=date, end=date, availability_status=availability_status).save()
