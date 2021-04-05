from django.forms import ModelForm
from tapeforms.contrib.bootstrap import BootstrapTapeformMixin

from train_management.models import TrainTimetableTemplate


class TrainTimetableTemplateForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = TrainTimetableTemplate
        fields = ['template_name',
                  'label',
                  'comment',
                  'start_station',
                  'start_time',
                  'destination_station',
                  'destination_time',
                  ]
