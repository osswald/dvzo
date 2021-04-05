from django.forms import ModelForm

from train_management.models import PhoneNumber, Personnel


class PhoneNumberForm(ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ['label', 'phone_number', 'phone_number_type']


class PhoneNumberPersonnelForm(ModelForm):
    class Meta:
        model = Personnel
        fields = ['lastname', 'firstname', 'status', 'mobile_phone', 'mobile_phone_public']
