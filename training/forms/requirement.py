from django.forms import ModelForm
from tapeforms.contrib.bootstrap import BootstrapTapeformMixin

from training.models import Requirement


class RequirementForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = Requirement
        fields = ['qualification',
                  'module',
                  'medical_fitness',
                  'periodic_exam'
                  ]
