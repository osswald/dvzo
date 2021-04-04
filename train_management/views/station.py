from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from train_management.forms import StationForm
from train_management.models import Station


@method_decorator(login_required, name='dispatch')
class StationListView(generic.ListView):
    context_object_name = "stations"

    def get_queryset(self):
        return Station.objects.all()


@method_decorator(login_required, name='dispatch')
class StationUpdateView(generic.UpdateView):
    model = Station
    form_class = StationForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("station-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class StationCreateView(generic.CreateView):
    model = Station
    form_class = StationForm
    template_name_suffix = "_create_form"

    def get_success_url(self):
        return reverse_lazy("station-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class StationDeleteView(generic.DeleteView):
    model = Station
    success_url = reverse_lazy("station-list")
