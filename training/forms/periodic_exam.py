from django.forms import ModelForm
from tapeforms.contrib.bootstrap import BootstrapTapeformMixin

from training.models import PeriodicExam


class PeriodicExamModuleForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = PeriodicExam
        fields = ['personnel',
                  'qualification',
                  'date'
                  ]
