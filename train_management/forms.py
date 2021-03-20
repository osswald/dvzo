from django.forms import ModelForm

from train_management.models import DayPlanning
from train_management.models import Personnel
from train_management.models import DvzoFunction
from train_management.models import Train
from train_management.models import DayPlanningFunction
from train_management.models import TrainFunction


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


class TrainFunctionForm(ModelForm):
    class Meta:
        model = TrainFunction
        fields = ['train',
                  'driver',
                  'stoker_early',
                  'stoker_middle',
                  'stoker_late',
                  'accomp_z',
                  'accomp_k',
                  'accomp_b',
                  'shunting',
                  'gastro'
                  ]


class DayPlanningFunctionForm(ModelForm):
    class Meta:
        model = DayPlanningFunction
        fields = '__all__'
