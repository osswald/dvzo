from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from train_management.models import DayPlanning
from train_management.models import Personnel
from train_management.models import Function
from train_management.forms import DayPlanningForm
from train_management.forms import PersonnelForm
from train_management.forms import FunctionForm


@login_required
def dashboard(request):
    return render(request, "train_management/dashboard.html")


@method_decorator(login_required, name='dispatch')
class DayPlanningListView(generic.ListView):
    context_object_name = "day_plannings"

    def get_queryset(self):
        return DayPlanning.objects.all()


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
        return Function.objects.all()


@method_decorator(login_required, name='dispatch')
class FunctionUpdateView(generic.UpdateView):
    model = Function
    form_class = FunctionForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("function-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class FunctionCreateView(generic.CreateView):
    model = Function
    form_class = FunctionForm
    template_name_suffix = "_create_form"

    def get_success_url(self):
        return reverse_lazy("function-detail", kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class FunctionDeleteView(generic.DeleteView):
    model = Function
    success_url = reverse_lazy("function-list")
