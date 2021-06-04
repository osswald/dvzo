from django.db import models
from django.utils.translation import gettext_lazy as _

from train_management.models import AbstractDvzoModel, Station, TrainTimetable


class Route(AbstractDvzoModel):

    class Meta:
        verbose_name = _("route.singular")
        verbose_name_plural = _("route.plural")
        
    class Reason(models.TextChoices):
        NO_STOP = "no_stop", _("route.reason.no_stop")
        NO_STOP_DIFF = "no_stop_diff", _("route.reason.no_stop_diff")
        START = "start", _("route.reason.start")
        END = "end", _("route.reason.end")
        STOP = "stop", _("route.reason.stop")
        
# TODO: form, view, template. in template and view limit station (starting with 2nd station) to neighbours of previous station
# in template and view handle adding of additional route-points

    traintimetable = models.ForeignKey(TrainTimetable, null=True, on_delete=models.DO_NOTHING)
    station = models.ForeignKey(Station, on_delete=models.DO_NOTHING)
    arrival = models.TimeField(_("route.arrival"), null=True, blank=True)
    departure = models.TimeField(_("route.departure"), null=True, blank=True)
    reason = models.CharField(_("route.reason"), max_length=80, choices=Reason.choices)
    ordering = models.IntegerField(_("route.ordering"))

    def __str__(self):
        return self.station.label
