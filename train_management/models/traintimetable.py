from django.db import models
from django.utils.translation import gettext_lazy as _
from train_management.models import Train, Station


class TrainTimetable(models.Model):

    class Meta:
        verbose_name = _("Train timetable")
        verbose_name_plural = _("Train timetables")

    label = models.CharField(_("label"), max_length=200)
    train = models.ForeignKey(Train, on_delete=models.DO_NOTHING, null=True)
    start_station = models.ForeignKey(Station, related_name="start_station", on_delete=models.DO_NOTHING, null=True)
    destination_station = models.ForeignKey(Station, related_name="destination_station", on_delete=models.DO_NOTHING, null=True)
    start_time = models.TimeField(_("start time"), null=True, blank=True)
    destination_time = models.TimeField(_("destination time"), null=True, blank=True)
    comment = models.TextField(_("description"), blank=True)

