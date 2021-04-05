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
