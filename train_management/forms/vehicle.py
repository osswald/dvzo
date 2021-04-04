from django.forms import ModelForm
from train_management.models import Vehicle


class EngineForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = ['label',
                  'historic_name',
                  'description',
                  'uic',
                  'image',
                  'gross_weight',
                  'status',
                  'home',
                  'start_year',
                  'last_revision',
                  'next_revision',
                  'axles_distance',
                  'length',
                  'manufacturer',
                  'traction_25',
                  'traction_30',
                  'power_unit',
                  'steam_heating',
                  'max_speed'
                  ]


class CarriageForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = ['label',
                  'historic_name',
                  'description',
                  'uic',
                  'image',
                  'gross_weight',
                  'seats',
                  'status',
                  'carriage_type',
                  'home',
                  'start_year',
                  'last_revision',
                  'next_revision',
                  'axles_distance',
                  'length',
                  'manufacturer',
                  'max_speed'
                  ]
