from django.forms import ModelForm
from tapeforms.contrib.bootstrap import BootstrapTapeformMixin

from shifts.models import ShiftPositionType


class ShiftPositionTypeForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = ShiftPositionType
        fields = ['label',
                  'work_time',
                  ]
