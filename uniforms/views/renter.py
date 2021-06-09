from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from uniforms.forms import RenterForm
from uniforms.models import Renter


@method_decorator(login_required, name='dispatch')
class RenterListView(generic.ListView):
    context_object_name = "renters"

    def get_queryset(self):
        return Renter.objects.all()


@method_decorator(login_required, name='dispatch')
class RenterDetailView(generic.DetailView):
    model = Renter
    context_object_name = "renters"
    template_name_suffix = "_detail_form"


@method_decorator(login_required, name='dispatch')
class RenterUpdateView(generic.UpdateView):
    model = Renter
    form_class = RenterForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("renter-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class RenterCreateView(generic.CreateView):
    model = Renter
    form_class = RenterForm
    template_name_suffix = "_create_form"

    def get_success_url(self):
        return reverse_lazy("renter-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class RenterDeleteView(generic.DeleteView):
    model = Renter
    template_name = "uniforms/confirm_delete.html"
    success_url = reverse_lazy("renter-list")
