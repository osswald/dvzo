from django.db import models
from django.utils.translation import gettext_lazy as _

from train_management.models import AbstractDvzoModel


class Vehicle(AbstractDvzoModel):

    class Meta:
        verbose_name = _("vehicle.singular")
        verbose_name_plural = _("vehicle.plural")

    class VehicleType(models.TextChoices):
        ENGINE = "engine", _("vehicle.type.engine")
        CARRIAGE = "carriage", _("vehicle.type.carriage")

    class Status(models.TextChoices):
        AVAILABLE = "available", _("vehicle.status.available")
        SERVICE = "servicing", _("vehicle.status.servicing")
        ASK = "ask", _("vehicle.status.ask")
        LOCKED = "locked", _("vehicle.status.locked")
        NOT_IN_SERVICE = "not_in_service", _("vehicle.status.not_in_service")

    class CarriageType(models.TextChoices):
        SEAT = "seat", _("vehicle.carriage_type.seat")
        GASTRO = "gastro", _("vehicle.carriage_type.gastro")
        LUGGAGE = "luggage", _("vehicle.carriage_type.luggage")
        CARGO = "cargo", _("vehicle.carriage_type.cargo")
        AMOR = "amor", _("vehicle.carriage_type.amor")

    class Home(models.TextChoices):
        BAUMA = "bauma", _("vehicle.home.bauma")
        USTER = "uster", _("vehicle.home.uster")
        WALD = "wald", _("vehicle.home.wald")

    class PowerUnit(models.TextChoices):
        STEAM = "steam", _("vehicle.power_unit.steam")
        DIESEL = "diesel", _("vehicle.power_unit.diesel")
        ELECTRIC = "electric", _("vehicle.power_unit.electric")
        DIESEL_ELECTRIC = "dieselelectric", _("vehicle.power_unit.dieselelectric")

    class SteamHeating(models.TextChoices):
        NO = "no", _("vehicle.steam_heating.no")
        FRONT = "front", _("vehicle.steam_heating.front")
        BACK = "back", _("vehicle.steam_heating.back")
        FRONT_BACK = "both", _("vehicle.steam_heating.both")

    label = models.CharField(_("vehicle.label"), max_length=200)
    historic_name = models.CharField(_("vehicle.historic_name"), max_length=200, blank=True)
    description = models.TextField(_("vehicle.description"), blank=True)
    uic = models.CharField(_("vehicle.uic"), max_length=200, blank=True)
    image = models.ImageField(_("vehicle.image"), blank=True, null=True)
    gross_weight = models.FloatField(_("vehicle.gross_weight"), blank=True, null=True)
    empty_weight = models.FloatField(_("vehicle.empty_weight"), blank=True, null=True)
    added_weight = models.FloatField(_("vehicle.added_weight"), blank=True, null=True)
    seats = models.IntegerField(_("vehicle.seats"), blank=True, null=True)
    vehicle_type = models.CharField(_("vehicle.type"),
                                    max_length=80, choices=VehicleType.choices)
    status = models.CharField(_("vehicle.status"),
                              max_length=80, choices=Status.choices, default=Status.AVAILABLE)
    carriage_type = models.CharField(_("vehiclecarriage_type"),
                                     max_length=80, choices=CarriageType.choices, blank=True)
    home = models.CharField(_("vehicle.home"),
                            max_length=80, choices=Home.choices)
    start_year = models.IntegerField(_("vehicle.start_year"), blank=True, null=True)
    last_revision = models.DateField(_("vehicle.last_revision"), blank=True, null=True)
    next_revision = models.DateField(_("vehicle.next_revision"), blank=True, null=True)
    axles_distance = models.FloatField(_("vehicle.axles_distance"), blank=True, null=True)
    length = models.FloatField(_("vehicle.length"), blank=True, null=True)
    manufacturer = models.CharField(_("vehicle.manufacturer"), max_length=200, blank=True)
    traction_25 = models.IntegerField(_("vehicle.traction_25"), blank=True, null=True)
    traction_30 = models.IntegerField(_("vehicle.traction_30"), blank=True, null=True)
    power_unit = models.CharField(_("vehicle.power_unit"),
                                  max_length=80, choices=PowerUnit.choices)
    steam_heating = models.CharField(_("vehicles.steam_heating"),
                                     max_length=80, choices=SteamHeating.choices)
    max_speed = models.IntegerField(_("vehicle.maximum_speed"), blank=True, null=True)

    def __str__(self):
        return self.label
