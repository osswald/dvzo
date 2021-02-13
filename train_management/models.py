from django.db import models
from django.utils.translation import gettext_lazy as _


class FunctionType(models.Model):
    label = models.CharField(max_length=200)
    sorting = models.IntegerField()

    def __str__(self):
        return self.label


class Vehicle(models.Model):

    class Meta:
        verbose_name = _("Vehicle")
        verbose_name_plural = _("Vehicles")

    class VehicleType(models.TextChoices):
        ENGINE = "E", _("Engine")
        CARRIAGE = "C", _("Carriage")

    class CarriageStatus(models.TextChoices):
        AVAILABLE = "A", _("Available")
        SERVICE = "S", _("In Servicing")
        ASK = "B", _("Ask")

    class CarriageType(models.TextChoices):
        SEATS = "C", _("Seating Car")
        GASTRO = "W", _("Waggon Restaurant")
        CARGO = "H", _("Cargo")

    class CarriageHome(models.TextChoices):
        BAUMA = "B", _("Bauma")
        USTER = "U", _("Uster")
        WALD = "W", _("Wald ZH")

    class PowerUnit(models.TextChoices):
        STEAM = "S", _("Steam")
        DIESEL = "D", _("Diesel")
        ELECTRIC = "E", _("Electric")
        DIESEL_ELECTRIC = "F", _("Diesel/Electric")

    class SteamHeating(models.TextChoices):
        NO = "A", _("No")
        FRONT = "B", _("Front")
        BACK = "C", _("Back")
        FRONT_BACK = "D", _("Front and Back")

    label = models.CharField(_("label"), max_length=200)
    historic_name = models.CharField(_("historic_name"),max_length=200, blank=True)
    description = models.TextField(_("description"),blank=True)
    uic = models.CharField(_("UIC"),max_length=200, blank=True)
    image = models.ImageField(_("image"),blank=True, null=True)
    gross_weight = models.FloatField(_("gross_weight"),blank=True, null=True)
    seats = models.IntegerField(_("seats"),blank=True, null=True)
    vehicle_type = models.CharField(_("vehicle type"),
        max_length=1, choices=VehicleType.choices)
    status = models.CharField(_("status"),
                                  max_length=1, choices=CarriageStatus.choices)
    carriage_type = models.CharField(_("carriage_type"),
                                  max_length=1, choices=CarriageType.choices)
    home = models.CharField(_("home"),
                                  max_length=1, choices=CarriageHome.choices)
    start_year = models.IntegerField(_("start year"),blank=True, null=True)
    last_revision = models.DateField(_("last revision"),blank=True, null=True)
    next_revision = models.DateField(_("next revision"),blank=True, null=True)
    axles_distance = models.FloatField(_("axles distance"),blank=True, null=True)
    length = models.FloatField(_("length"),blank=True, null=True)
    manufacturer = models.CharField(_("manufacturer"),max_length=200, blank=True)
    traction_25 = models.IntegerField(_("traction 25 permille"),blank=True)
    traction_30 = models.IntegerField(_("traction 30 permille"),blank=True)
    power_unit = models.CharField(_("power_unit"),
                                  max_length=1, choices=PowerUnit.choices)
    steam_heating = models.CharField(_("steam_heating"),
                                  max_length=1, choices=SteamHeating.choices)
    max_speed = models.IntegerField(_("maximum speed"),blank=True)
    lup = models.CharField(_("length over bumper"),max_length=200, blank=True)

    def __str__(self):
        return self.label


class DayPlanning(models.Model):

    class DayPlanningStatus(models.TextChoices):
        DRAFT = "D", _("Draft")
        CONFIRMED = "C", _("Confirmed")
        EXECUTED = "E", _("Executed")

    class DayPlanningType(models.TextChoices):
        SUNDAY = "S", _("Sunday")
        EXTRA = "E", _("Extra")
        OTHER = "O", _("Other")

    label = models.CharField(_("label"),max_length=200)
    day_planning_type = models.CharField(_("day_planning_type"),
                                  max_length=1, choices=DayPlanningType.choices)
    date = models.DateField(_("date"))
    status = models.CharField(_("status"),
                                  max_length=1, choices=DayPlanningStatus.choices)
    paid = models.BooleanField(_("paid"))

    def __str__(self):
        return self.label


class Train(models.Model):
    label = models.CharField(_("label"), max_length=200)
    km = models.IntegerField(_("km"), blank=True)
    day_planning = models.ForeignKey(DayPlanning, on_delete=models.CASCADE)

    def __str__(self):
        return self.label


class TextBlock(models.Model):
    title = models.CharField(_("title"), max_length=200)
    content = models.IntegerField(_("content"), blank=True)
    day_planning = models.ForeignKey(DayPlanning, on_delete=models.CASCADE)
    sorting = models.IntegerField(_("sorting"), blank=True)

    def __str__(self):
        return self.title


class TrainConfiguration(models.Model):
    vehicle = models.ForeignKey(Vehicle, null=True, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    sorting = models.IntegerField(_("sorting"), blank=True, null=True)


class Personnel(models.Model):

    class PersonnelStatus(models.TextChoices):
        ACTIVE = "A", _("Active")
        INACTIVE = "I", _("Inactive")

    firstname = models.CharField(_("firstname"), max_length=200)
    lastname = models.CharField(_("lastname"), max_length=200)
    email = models.CharField(_("email"), max_length=200)
    mobile_phone = models.CharField(_("mobile phone"), max_length=200)
    status = models.CharField(_("status"),
                                  max_length=1, choices=PersonnelStatus.choices)
    mobile_phone_public = models.BooleanField(_("mobile phone publicly available"))
    date_of_birth = models.DateField(_("date of birth"))

    def __str__(self):
        return "%s, %s" % (self.firstname, self.lastname)


class Function(models.Model):

    class FunctionType(models.TextChoices):
        TRAIN = "T", _("Train")
        BAUMA = "B", _("Bauma")
        NEUTHAL = "N", _("Neuthal")
        BAERETSWIL = "X", _("Bäretswil")
        HINWIL = "H", _("Hinwil")

    label = models.CharField(_("label"), max_length=200)
    label_short = models.CharField(_("label short"), max_length=10)
    function_type = models.CharField(_("function_type"),
                                  max_length=1, choices=FunctionType.choices)
