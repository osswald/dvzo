from django.forms import CharField
from django.forms import ChoiceField
from django.forms import DateField
from django.forms import ModelForm
from django.forms import Select
from django.forms import TextInput
from django.forms import Textarea
from django.forms import EmailInput

from train_management.models import DayPlanning
from train_management.models import Personnel


class DayPlanningForm(ModelForm):
    class Meta:
        model = DayPlanning
        fields = ['label', 'date', 'day_planning_type', 'status', 'paid', 'text']

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
    text = CharField(
        widget = Textarea(
            attrs={'class': 'form-control'}))


class PersonnelForm(ModelForm):
    class Meta:
        model = Personnel
        fields = ['lastname', 'firstname', 'status', 'email', 'mobile_phone', 'mobile_phone_public', 'date_of_birth']

    lastname = CharField(
        widget=TextInput(attrs={'class': 'form-control'}))
    firstname = CharField(
        widget=TextInput(attrs={'class': 'form-control'}))
    status = ChoiceField(
        choices=Personnel.PersonnelStatus.choices,
        widget=Select(attrs={'class': 'form-control'}))
    email = CharField(
        widget=EmailInput(attrs={'class': 'form-control'}))
    mobile_phone = CharField(
        widget=TextInput(attrs={'class': 'form-control'}))
    date_of_birth = DateField(
        widget=TextInput(attrs={'class': 'form-control', 'type': 'date'}))

