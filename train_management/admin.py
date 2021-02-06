from django.contrib import admin
from .models import Vehicle, DayPlanning, Train
from .models import CarriageStatus, CarriageType, CarriageHome, SteamHeating, PowerUnit, VehicleType
from .models import DayPlanningType, DayPlanningStatus


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('label', 'vehicle_type', 'uic', 'status')


admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(DayPlanning)
admin.site.register(Train)

admin.site.register(CarriageStatus)
admin.site.register(CarriageHome)
admin.site.register(CarriageType)
admin.site.register(SteamHeating)
admin.site.register(PowerUnit)

admin.site.register(DayPlanningStatus)
admin.site.register(DayPlanningType)
