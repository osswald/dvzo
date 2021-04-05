from django.db import models
from django.utils.translation import gettext_lazy as _

from train_management.models import FunctionPersons


class DayPlanning(models.Model):

    class Meta:
        verbose_name = _("Day planning")
        verbose_name_plural = _("Day plannings")

    class DayPlanningStatus(models.TextChoices):
        DRAFT = "draft", _("Draft")
        CONFIRMED = "confirmed", _("Confirmed")
        EXECUTED = "executed", _("Executed")

    class DayPlanningType(models.TextChoices):
        SUNDAY = "sunday", _("Sunday")
        EXTRA = "extra", _("Extra")
        OTHER = "other", _("Other")

    class DayPlanningPaid(models.TextChoices):
        YES = "yes", _("Yes")
        NO = "no", _("No")
        NOT_APPLICABLE = "not_applicable", _("Not applicable")

    class DayPlanningSlot(models.TextChoices):
        OPEN = "open", _("Open")
        ORDERED = "ordered", _("Ordered")
        RECEIVED = "received", _("Received")
        NOT_APPLICABLE = "not_applicable", _("Not applicable")

    class DayPlanningPersonnelDisposition(models.TextChoices):
        OPEN = "open", _("Open")
        DISPOSED = "disposed", _("Disposed")
        NOT_APPLICABLE = "not_applicable", _("Not applicable")

    class DayPlanningBookingStatus(models.TextChoices):
        PROPOSAL = "proposal", _("Proposal")
        RESERVATION = "reservation", _("Reservation")
        BOOKED = "booked", _("Booked")
        CANCELLED_DVZO = "cancelled_dvzo", _("Cancelled DVZO")
        CANCELLED_CUSTOMER = "cancelled_customer", _("Cancelled customer")
        NOT_APPLICABLE = "not_applicable", _("Not applicable")

    label = models.CharField(_("label"), max_length=200)
    day_planning_type = models.CharField(_("day_planning_type"), max_length=80, choices=DayPlanningType.choices)
    date = models.DateField(_("date"))
    status = models.CharField(_("status"), max_length=80, choices=DayPlanningStatus.choices)
    paid = models.TextField(_("paid"), max_length=80, choices=DayPlanningPaid.choices,
                            default=DayPlanningPaid.NOT_APPLICABLE)
    text = models.TextField(_("Text"), max_length=5000, blank=True)
    function_persons = models.ManyToManyField(FunctionPersons, related_name="dayplanning")
    slot_ordered = models.CharField(_("slot ordered"), max_length=80, choices=DayPlanningSlot.choices,
                                    default=DayPlanningSlot.NOT_APPLICABLE)
    personnel_disposition = models.CharField(_("Personnel disposition"), max_length=80,
                                             choices=DayPlanningPersonnelDisposition.choices,
                                             default=DayPlanningPersonnelDisposition.OPEN)
    customers = models.IntegerField(_("Number of customers"), blank=True, null=True)
    price = models.DecimalField(_("Price"), blank=True, max_digits=8, decimal_places=2, null=True)
    booking_status = models.CharField(_("Booking status"), max_length=80, choices=DayPlanningBookingStatus.choices,
                                      default=DayPlanningBookingStatus.NOT_APPLICABLE)
    comment = models.TextField(_("Comment"), blank=True)

    def __str__(self):
        return self.label
