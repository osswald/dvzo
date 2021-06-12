from django.forms import ModelForm
from tapeforms.contrib.bootstrap import BootstrapTapeformMixin

from training.models import Qualification


class QualificationModuleForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = Qualification
        fields = ['label',
                  'description',
                  'type',
                  'valid_years'
                  ]
