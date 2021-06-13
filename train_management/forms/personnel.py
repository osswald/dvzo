from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from tapeforms.contrib.bootstrap import BootstrapTapeformMixin

from train_management.models import Personnel


class PersonnelForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = Personnel
        fields = ['category',
                  'status',
                  'mobile_phone',
                  'mobile_phone_public',
                  'date_of_birth'
                  ]

    date_of_birth = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d')
    )


class UserForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = get_user_model()
        fields = ['username',
                  'last_name',
                  'first_name',
                  'groups',
                  'is_active',
                  'email'
                  ]
