from django.forms import ModelForm
from tapeforms.contrib.bootstrap import BootstrapTapeformMixin

from training.models import Participant


class ParticipantModuleForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = Participant
        fields = ['personnel',
                  'attended',
                  'passed'
                  ]
