from django.forms import ModelForm
from tapeforms.contrib.bootstrap import BootstrapTapeformMixin

from training.models import PersonnelQualification


class PersonnelQualificationModuleForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = PersonnelQualification
        fields = ['personnel',
                  'qualification',
                  'valid_until',
                  'automatically_added'
                  ]
