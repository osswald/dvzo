from django.forms import ModelForm
from tapeforms.contrib.bootstrap import BootstrapTapeformMixin

from shifts.models import ShiftTemplate


class ShiftTemplateForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = ShiftTemplate
        fields = ['label',
                  'description',
                  'active',
                  'category'
                  ]
