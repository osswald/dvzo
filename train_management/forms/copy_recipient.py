from django.forms import ModelForm
from tapeforms.contrib.bootstrap import BootstrapTapeformMixin

from train_management.models import CopyRecipient


class CopyRecipientForm(BootstrapTapeformMixin, ModelForm):
    field_container_css_class = "mb-3"

    class Meta:
        model = CopyRecipient
        fields = ["label", "email"]
