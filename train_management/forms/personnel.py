from django.forms import ModelForm
from tapeforms.contrib.bootstrap import BootstrapTapeformMixin

from train_management.models import Personnel


class PersonnelForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = Personnel
        fields = ['lastname',
                  'firstname',
                  'status',
                  'email',
                  'mobile_phone',
                  'mobile_phone_public',
                  'date_of_birth'
                  ]
