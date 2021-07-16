from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from train_management.models import AbstractDvzoModel
from train_management.models import Station
from train_management.models import TrainTimetable


class Reservation(AbstractDvzoModel):
    class Meta:
        verbose_name = _("reservation.singular")
        verbose_name_plural = _("reservation.plural")

    class ReservationType(models.TextChoices):
        GASTRO = "gastro", _("reservation.type.gastro")
        SEATING = "seating", _("reservation.type.seating")

    class ReservationStatus(models.TextChoices):
        PROPOSAL = "proposal", _("reservation.status.proposal")
        CONFIRMED = "confirmed", _("reservation.status.confirmed")

    label = models.CharField(_("reservation.label"), max_length=200)
    train_timetable = models.ForeignKey(TrainTimetable, on_delete=models.CASCADE)
    phone = PhoneNumberField(_("reservation.phone"), blank=True)
    email = models.EmailField(_("reservation.email"), blank=True)
    amount = models.IntegerField(_("reservation.amount"))
    reservation_type = models.CharField(_("reservation.type"), choices=ReservationType.choices, max_length=80)
    reservation_status = models.CharField(
        _("reservation.status"), choices=ReservationStatus.choices, max_length=80, default=ReservationStatus.CONFIRMED
    )
    comment = models.TextField(_("reservation.comment"), blank=True, null=True)
    start = models.ForeignKey(
        Station, related_name="start_reservation", null=True, blank=True, on_delete=models.DO_NOTHING
    )
    end = models.ForeignKey(Station, related_name="end_reservation", null=True, blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.label
