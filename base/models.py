from django.db import models


class CarriageStatus(models.Model):
    label = models.CharField()
    sorting = models.IntegerField()


class CarriageType(models.Model):
    label = models.CharField()
    sorting = models.IntegerField()


class CarriageHome(models.Model):
    label = models.CharField()
    sorting = models.IntegerField()


class PowerUnit(models.Model):
    label = models.CharField()
    sorting = models.IntegerField()


class SteamHeating(models.Model):
    label = models.CharField()
    sorting = models.IntegerField()


class Carriage(models.Model):
    label = models.CharField()
    historic_name = models.CharField()
    description = models.TextField()
    uic = models.CharField()
    image = models.ImageField()
    gross_weight = models.FloatField()
    seats = models.IntegerField()
    status = models.ForeignKey(CarriageStatus, on_delete=models.CASCADE)
    type = models.ForeignKey(CarriageType, on_delete=models.CASCADE)
    home = models.ForeignKey(CarriageHome, on_delete=models.CASCADE)
    start_year = models.IntegerField()
    last_revision = models.DateField()
    next_revision = models.DateField()
    axles_distance = models.FloatField()
    length = models.FloatField()
    manufacturer = models.CharField()


class Engine(models.Model):
    label = models.CharField()
    historic_name = models.CharField()
    description = models.TextField()
    uic = models.CharField()
    image = models.ImageField()
    gross_weight = models.FloatField()
    traction_25 = models.IntegerField()
    traction_30 = models.IntegerField()
    power_unit = models.ForeignKey(PowerUnit, on_delete=models.CASCADE)
    steam_heating = models.ForeignKey(SteamHeating, on_delete=models.CASCADE)
    status = models.ForeignKey(CarriageStatus, on_delete=models.CASCADE)
    type = models.ForeignKey(CarriageType, on_delete=models.CASCADE)
    home = models.ForeignKey(CarriageHome, on_delete=models.CASCADE)
    start_year = models.IntegerField()
    last_revision = models.DateField()
    next_revision = models.DateField()
    max_speed = models.IntegerField()
    lup = models.CharField
    length = models.FloatField()
    manufacturer = models.CharField()
