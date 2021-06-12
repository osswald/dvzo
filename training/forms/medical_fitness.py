from django.forms import ModelForm
from tapeforms.contrib.bootstrap import BootstrapTapeformMixin

from training.models import MedicalFitness, MedicalFitnessLevel


class MedicalFitnessModuleForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = MedicalFitness
        fields = ['personnel',
                  'level',
                  'date'
                  ]


class MedicalFitnessLevelModuleForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = MedicalFitnessLevel
        fields = ['label']
