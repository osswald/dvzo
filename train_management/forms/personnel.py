from django.contrib.auth.models import User
from django.forms import ModelForm
from tapeforms.contrib.bootstrap import BootstrapTapeformMixin

from train_management.models import Personnel


class PersonnelForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = Personnel
        fields = ['status',
                  'mobile_phone',
                  'mobile_phone_public',
                  'date_of_birth'
                  ]


class UserForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = User
        fields = ['username',
                  'last_name',
                  'first_name',
                  'is_active',
                  'email'
                  ]
