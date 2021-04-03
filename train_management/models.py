from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Vehicle(models.Model):

    class Meta:
        verbose_name = _("Vehicle")
        verbose_name_plural = _("Vehicles")

    class VehicleType(models.TextChoices):
        ENGINE = "engine", _("Engine")
        CARRIAGE = "carriage", _("Carriage")

    class Status(models.TextChoices):
        AVAILABLE = "available", _("Available")
        SERVICE = "servicing", _("In Servicing")
        ASK = "ask", _("Ask")

    class CarriageType(models.TextChoices):
        SEAT = "seat", _("Seating Car")
        GASTRO = "gastro", _("Waggon Restaurant")
        LUGGAGE = "luggage", _("Luggage")
        CARGO = "cargo", _("Cargo")

    class Home(models.TextChoices):
        BAUMA = "bauma", _("Bauma")
        USTER = "uster", _("Uster")
        WALD = "wald", _("Wald ZH")

    class PowerUnit(models.TextChoices):
        STEAM = "steam", _("Steam")
        DIESEL = "diesel", _("Diesel")
        ELECTRIC = "electric", _("Electric")
        DIESEL_ELECTRIC = "dieselelectric", _("Diesel/Electric")

    class SteamHeating(models.TextChoices):
        NO = "no", _("No")
        FRONT = "front", _("Front")
        BACK = "back", _("Back")
        FRONT_BACK = "both", _("Front and Back")

    label = models.CharField(_("label"), max_length=200)
    historic_name = models.CharField(_("historic_name"), max_length=200, blank=True)
    description = models.TextField(_("description"), blank=True)
    uic = models.CharField(_("UIC"), max_length=200, blank=True)
    image = models.ImageField(_("image"), blank=True, null=True)
    gross_weight = models.FloatField(_("gross_weight"), blank=True, null=True)
    seats = models.IntegerField(_("seats"), blank=True, null=True)
    vehicle_type = models.CharField(_("vehicle type"),
                            max_length=80, choices=VehicleType.choices)
    status = models.CharField(_("status"),
                            max_length=80, choices=Status.choices)
    carriage_type = models.CharField(_("carriage_type"),
                            max_length=80, choices=CarriageType.choices)
    home = models.CharField(_("home"),
                            max_length=80, choices=Home.choices)
    start_year = models.IntegerField(_("start year"), blank=True, null=True)
    last_revision = models.DateField(_("last revision"), blank=True, null=True)
    next_revision = models.DateField(_("next revision"), blank=True, null=True)
    axles_distance = models.FloatField(_("axles distance"), blank=True, null=True)
    length = models.FloatField(_("length"), blank=True, null=True)
    manufacturer = models.CharField(_("manufacturer"), max_length=200, blank=True)
    traction_25 = models.IntegerField(_("traction 25 permille"), blank=True, null=True)
    traction_30 = models.IntegerField(_("traction 30 permille"), blank=True, null=True)
    power_unit = models.CharField(_("power_unit"),
                                  max_length=80, choices=PowerUnit.choices)
    steam_heating = models.CharField(_("steam_heating"),
                                max_length=80, choices=SteamHeating.choices)
    max_speed = models.IntegerField(_("maximum speed"), blank=True, null=True)

    def __str__(self):
        return self.label


class Personnel(models.Model):

    class Meta:
        verbose_name = _("Personnel")
        verbose_name_plural = _("Personnel")

    class PersonnelStatus(models.TextChoices):
        ACTIVE = "active", _("Active")
        INACTIVE = "inactive", _("Inactive")

    class PersonnelMobilePublic(models.TextChoices):
        YES = "yes", _("Yes")
        NO = "no", _("No")
        UNKNOWN = "unknown", _("Unknown")

    firstname = models.CharField(_("firstname"), max_length=200)
    lastname = models.CharField(_("lastname"), max_length=200)
    email = models.CharField(_("email"), max_length=200)
    mobile_phone = models.CharField(_("mobile phone"), max_length=200)
    status = models.CharField(_("status"),
                              max_length=80, choices=PersonnelStatus.choices)
    mobile_phone_public = models.CharField(_("mobile phone publicly available"), max_length=80,
                                           choices=PersonnelMobilePublic.choices, default=PersonnelMobilePublic.UNKNOWN)
    date_of_birth = models.DateField(_("date of birth"))

    def __str__(self):
        return "%s %s" % (self.firstname, self.lastname)


