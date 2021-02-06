from django.contrib import admin
from .models import Carriage
from .models import Engine
from .models import CarriageStatus
from .models import CarriageHome
from .models import CarriageType
from .models import SteamHeating
from .models import PowerUnit

class CarriageAdmin(admin.ModelAdmin):
    list_display = ('label', 'uic', 'status')


admin.site.register(Carriage, CarriageAdmin)
admin.site.register(Engine)
admin.site.register(CarriageStatus)
admin.site.register(CarriageHome)
admin.site.register(CarriageType)
admin.site.register(SteamHeating)
admin.site.register(PowerUnit)
