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


class DayPlanningType(models.Model):
    label = models.CharField(max_length=200)
    sorting = models.IntegerField()

    def __str__(self):
        return self.label


class DayPlanningStatus(models.Model):
    label = models.CharField(max_length=200)
    sorting = models.IntegerField()

    def __str__(self):
        return self.label


class VehicleType(models.Model):
    label = models.CharField(max_length=200)
    sorting = models.IntegerField()

    def __str__(self):
        return self.label


class PersonnelStatus(models.Model):
    label = models.CharField(max_length=200)
    sorting = models.IntegerField()

    def __str__(self):
        return self.label


class FunctionType(models.Model):
    label = models.CharField(max_length=200)
    sorting = models.IntegerField()

    def __str__(self):
        return self.label


class Vehicle(models.Model):
    label = models.CharField(max_length=200)
    historic_name = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    uic = models.CharField(max_length=200, blank=True)
    image = models.ImageField(blank=True, null=True)
    gross_weight = models.FloatField(blank=True, null=True)
    seats = models.IntegerField(blank=True, null=True)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    status = models.ForeignKey(CarriageStatus, on_delete=models.CASCADE)
    carriage_type = models.ForeignKey(CarriageType, on_delete=models.CASCADE)
    home = models.ForeignKey(CarriageHome, on_delete=models.CASCADE)
    start_year = models.IntegerField(blank=True, null=True)
    last_revision = models.DateField(blank=True, null=True)
    next_revision = models.DateField(blank=True, null=True)
    axles_distance = models.FloatField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    manufacturer = models.CharField(max_length=200, blank=True)
    traction_25 = models.IntegerField(blank=True)
    traction_30 = models.IntegerField(blank=True)
    power_unit = models.ForeignKey(PowerUnit, on_delete=models.CASCADE)
    steam_heating = models.ForeignKey(SteamHeating, on_delete=models.CASCADE)
    max_speed = models.IntegerField(blank=True)
    lup = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.label


class DayPlanning(models.Model):
    label = models.CharField(max_length=200)
    day_planning_type = models.ForeignKey(DayPlanningType, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.ForeignKey(DayPlanningStatus, on_delete=models.CASCADE)
    paid = models.BooleanField

    def __str__(self):
        return self.label


class Train(models.Model):
    label = models.CharField(max_length=200)
    km = models.IntegerField(blank=True)
    day_planning = models.ForeignKey(DayPlanning, on_delete=models.CASCADE)

    def __str__(self):
        return self.label


class TrainConfiguration(models.Model):
    engine = models.ForeignKey(Vehicle, null=True, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    sorting = models.IntegerField(blank=True)


class Personnel(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    mobile_phone = models.CharField(max_length=200)
    status = models.ForeignKey(PersonnelStatus, on_delete=models.CASCADE)
    mobile_phone_public = models.BooleanField
    date_of_birth = models.DateField

    def __str__(self):
        return "%s, %s" % (self.firstname, self.lastname)


class Function(models.Model):
    label = models.CharField(max_length=200)
    label_short = models.CharField(max_length=10)
    function_type = models.ForeignKey(FunctionType, on_delete=models.CASCADE)
