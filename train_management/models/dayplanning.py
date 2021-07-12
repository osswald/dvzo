from django.db import models
from django.utils.translation import gettext_lazy as _

from train_management.models import AbstractDvzoModel, FunctionPersons


class DayPlanning(AbstractDvzoModel):

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

    class DayPlanningBilled(models.TextChoices):
        YES = "yes", _("dayplanning.billed.yes")
        NO = "no", _("dayplanning.billed.no")
        NOT_APPLICABLE = "not_applicable", _("dayplanning.billed.not_applicable")

    class DayPlanningSlot(models.TextChoices):
        OPEN = "open", _("dayplanning.slot.open")
        ORDERED = "ordered", _("dayplanning.slot.ordered")
        RESERVED = "reserved", _("dayplanning.slot.reserved")
        RECEIVED = "received", _("dayplanning.slot.received")
        NOT_APPLICABLE = "not_applicable", _("dayplanning.slot.not_applicable")

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

    class DayPlanningEnginePlanningStatus(models.TextChoices):
        OPEN = "open", _("dayplanning.vehicle_planning_status.open")
        ASKED = "asked", _("dayplanning.vehicle_planning_status.asked")
        OK = "ok", _("dayplanning.vehicle_planning_status.ok")

    class DayPlanningCarriagePlanningStatus(models.TextChoices):
        OPEN = "open", _("dayplanning.vehicle_planning_status.open")
        ASKED = "asked", _("dayplanning.vehicle_planning_status.asked")
        OK = "ok", _("dayplanning.vehicle_planning_status.ok")

    class DayPlanningRailwayCompany(models.TextChoices):
        TR = "tr", _("dayplanning.railway_company.tr")
        SBB = "sbb", _("dayplanning.railway_company.sbb")
        OTHER = "other", _("dayplanning.railway_company.other")

    label = models.CharField(_("dayplanning.label"), max_length=200)
    day_planning_type = models.CharField(_("dayplanning.day_planning_type"), max_length=80,
                                         choices=DayPlanningType.choices)
    date = models.DateField(_("dayplanning.date"))
    status = models.CharField(_("dayplanning.status"), max_length=80, choices=DayPlanningStatus.choices)
    billed = models.TextField(_("dayplanning.billed"), max_length=80, choices=DayPlanningBilled.choices,
                              default=DayPlanningBilled.NOT_APPLICABLE)
    function_persons = models.ManyToManyField(FunctionPersons, related_name="dayplanning")
    slot_ordered_st = models.CharField(_("dayplanning.slot_ordered_st"), max_length=80, choices=DayPlanningSlot.choices,
                                       default=DayPlanningSlot.NOT_APPLICABLE)
    slot_ordered_sbb = models.CharField(_("dayplanning.slot_ordered_sbb"), max_length=80,
                                        choices=DayPlanningSlot.choices, default=DayPlanningSlot.NOT_APPLICABLE)
    personnel_disposition = models.CharField(_("dayplanning.personnel_disposition"), max_length=80,
                                             choices=DayPlanningPersonnelDisposition.choices,
                                             default=DayPlanningPersonnelDisposition.OPEN)
    customers = models.IntegerField(_("dayplanning.customers"), blank=True, null=True)
    price = models.DecimalField(_("dayplanning.price"), blank=True, max_digits=8, decimal_places=2, null=True)
    booking_status = models.CharField(_("dayplanning.booking_status"), max_length=80,
                                      choices=DayPlanningBookingStatus.choices,
                                      default=DayPlanningBookingStatus.NOT_APPLICABLE)
    comment = models.TextField(_("dayplanning.comment"), blank=True)
    post_mortem = models.TextField(_("dayplanning.post_mortem"), blank=True)
    engine_planning_status = models.CharField(_("dayplanning.engine_planning_status"), max_length=80,
                                              choices=DayPlanningEnginePlanningStatus.choices,
                                              default=DayPlanningEnginePlanningStatus.OPEN)
    carriage_planning_status = models.CharField(_("dayplanning.carriage_planning_status"), max_length=80,
                                                choices=DayPlanningCarriagePlanningStatus.choices,
                                                default=DayPlanningCarriagePlanningStatus.OPEN)
    railway_company = models.CharField(_("dayplanning.railway_company"), max_length=80,
                                       choices=DayPlanningRailwayCompany.choices, default=DayPlanningRailwayCompany.TR)

    def __str__(self):
        return self.label


class DayPlanningText(AbstractDvzoModel):

    class Meta:
        verbose_name = _("dayplanning_text.singular")
        verbose_name_plural = _("dayplanning_text.plural")

    label = models.CharField(_("dayplanning_text.label"), max_length=200)
    text = models.TextField(_("dayplanning_text.text"))
    sorting = models.IntegerField(_("dayplanning_text.sorting"), blank=True, null=True)
    dayplanning = models.ForeignKey(DayPlanning, on_delete=models.CASCADE)

    def __str__(self):
        return self.label
