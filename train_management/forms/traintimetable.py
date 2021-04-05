from django.forms import ModelForm

from train_management.models import TrainTimetable


class TrainTimetableForm(ModelForm):
    class Meta:
        model = TrainTimetable
        fields = ['label', 'comment', 'start_station', 'start_time', 'destination_station', 'destination_time', ]
