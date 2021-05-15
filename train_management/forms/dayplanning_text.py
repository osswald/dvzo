from django.forms import ModelForm
from tapeforms.contrib.bootstrap import BootstrapTapeformMixin

from train_management.models import DayPlanningText


class DayPlanningTextForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = DayPlanningText
        fields = ['label',
                  'text'
                  ]
