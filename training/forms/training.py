from django.forms import ModelForm
from tapeforms.contrib.bootstrap import BootstrapTapeformMixin

from training.models import Training, TrainingDate


class TrainingForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = Training
        fields = ['label',
                  'course_label',
                  'module',
                  'responsible',
                  'start_date',
                  'end_date'
                  ]


class TrainingDateForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = TrainingDate
        fields = ['label',
                  'responsible',
                  'start_datetime',
                  'end_datetime'
                  ]
