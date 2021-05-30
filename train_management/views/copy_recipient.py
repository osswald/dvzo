from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from train_management.forms import CopyRecipientForm
from train_management.models import CopyRecipient


@method_decorator(login_required, name='dispatch')
class CopyRecipientListView(generic.ListView):
    context_object_name = "copy_recipients"

    def get_queryset(self):
        return CopyRecipient.objects.all()


@method_decorator(login_required, name='dispatch')
class CopyRecipientUpdateView(generic.UpdateView):
    model = CopyRecipient
    form_class = CopyRecipientForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("copy-recipient-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class CopyRecipientCreateView(generic.CreateView):
    model = CopyRecipient
    form_class = CopyRecipientForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("copy-recipient-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class CopyRecipientDeleteView(generic.DeleteView):
    model = CopyRecipient
    template_name = "train_management/confirm_delete.html"
    success_url = reverse_lazy("copy-recipient-list")
