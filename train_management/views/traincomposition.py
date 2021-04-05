from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from train_management.forms import TrainForm
from train_management.models import DayPlanning, Train, Vehicle


@method_decorator(login_required, name='dispatch')
class TrainCompositionUpdateView(generic.UpdateView):
    model = Train
    form_class = TrainForm
    template_name_suffix = "_update_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["available_vehicles"] = Vehicle.objects.all().exclude(trainconfiguration__train=self.object)
        return context

    def post(self, request, pk, **kwargs):
        vehicle_ids = request.POST["ordering"].split(",")
        vehicles = [get_object_or_404(Vehicle, pk=pk) for pk in vehicle_ids]
        train = get_object_or_404(Train, pk=pk)
        train.set_composition(vehicles)
        return super().post(request, **kwargs)

    def get_success_url(self):
        return reverse_lazy("day-planning-detail", kwargs={'pk': self.object.day_planning.id})


@method_decorator(login_required, name='dispatch')
class TrainCompositionCreateView(generic.CreateView):
    model = Train
    form_class = TrainForm
    template_name_suffix = "_update_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["available_vehicles"] = Vehicle.objects.all()
        return context

    def post(self, request, pk, **kwargs):
        vehicle_ids = request.POST["ordering"].split(",")
        self.vehicles = [get_object_or_404(Vehicle, pk=pk) for pk in vehicle_ids]
        self.day_planning = get_object_or_404(DayPlanning, pk=pk)
        return super().post(request, **kwargs)

    def form_valid(self, form):
        form.instance.day_planning = self.day_planning
        return_value = super().form_valid(form)
        self.object.set_composition(self.vehicles)
        return return_value

    def get_success_url(self):
        return reverse_lazy("day-planning-detail", kwargs={'pk': self.object.day_planning.id})
