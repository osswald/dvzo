from django.db import models
from django.utils.translation import gettext_lazy as _

from train_management.models import AbstractDvzoModel, Station, Train


class TrainTimetable(AbstractDvzoModel):

    class Meta:
        verbose_name = _("train_timetable.singular")
        verbose_name_plural = _("train_timetable.plural")

    class ReservationPossible(models.TextChoices):
        NOT_POSSIBLE = "not_possible", _("train_timetable.reservation_possible.not_possible")
        POSSIBLE = "possible", _("train_timetable.reservation_possible.possible")

    label = models.CharField(_("train_timetable.label"), max_length=200)
    train = models.ForeignKey(Train, on_delete=models.DO_NOTHING, null=True)
    start_station = models.ForeignKey(Station, related_name="start_station", on_delete=models.DO_NOTHING, null=True)
    destination_station = models.ForeignKey(Station, related_name="destination_station",
                                            on_delete=models.DO_NOTHING, null=True)
    start_time = models.TimeField(_("train_timetable.start time"), null=True, blank=True)
    destination_time = models.TimeField(_("train_timetable.destination time"), null=True, blank=True)
    comment = models.TextField(_("train_timetable.description"), blank=True)
    reservation_internal = models.CharField(_("train_timetable.reservation_internal"), max_length=80,
                                            choices=ReservationPossible.choices,
                                            default=ReservationPossible.NOT_POSSIBLE)
    reservation_external = models.CharField(_("train_timetable.reservation_external"), max_length=80,
                                            choices=ReservationPossible.choices,
                                            default=ReservationPossible.NOT_POSSIBLE)
    frequency = models.IntegerField(_("train_timetable.frequency"), null=True, blank=True)

    def __str__(self):
        return self.label
