from django.forms import ModelForm

from train_management.models import DayPlanning
from train_management.models import Personnel
from train_management.models import DvzoFunction
from train_management.models import Train
from train_management.models import Vehicle


class DayPlanningForm(ModelForm):
    class Meta:
        model = DayPlanning
        fields = ['label', 'date', 'day_planning_type', 'status', 'paid', 'text']


class PersonnelForm(ModelForm):
    class Meta:
        model = Personnel
        fields = ['lastname', 'firstname', 'status', 'email', 'mobile_phone', 'mobile_phone_public', 'date_of_birth']


class FunctionForm(ModelForm):
    class Meta:
        model = DvzoFunction
        fields = ['label_short', 'label', 'function_type']


class TrainForm(ModelForm):
    class Meta:
        model = Train
        fields = ['km', 'label']


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
