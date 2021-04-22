from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from train_management.forms import CarriageForm, EngineForm
from train_management.models import Availability,Vehicle


@method_decorator(login_required, name='dispatch')
class CarriageListView(generic.ListView):
    context_object_name = "carriages"
    queryset = Vehicle.objects.filter(vehicle_type="carriage")
    template_name = "train_management/carriage_list.html"


@method_decorator(login_required, name='dispatch')
class CarriageUpdateView(generic.UpdateView):
    model = Vehicle
    form_class = CarriageForm
    template_name = "train_management/carriage_update_form.html"

    def get_success_url(self):
        return reverse_lazy("carriage-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class CarriageDetailView(generic.DetailView):
    model = Vehicle
    form_class = CarriageForm
    template_name = "train_management/carriage_detail_form.html"

    def get_context_data(self, **kwargs):
        availabilities = Availability.objects.filter(vehicle=self.object.id).order_by("start")
        return super().get_context_data(availabilities=availabilities, **kwargs)


@method_decorator(login_required, name='dispatch')
class CarriageCreateView(generic.CreateView):
    model = Vehicle
    form_class = CarriageForm
    template_name = "train_management/carriage_create_form.html"

    def form_valid(self, form):
        form.instance.vehicle_type = "carriage"
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("carriage-list")


@method_decorator(login_required, name='dispatch')
class CarriageDeleteView(generic.DeleteView):
    model = Vehicle
    template_name = "train_management/confirm_delete.html"
    success_url = reverse_lazy("carriage-list")


@method_decorator(login_required, name='dispatch')
class EngineListView(generic.ListView):
    context_object_name = "engines"
    queryset = Vehicle.objects.filter(vehicle_type="engine")
    template_name = "train_management/engine_list.html"


@method_decorator(login_required, name='dispatch')
class EngineUpdateView(generic.UpdateView):
    model = Vehicle
    form_class = EngineForm
    template_name = "train_management/engine_update_form.html"

    def get_success_url(self):
        return reverse_lazy("engine-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class EngineDetailView(generic.DetailView):
    model = Vehicle
    form_class = EngineForm
    template_name = "train_management/engine_detail_form.html"

    def get_context_data(self, **kwargs):
        availabilities = Availability.objects.filter(vehicle=self.object.id).order_by("start")
        return super().get_context_data(availabilities=availabilities, **kwargs)


@method_decorator(login_required, name='dispatch')
class EngineCreateView(generic.CreateView):
    model = Vehicle
    form_class = EngineForm
    template_name = "train_management/engine_create_form.html"

    def form_valid(self, form):
        form.instance.vehicle_type = "engine"
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("engine-list")


@method_decorator(login_required, name='dispatch')
class EngineDeleteView(generic.DeleteView):
    model = Vehicle
    template_name = "train_management/confirm_delete.html"
    success_url = reverse_lazy("engine-list")
