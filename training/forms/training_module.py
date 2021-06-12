from django.forms import ModelForm
from tapeforms.contrib.bootstrap import BootstrapTapeformMixin

from training.models import TrainingModule


class TrainingModuleForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = TrainingModule
        fields = ['label',
                  'label_short',
                  'description'
                  ]
