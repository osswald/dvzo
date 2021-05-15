from django.db import models
from django.utils.translation import gettext_lazy as _

from train_management.models import Station, Train


class TrainTimetableTemplate(models.Model):

    class Meta:
        verbose_name = _("train_timetable_template.singular")
        verbose_name_plural = _("train_timetable_template.plural")

    class Active(models.TextChoices):
        YES = "yes", _("train_timetable_template.active.yes")
        NO = "no", _("train_timetable_template.active.no")

    template_name = models.CharField(_("train_timetable_template.template_name"), max_length=200)
    label = models.CharField(_("train_timetable_template.label"), max_length=200)
    train = models.ForeignKey(Train, on_delete=models.DO_NOTHING, null=True)
    start_station = models.ForeignKey(
        Station, related_name="start_station_template", on_delete=models.DO_NOTHING, null=True)
    destination_station = models.ForeignKey(
        Station, related_name="destination_station_template", on_delete=models.DO_NOTHING, null=True)
    start_time = models.TimeField(_("train_timetable_template.start_time"), null=True, blank=True)
    destination_time = models.TimeField(_("train_timetable_template.destination_time"), null=True, blank=True)
    comment = models.TextField(_("train_timetable_template.description"), blank=True)
    active = models.CharField(_("train_timetable_template.active"), max_length=50, choices=Active.choices, default=Active.YES)

    def __str__(self):
        return self.template_name
