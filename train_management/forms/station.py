from django.forms import ModelForm

from train_management.models import Station


class StationForm(ModelForm):
    class Meta:
        model = Station
        fields = ['didok_nr', 'label', 'label_short']
