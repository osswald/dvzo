from django.contrib import admin
from .models import Vehicle, DayPlanning, Train


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('label', 'type', 'uic', 'status')


admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(DayPlanning)
admin.site.register(Train)
