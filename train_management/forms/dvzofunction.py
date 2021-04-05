from django.forms import ModelForm

from train_management.models import DvzoFunction


class FunctionForm(ModelForm):
    class Meta:
        model = DvzoFunction
        fields = ['label_short', 'label', 'function_type', 'sorting']
