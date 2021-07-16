from django.urls import reverse_lazy

from dvzo.views import DvzoCreateView
from dvzo.views import DvzoDeleteView
from dvzo.views import DvzoListView
from dvzo.views import DvzoUpdateView
from train_management.forms import CopyRecipientForm
from train_management.models import CopyRecipient


class CopyRecipientListView(DvzoListView):
    permission_required = "train_management.view_copyrecipient"
    context_object_name = "copy_recipients"

    def get_queryset(self):
        return CopyRecipient.objects.all()


class CopyRecipientUpdateView(DvzoUpdateView):
    permission_required = "train_management.change_copyrecipient"
    model = CopyRecipient
    form_class = CopyRecipientForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("copy-recipient-detail", kwargs={"pk": self.object.id})


class CopyRecipientCreateView(DvzoCreateView):
    permission_required = "train_management.add_copyrecipient"
    model = CopyRecipient
    form_class = CopyRecipientForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("copy-recipient-detail", kwargs={"pk": self.object.id})


class CopyRecipientDeleteView(DvzoDeleteView):
    permission_required = "train_management.delete_copyrecipient"
    model = CopyRecipient
    template_name = "train_management/confirm_delete.html"
    success_url = reverse_lazy("copy-recipient-list")
