from django.forms import ModelForm
from tapeforms.contrib.bootstrap import BootstrapTapeformMixin

from train_management.models import TrainTimetable


class TrainTimetableForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = TrainTimetable
        fields = ['label',
                  'comment',
                  'start_station',
                  'start_time',
                  'destination_station',
                  'destination_time',
                  ]
