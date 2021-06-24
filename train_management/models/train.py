from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from train_management.models import AbstractDvzoModel, DayPlanning, FunctionPersons, Station, Vehicle


class Train(AbstractDvzoModel):

    class Meta:
        verbose_name = _("train.singular")
        verbose_name_plural = _("train.plural")

    label = models.CharField(_("train.label"), max_length=200)
    km = models.IntegerField(_("train.km"), blank=True)
    day_planning = models.ForeignKey(DayPlanning, on_delete=models.CASCADE)
    function_persons = models.ManyToManyField(FunctionPersons, related_name="train")
    frequency = models.IntegerField(_("train.frequency"), null=True, blank=True)

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

    def add_traintimetable(self, timetables):

        for timetable in timetables:
            template = TrainTimetableTemplate.objects.get(pk=timetable.pk)
            TrainTimetable(train=self,
                           label=template.label,
                           start_station=template.start_station,
                           destination_station=template.destination_station,
                           start_time=template.start_time,
                           destination_time=template.destination_time,
                           reservation_internal=template.reservation_internal,
                           reservation_external=template.reservation_external,).save()


class TrainConfiguration(AbstractDvzoModel):

    class Meta:
        verbose_name = _("train_configuration.singular")
        verbose_name_plural = _("train_configuration.plural")

    vehicle = models.ForeignKey(Vehicle, null=True, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    sorting = models.IntegerField(_("train_configuration.sorting"), blank=True, null=True)


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


class TrainTimetableTemplate(AbstractDvzoModel):

    class Meta:
        verbose_name = _("train_timetable_template.singular")
        verbose_name_plural = _("train_timetable_template.plural")

    class Active(models.TextChoices):
        YES = "yes", _("train_timetable_template.active.yes")
        NO = "no", _("train_timetable_template.active.no")

    class ReservationPossible(models.TextChoices):
        NOT_POSSIBLE = "not_possible", _("train_timetable.reservation_possible.not_possible")
        POSSIBLE = "possible", _("train_timetable.reservation_possible.possible")

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
    active = models.CharField(_("train_timetable_template.active"), max_length=50, choices=Active.choices,
                              default=Active.YES)
    reservation_internal = models.CharField(_("train_timetable.reservation_internal"), max_length=80,
                                            choices=ReservationPossible.choices,
                                            default=ReservationPossible.NOT_POSSIBLE)
    reservation_external = models.CharField(_("train_timetable.reservation_external"), max_length=80,
                                            choices=ReservationPossible.choices,
                                            default=ReservationPossible.NOT_POSSIBLE)

    def __str__(self):
        return self.template_name


@receiver(post_save, sender=TrainTimetable)
def sum_up_frequencies_on_save(sender, instance, created, *args, **kwargs):
    train = Train.objects.get(id=instance.train.id)
    train_timetables = TrainTimetable.objects.filter(train=train)
    frequency = train_timetables.aggregate(Sum('frequency'))
    train.frequency = frequency['frequency__sum']
    train.save()


@receiver(post_delete, sender=TrainTimetable)
def sum_up_frequencies_on_delete(sender, instance, *args, **kwargs):
    train = Train.objects.get(id=instance.train.id)
    train_timetables = TrainTimetable.objects.filter(train=train)
    frequency = train_timetables.aggregate(Sum('frequency'))
    train.frequency = frequency['frequency__sum']
    train.save()
