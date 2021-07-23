from django.forms import ModelForm
from tapeforms.contrib.bootstrap import BootstrapTapeformMixin

from train_management.models import DvzoFunction


class FunctionForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = "mb-3"

    class Meta:
        model = DvzoFunction
        fields = ["label_short", "label", "function_type", "category", "sorting"]
