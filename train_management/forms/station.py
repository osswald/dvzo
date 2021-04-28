from django.forms import ModelForm
from tapeforms.contrib.bootstrap import BootstrapTapeformMixin

from train_management.models import Station


class StationForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = Station
        fields = ['didok_nr',
                  'label',
                  'label_short',
                  'neighbours'
                  ]
