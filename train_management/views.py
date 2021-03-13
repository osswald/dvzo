from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from train_management.models import DayPlanning
from train_management.models import Personnel
from train_management.models import DvzoFunction
from train_management.models import Train
from train_management.models import Vehicle
from train_management.forms import DayPlanningForm
from train_management.forms import PersonnelForm
from train_management.forms import FunctionForm
from train_management.forms import TrainForm


@login_required
def dashboard(request):
    return render(request, "train_management/dashboard.html")


@method_decorator(login_required, name='dispatch')
class DayPlanningListView(generic.ListView):
    context_object_name = "day_plannings"

    def get_queryset(self):
        return DayPlanning.objects.all()


@method_decorator(login_required, name='dispatch')
class DayPlanningDetailView(generic.DetailView):
    model = DayPlanning
    form_class = DayPlanningForm
    template_name_suffix = "_detail_form"


@method_decorator(login_required, name='dispatch')
class DayPlanningUpdateView(generic.UpdateView):
    model = DayPlanning
    form_class = DayPlanningForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("day-planning-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class DayPlanningCreateView(generic.CreateView):
    model = DayPlanning
    form_class = DayPlanningForm
    template_name_suffix = "_create_form"

    def get_success_url(self):
        return reverse_lazy("day-planning-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class DayPlanningDeleteView(generic.DeleteView):
    model = DayPlanning
    success_url = reverse_lazy("day-planning-list")


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
    success_url = reverse_lazy("personnel-list")


@method_decorator(login_required, name='dispatch')
class FunctionListView(generic.ListView):
    context_object_name = "functions"

    def get_queryset(self):
        return DvzoFunction.objects.all()


@method_decorator(login_required, name='dispatch')
class FunctionUpdateView(generic.UpdateView):
    model = DvzoFunction
    form_class = FunctionForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("function-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class FunctionCreateView(generic.CreateView):
    model = DvzoFunction
    form_class = FunctionForm
    template_name_suffix = "_create_form"

    def get_success_url(self):
        return reverse_lazy("function-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class FunctionDeleteView(generic.DeleteView):
    model = DvzoFunction
    success_url = reverse_lazy("function-list")


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
