from django.forms import ModelForm
from tapeforms.contrib.bootstrap import BootstrapTapeformMixin

from train_management.models import Personnel, PhoneNumber


class PhoneNumberForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = PhoneNumber
        fields = ['label', 'phone_number', 'phone_number_type']


class PhoneNumberPersonnelForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = 'mb-3'

    class Meta:
        model = Personnel
        fields = ['lastname', 'firstname', 'status', 'mobile_phone', 'mobile_phone_public']
