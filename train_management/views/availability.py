from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from train_management.forms import AvailabilityForm
from train_management.models import Availability, Vehicle


@method_decorator(login_required, name='dispatch')
class AvailabilityListView(generic.ListView):
    context_object_name = "availabilities"

    def get_queryset(self):
        return Availability.objects.all()


@method_decorator(login_required, name='dispatch')
class AvailabilityEngineCreateView(generic.CreateView):
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
        return reverse_lazy("engine-detail", kwargs={'pk': self.object.vehicle.id})


@method_decorator(login_required, name='dispatch')
class AvailabilityCarriageCreateView(generic.CreateView):
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
        return reverse_lazy("carriage-detail", kwargs={'pk': self.object.vehicle.id})


@method_decorator(login_required, name='dispatch')
class AvailabilityEngineUpdateView(generic.UpdateView):
    model = Availability
    form_class = AvailabilityForm
    template_name = "train_management/availability_update_form.html"

    def get_success_url(self):
        return reverse_lazy("engine-detail", kwargs={'pk': self.object.vehicle.id})


@method_decorator(login_required, name='dispatch')
class AvailabilityCarriageUpdateView(generic.UpdateView):
    model = Availability
    form_class = AvailabilityForm
    template_name = "train_management/availability_update_form.html"

    def get_success_url(self):
        return reverse_lazy("carriage-detail", kwargs={'pk': self.object.vehicle.id})


@method_decorator(login_required, name='dispatch')
class AvailabilityDeleteView(generic.DeleteView):
    model = Availability
    template_name = "train_management/confirm_delete.html"
    success_url = reverse_lazy("dashboard")
