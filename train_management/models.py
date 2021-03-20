from django.db import models
from django.utils.translation import gettext_lazy as _


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

    label = models.CharField(_("label"), max_length=200)
    day_planning_type = models.CharField(_("day_planning_type"),
                                  max_length=80, choices=DayPlanningType.choices)
    date = models.DateField(_("date"))
    status = models.CharField(_("status"),
                                max_length=80, choices=DayPlanningStatus.choices)
    paid = models.BooleanField(_("paid"), default=False)
    text = models.CharField(_("Text"), max_length=5000, blank=True)

    def __str__(self):
        return self.label


class Train(models.Model):

    class Meta:
        verbose_name = _("Train")
        verbose_name_plural = _("Trains")

    label = models.CharField(_("label"), max_length=200)
    km = models.IntegerField(_("km"), blank=True)
    day_planning = models.ForeignKey(DayPlanning, on_delete=models.CASCADE)

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


class Personnel(models.Model):

    class Meta:
        verbose_name = _("Personnel")
        verbose_name_plural = _("Personnel")

    class PersonnelStatus(models.TextChoices):
        ACTIVE = "active", _("Active")
        INACTIVE = "inactive", _("Inactive")

    firstname = models.CharField(_("firstname"), max_length=200)
    lastname = models.CharField(_("lastname"), max_length=200)
    email = models.CharField(_("email"), max_length=200)
    mobile_phone = models.CharField(_("mobile phone"), max_length=200)
    status = models.CharField(_("status"),
                                  max_length=80, choices=PersonnelStatus.choices)
    mobile_phone_public = models.BooleanField(_("mobile phone publicly available"))
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


class Mileage(models.Model):

    class Meta:
        verbose_name = _("Mileage")
        verbose_name_plural = _("Mileages")

    date = models.DateField(_("date"))
    label = models.CharField(_("label"), max_length=200, blank=True)
    train = models.ForeignKey(Train, on_delete=models.CASCADE, null=True)


class TrainFunction(models.Model):

    class Meta:
        verbose_name = _("Train function")
        verbose_name_plural = _("Train functions")

    train = models.OneToOneField(Train, on_delete=models.CASCADE)
    driver = models.ManyToManyField(Personnel, related_name="driver", blank=True)
    stoker_early = models.ManyToManyField(Personnel, related_name="stoker_early", blank=True)
    stoker_middle = models.ManyToManyField(Personnel, related_name="stoker_middle", blank=True)
    stoker_late = models.ManyToManyField(Personnel, related_name="stoker_late", blank=True)
    accomp_z = models.ManyToManyField(Personnel, related_name="accomp_z", blank=True)
    accomp_k = models.ManyToManyField(Personnel, related_name="accomp_k", blank=True)
    accomp_b = models.ManyToManyField(Personnel, related_name="accomp_b", blank=True)
    shunting_assistant = models.ManyToManyField(Personnel, related_name="shunting_assistant", blank=True)
    shunting = models.ManyToManyField(Personnel, related_name="shunting", blank=True)
    gastro = models.ManyToManyField(Personnel, related_name="gastro", blank=True)


class DayPlanningFunction(models.Model):

    class Meta:
        verbose_name = _("Day planning function")
        verbose_name_plural = _("Day planning functions")

    dayplanning = models.OneToOneField(DayPlanning, on_delete=models.CASCADE)
    sales_hi = models.ManyToManyField(Personnel, related_name="sales_hi", blank=True)
    coordinator_baew = models.ManyToManyField(Personnel, related_name="coordinator_baew", blank=True)
    station_baew = models.ManyToManyField(Personnel, related_name="station_baew", blank=True)
    barrier_baew = models.ManyToManyField(Personnel, related_name="barrier_baew", blank=True)
    barrier_neu = models.ManyToManyField(Personnel, related_name="barrier_neu", blank=True)
    coordinator_bma = models.ManyToManyField(Personnel, related_name="coordinator_bma", blank=True)
    station_bma = models.ManyToManyField(Personnel, related_name="station_bma", blank=True)
    barrier_bma = models.ManyToManyField(Personnel, related_name="barrier_bma", blank=True)
    engine_assistant_bma = models.ManyToManyField(Personnel, related_name="engine_assistant_bma", blank=True)
    food_bma = models.ManyToManyField(Personnel, related_name="food_bma", blank=True)
