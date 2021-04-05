from django.forms import ModelForm
from tapeforms.contrib.bootstrap import BootstrapTapeformMixin

from train_management.models import DayPlanning


class DayPlanningForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = DayPlanning
        fields = ['label',
                  'date',
                  'day_planning_type',
                  'status',
                  'paid',
                  'text'
                  ]
