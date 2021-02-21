from django.forms import CharField
from django.forms import ChoiceField
from django.forms import DateField
from django.forms import ModelForm
from django.forms import Select
from django.forms import TextInput

from train_management.models import DayPlanning


class DayPlanningForm(ModelForm):
    class Meta:
        model = DayPlanning
        fields = ['label', 'date', 'day_planning_type', 'status', 'paid']

    label = CharField(
        widget=TextInput(attrs={'class': 'form-control'}))
    date = DateField(
        widget=TextInput(attrs={'class': 'form-control', 'type': 'date'}))
    day_planning_type = ChoiceField(
        choices=DayPlanning.DayPlanningType.choices,
        widget=Select(attrs={'class': 'form-control'}))
    status = ChoiceField(
        choices=DayPlanning.DayPlanningStatus.choices,
        widget=Select(attrs={'class': 'form-control'}))
