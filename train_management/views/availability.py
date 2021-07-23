from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from dvzo.views import DvzoCreateView
from dvzo.views import DvzoDeleteView
from dvzo.views import DvzoListView
from dvzo.views import DvzoUpdateView
from train_management.forms import AvailabilityForm
from train_management.models import Availability
from train_management.models import Vehicle


class AvailabilityListView(DvzoListView):
    permission_required = ""
    context_object_name = "availabilities"

    def get_queryset(self):
        return Availability.objects.all()


class AvailabilityEngineCreateView(DvzoCreateView):
    permission_required = ""
    model = Availability
    form_class = AvailabilityForm
    template_name = "train_management/availability_update_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, pk, **kwargs):
        self.vehicle = get_object_or_404(Vehicle, pk=pk)
        return super().post(request, **kwargs)

    def form_valid(self, form):
        form.instance.vehicle = self.vehicle
        return_value = super().form_valid(form)
        return return_value

    def get_success_url(self):
        return reverse_lazy("engine-detail", kwargs={"pk": self.object.vehicle.id})


class AvailabilityCarriageCreateView(DvzoCreateView):
    permission_required = ""
    model = Availability
    form_class = AvailabilityForm
    template_name = "train_management/availability_update_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, pk, **kwargs):
        self.vehicle = get_object_or_404(Vehicle, pk=pk)
        return super().post(request, **kwargs)

    def form_valid(self, form):
        form.instance.vehicle = self.vehicle
        return_value = super().form_valid(form)
        return return_value

    def get_success_url(self):
        return reverse_lazy("carriage-detail", kwargs={"pk": self.object.vehicle.id})


class AvailabilityEngineUpdateView(DvzoUpdateView):
    permission_required = ""
    model = Availability
    form_class = AvailabilityForm
    template_name = "train_management/availability_update_form.html"

    def get_success_url(self):
        return reverse_lazy("engine-detail", kwargs={"pk": self.object.vehicle.id})


class AvailabilityCarriageUpdateView(DvzoUpdateView):
    permission_required = ""
    model = Availability
    form_class = AvailabilityForm
    template_name = "train_management/availability_update_form.html"

    def get_success_url(self):
        return reverse_lazy("carriage-detail", kwargs={"pk": self.object.vehicle.id})


class AvailabilityDeleteView(DvzoDeleteView):
    permission_required = ""
    model = Availability
    template_name = "train_management/confirm_delete.html"
    success_url = reverse_lazy("availability-list")
