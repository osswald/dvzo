from django.forms import ModelForm
from train_management.models import Train


class TrainForm(ModelForm):
    class Meta:
        model = Train
        fields = ['km', 'label']
