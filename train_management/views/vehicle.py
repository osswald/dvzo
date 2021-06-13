from django.urls import reverse_lazy

from dvzo.views import DvzoCreateView, DvzoDeleteView, DvzoDetailView, DvzoListView, DvzoUpdateView
from train_management.forms import CarriageForm, EngineForm
from train_management.models import Availability, Vehicle


class CarriageListView(DvzoListView):
    permission_required = ''
    context_object_name = "carriages"
    queryset = Vehicle.objects.filter(vehicle_type="carriage")
    template_name = "train_management/carriage_list.html"


class CarriageUpdateView(DvzoUpdateView):
    permission_required = ''
    model = Vehicle
    form_class = CarriageForm
    template_name = "train_management/carriage_update_form.html"

    def get_success_url(self):
        return reverse_lazy("carriage-detail", kwargs={'pk': self.object.id})


class CarriageDetailView(DvzoDetailView):
    permission_required = ''
    model = Vehicle
    form_class = CarriageForm
    template_name = "train_management/carriage_detail_form.html"

    def get_context_data(self, **kwargs):
        availabilities = Availability.objects.filter(vehicle=self.object.id).order_by("start")
        return super().get_context_data(availabilities=availabilities, **kwargs)


class CarriageCreateView(DvzoCreateView):
    permission_required = ''
    model = Vehicle
    form_class = CarriageForm
    template_name = "train_management/carriage_create_form.html"

    def form_valid(self, form):
        form.instance.vehicle_type = "carriage"
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("carriage-list")


class CarriageDeleteView(DvzoDeleteView):
    permission_required = ''
    model = Vehicle
    template_name = "train_management/confirm_delete.html"
    success_url = reverse_lazy("carriage-list")


class EngineListView(DvzoListView):
    permission_required = ''
    context_object_name = "engines"
    queryset = Vehicle.objects.filter(vehicle_type="engine")
    template_name = "train_management/engine_list.html"


class EngineUpdateView(DvzoUpdateView):
    permission_required = ''
    model = Vehicle
    form_class = EngineForm
    template_name = "train_management/engine_update_form.html"

    def get_success_url(self):
        return reverse_lazy("engine-detail", kwargs={'pk': self.object.id})


class EngineDetailView(DvzoDetailView):
    permission_required = ''
    model = Vehicle
    form_class = EngineForm
    template_name = "train_management/engine_detail_form.html"

    def get_context_data(self, **kwargs):
        availabilities = Availability.objects.filter(vehicle=self.object.id).order_by("start")
        return super().get_context_data(availabilities=availabilities, **kwargs)


class EngineCreateView(DvzoCreateView):
    permission_required = ''
    model = Vehicle
    form_class = EngineForm
    template_name = "train_management/engine_create_form.html"

    def form_valid(self, form):
        form.instance.vehicle_type = "engine"
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("engine-list")


class EngineDeleteView(DvzoDeleteView):
    permission_required = ''
    model = Vehicle
    template_name = "train_management/confirm_delete.html"
    success_url = reverse_lazy("engine-list")
