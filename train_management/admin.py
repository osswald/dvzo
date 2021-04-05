from django.contrib import admin

from .models import DayPlanning, Train, Vehicle


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('label', 'vehicle_type', 'uic', 'status')


admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(DayPlanning)
admin.site.register(Train)
