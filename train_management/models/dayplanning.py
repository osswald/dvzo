from django.db import models
from django.utils.translation import gettext_lazy as _

from train_management.models import FunctionPersons


class DayPlanning(models.Model):

    class Meta:
        verbose_name = _("dayplanning.singular")
        verbose_name_plural = _("dayplanning.plural")

    class DayPlanningStatus(models.TextChoices):
        DRAFT = "draft", _("dayplanning.status.draft")
        CONFIRMED = "confirmed", _("dayplanning.status.confirmed")
        EXECUTED = "executed", _("dayplanning.status.executed")

    class DayPlanningType(models.TextChoices):
        SUNDAY = "sunday", _("dayplanning.type.sunday")
        EXTRA = "extra", _("dayplanning.type.extra")
        OTHER = "other", _("dayplanning.type.other")

    class DayPlanningPaid(models.TextChoices):
        YES = "yes", _("dayplanning.paid.yes")
        NO = "no", _("dayplanning.paid.no")
        NOT_APPLICABLE = "not_applicable", _("dayplanning.paid.not_applicable")

    class DayPlanningSlot(models.TextChoices):
        OPEN = "open", _("dayplanning.slot.open")
        ORDERED = "ordered", _("dayplanning.slot.ordered")
        RECEIVED = "received", _("dayplanning.slot.received")
        NOT_APPLICABLE = "not_applicable", _("dayplanning.slot.received")

    class DayPlanningPersonnelDisposition(models.TextChoices):
        OPEN = "open", _("dayplanning.personnel_disposition.open")
        DISPOSED = "disposed", _("dayplanning.personnel_disposition.disposed")
        NOT_APPLICABLE = "not_applicable", _("dayplanning.personnel_disposition.not_applicable")

    class DayPlanningBookingStatus(models.TextChoices):
        PROPOSAL = "proposal", _("dayplanning.booking_status.proposal")
        RESERVATION = "reservation", _("dayplanning.booking_status.reservation")
        BOOKED = "booked", _("dayplanning.booking_status.booked")
        CANCELLED_DVZO = "cancelled_dvzo", _("dayplanning.booking_status.cancelled_dvzo")
        CANCELLED_CUSTOMER = "cancelled_customer", _("dayplanning.booking_status.cancelled_customer")
        NOT_APPLICABLE = "not_applicable", _("dayplanning.booking_status.not_applicable")

    label = models.CharField(_("dayplanning.label"), max_length=200)
    day_planning_type = models.CharField(_("dayplanning.day_planning_type"), max_length=80,
                                         choices=DayPlanningType.choices)
    date = models.DateField(_("dayplanning.date"))
    status = models.CharField(_("dayplanning.status"), max_length=80, choices=DayPlanningStatus.choices)
    paid = models.TextField(_("dayplanning.paid"), max_length=80, choices=DayPlanningPaid.choices,
                            default=DayPlanningPaid.NOT_APPLICABLE)
    text = models.TextField(_("dayplanning.text"), max_length=5000, blank=True)
    function_persons = models.ManyToManyField(FunctionPersons, related_name="dayplanning")
    slot_ordered = models.CharField(_("slot ordered"), max_length=80, choices=DayPlanningSlot.choices,
                                    default=DayPlanningSlot.NOT_APPLICABLE)
    personnel_disposition = models.CharField(_("dayplanning.personnel_disposition"), max_length=80,
                                             choices=DayPlanningPersonnelDisposition.choices,
                                             default=DayPlanningPersonnelDisposition.OPEN)
    customers = models.IntegerField(_("dayplanning.customers"), blank=True, null=True)
    price = models.DecimalField(_("dayplanning.price"), blank=True, max_digits=8, decimal_places=2, null=True)
    booking_status = models.CharField(_("dayplanning.booking_status"), max_length=80,
                                      choices=DayPlanningBookingStatus.choices,
                                      default=DayPlanningBookingStatus.NOT_APPLICABLE)
    comment = models.TextField(_("dayplanning.comment"), blank=True)

    def __str__(self):
        return self.label


class DayPlanningText(models.Model):

    class Meta:
        verbose_name = _("dayplanning_text.singular")
        verbose_name_plural = _("dayplanning_text.plural")

    label = models.CharField(_("dayplanning_text.label"), max_length=200)
    text = models.TextField(_("dayplanning_text.text"))
    sorting = models.IntegerField(_("dayplanning_text.sorting"), blank=True, null=True)
    dayplanning = models.ForeignKey(DayPlanning, on_delete=models.CASCADE)

    def __str__(self):
        return self.label
