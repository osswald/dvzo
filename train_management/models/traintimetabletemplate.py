from django.db import models
from django.utils.translation import gettext_lazy as _

from train_management.models import Station, Train


class TrainTimetableTemplate(models.Model):

    class Meta:
        verbose_name = _("Train timetable template")
        verbose_name_plural = _("Train timetable templates")

    class Active(models.TextChoices):
        YES = "yes", _("Yes")
        NO = "no", _("No")

    template_name = models.CharField(_("template name"), max_length=200)
    label = models.CharField(_("label"), max_length=200)
    train = models.ForeignKey(Train, on_delete=models.DO_NOTHING, null=True)
    start_station = models.ForeignKey(
        Station, related_name="start_station_template", on_delete=models.DO_NOTHING, null=True)
    destination_station = models.ForeignKey(
        Station, related_name="destination_station_template", on_delete=models.DO_NOTHING, null=True)
    start_time = models.TimeField(_("start time"), null=True, blank=True)
    destination_time = models.TimeField(_("destination time"), null=True, blank=True)
    comment = models.TextField(_("description"), blank=True)
    active = models.CharField(_("active"), max_length=50, choices=Active.choices, default=Active.YES)
