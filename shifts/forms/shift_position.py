from django.forms import ModelForm
from tapeforms.contrib.bootstrap import BootstrapTapeformMixin

from shifts.models import ShiftPosition


class ShiftPositionForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = ShiftPosition
        fields = ['label',
                  'type',
                  'start_time',
                  'end_time',
                  'start_station',
                  'end_station'
                  ]
