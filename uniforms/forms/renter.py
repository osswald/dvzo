from django.forms import ModelForm
from tapeforms.contrib.bootstrap import BootstrapTapeformMixin

from uniforms.models import Renter


class RenterForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = Renter
        fields = ['name',
                  'street',
                  'zip',
                  'city',
                  'phone',
                  'email'
                  ]
