from django.db import models


class CarriageStatus(models.Model):
    label = models.CharField(max_length=200)
    sorting = models.IntegerField()

    def __str__(self):
        return self.label


class CarriageType(models.Model):
    label = models.CharField(max_length=200)
    sorting = models.IntegerField()

    def __str__(self):
        return self.label


class CarriageHome(models.Model):
    label = models.CharField(max_length=200)
    sorting = models.IntegerField()

    def __str__(self):
        return self.label


class PowerUnit(models.Model):
    label = models.CharField(max_length=200)
    sorting = models.IntegerField()

    def __str__(self):
        return self.label


class SteamHeating(models.Model):
    label = models.CharField(max_length=200)
    sorting = models.IntegerField()

    def __str__(self):
        return self.label


class Carriage(models.Model):
    label = models.CharField(max_length=200)
    historic_name = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    uic = models.CharField(max_length=200, blank=True)
    image = models.ImageField(blank=True, null=True)
    gross_weight = models.FloatField(blank=True, null=True)
    seats = models.IntegerField(blank=True, null=True)
    status = models.ForeignKey(CarriageStatus, on_delete=models.CASCADE)
    carriage_type = models.ForeignKey(CarriageType, on_delete=models.CASCADE)
    home = models.ForeignKey(CarriageHome, on_delete=models.CASCADE)
    start_year = models.IntegerField(blank=True, null=True)
    last_revision = models.DateField(blank=True, null=True)
    next_revision = models.DateField(blank=True, null=True)
    axles_distance = models.FloatField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    manufacturer = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.label


class Engine(models.Model):
    label = models.CharField(max_length=200)
    historic_name = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    uic = models.CharField(max_length=200, blank=True)
    image = models.ImageField(null=True)
    gross_weight = models.FloatField(blank=True)
    traction_25 = models.IntegerField(blank=True)
    traction_30 = models.IntegerField(blank=True)
    power_unit = models.ForeignKey(PowerUnit, on_delete=models.CASCADE)
    steam_heating = models.ForeignKey(SteamHeating, on_delete=models.CASCADE)
    status = models.ForeignKey(CarriageStatus, on_delete=models.CASCADE)
    carriage_type = models.ForeignKey(CarriageType, on_delete=models.CASCADE)
    home = models.ForeignKey(CarriageHome, on_delete=models.CASCADE)
    start_year = models.IntegerField(null=True)
    last_revision = models.DateField(null=True)
    next_revision = models.DateField(null=True)
    max_speed = models.IntegerField(blank=True)
    lup = models.CharField(max_length=200, blank=True)
    length = models.FloatField(blank=True)
    manufacturer = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.label
