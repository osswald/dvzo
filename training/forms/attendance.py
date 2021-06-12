from django.forms import ModelForm
from tapeforms.contrib.bootstrap import BootstrapTapeformMixin

from training.models import Attendance


class AttendanceModuleForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = Attendance
        fields = ['training_date',
                  'participant',
                  'attended'
                  ]
