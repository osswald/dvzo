from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from train_management.forms import PersonnelForm
from train_management.models import Personnel


@method_decorator(login_required, name='dispatch')
class PersonnelListView(generic.ListView):
    context_object_name = "personnels"

    def get_queryset(self):
        return Personnel.objects.all()


@method_decorator(login_required, name='dispatch')
class PersonnelUpdateView(generic.UpdateView):
    model = Personnel
    form_class = PersonnelForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("personnel-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class PersonnelCreateView(generic.CreateView):
    model = Personnel
    form_class = PersonnelForm
    template_name_suffix = "_create_form"

    def get_success_url(self):
        return reverse_lazy("personnel-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class PersonnelDeleteView(generic.DeleteView):
    model = Personnel
    template_name = "train_management/confirm_delete.html"
    success_url = reverse_lazy("personnel-list")
