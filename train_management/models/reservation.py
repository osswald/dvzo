from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from train_management.models import TrainTimetable


class Reservation(models.Model):
    class Meta:
        verbose_name = _("Reservation")
        verbose_name_plural = _("Reservations")

    class ReservationType(models.TextChoices):
        GASTRO = "gastro", _("Gastro")
        SEATING = "seating", _("Seating")

    class ReservationStatus(models.TextChoices):
        PROPOSAL = "proposal", _("Proposal")
        CONFIRMED = "confirmed", _("Confirmed")

    label = models.CharField(_("label"), max_length=200)
    train_timetable = models.ForeignKey(TrainTimetable, on_delete=models.DO_NOTHING)
    phone = PhoneNumberField(_("phone"), blank=True)
    email = models.EmailField(_("email"), blank=True)
    amount = models.IntegerField(_("number of people"))
    reservation_type = models.CharField(_("reservation type"), choices=ReservationType.choices, max_length=80)
    reservation_status = models.CharField(_("reservation status"), choices=ReservationStatus.choices, max_length=80,
                                          default=ReservationStatus.CONFIRMED)

    def __str__(self):
        return self.label