class DvzoFunction(models.Model):

    class Meta:
        verbose_name = _("Function")
        verbose_name_plural = _("Functions")

    class FunctionType(models.TextChoices):
        TRAIN = "train", _("Train")
        BAUMA = "bauma", _("Bauma")
        NEUTHAL = "neuthal", _("Neuthal")
        BAERETSWIL = "baeretswil", _("Bäretswil")
        HINWIL = "hinwil", _("Hinwil")

    label = models.CharField(_("label"), max_length=200)
    label_short = models.CharField(_("label short"), max_length=80)
    sorting = models.IntegerField(null=True, blank=True)
    function_type = models.CharField(_("function_type"),
                                     max_length=80, choices=FunctionType.choices)


class FunctionPersons(models.Model):
    dvzo_function = models.ForeignKey(DvzoFunction, on_delete=models.DO_NOTHING)
    person = models.ForeignKey(Personnel, on_delete=models.DO_NOTHING)


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


class Train(models.Model):

    class Meta:
        verbose_name = _("Train tour")
        verbose_name_plural = _("Train tours")

    label = models.CharField(_("label"), max_length=200)
    km = models.IntegerField(_("km"), blank=True)
    day_planning = models.ForeignKey(DayPlanning, on_delete=models.CASCADE)
    function_persons = models.ManyToManyField(FunctionPersons, related_name="train")

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


class TrainConfiguration(models.Model):

    class Meta:
        verbose_name = _("Train configuration")
        verbose_name_plural = _("Train configurations")

    vehicle = models.ForeignKey(Vehicle, null=True, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    sorting = models.IntegerField(_("sorting"), blank=True, null=True)


class Mileage(models.Model):

    class Meta:
        verbose_name = _("Mileage")
        verbose_name_plural = _("Mileages")

    date = models.DateField(_("date"))
    label = models.CharField(_("label"), max_length=200, blank=True)
    train = models.ForeignKey(Train, on_delete=models.CASCADE, null=True)


class PhoneNumber(models.Model):

    class Meta:
        verbose_name = _("Phone number")
        verbose_name_plural = _("Phone numbers")

    class PhoneNumberType(models.TextChoices):
        SBB = "sbb", _("SBB")
        EMERGENCY = "emergency", _("Emergency")
        DVZO = "dvzo", _("DVZO")
        OTHER = "other", _("Other")

    label = models.CharField(_("label"), max_length=200)
    phone_number = PhoneNumberField(_("Phone number"))
    phone_number_type = models.CharField(_("Phone number type"), max_length=80, choices=PhoneNumberType.choices)


class Station(models.Model):
    class Meta:
        verbose_name = _("Betriebspunkt")
        verbose_name_plural = _("Betriebspunkte")

    didok_nr = models.CharField(_("DIDOK Nr."), blank=True, max_length=200)
    label_short = models.CharField(_("label short"), max_length=5)
    label = models.CharField(_("label"), max_length=200)

    def __str__(self):
        return self.label


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
    start_station = models.ForeignKey(Station, related_name="start_station_template", on_delete=models.DO_NOTHING, null=True)
    destination_station = models.ForeignKey(Station, related_name="destination_station_template", on_delete=models.DO_NOTHING, null=True)
    start_time = models.TimeField(_("start time"), null=True, blank=True)
    destination_time = models.TimeField(_("destination time"), null=True, blank=True)
    comment = models.TextField(_("description"), blank=True)
    active = models.CharField(_("active"), max_length=50, choices=Active.choices, default=Active.YES)
