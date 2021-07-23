from django import forms
from django.forms import ModelForm
from tapeforms.contrib.bootstrap import BootstrapTapeformMixin

from train_management.models import Availability


class AvailabilityForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = "mb-3"

    class Meta:
        model = Availability
        fields = ["availability_status", "start", "end"]

    start = forms.DateField(widget=forms.DateInput(format="%Y-%m-%d"))
    end = forms.DateField(widget=forms.DateInput(format="%Y-%m-%d"))
