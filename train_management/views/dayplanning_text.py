from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from dvzo.views import DvzoCreateView
from dvzo.views import DvzoDeleteView
from dvzo.views import DvzoUpdateView
from train_management.forms import DayPlanningTextForm
from train_management.models import DayPlanning
from train_management.models import DayPlanningText


class DayPlanningTextUpdateView(DvzoUpdateView):
    permission_required = "train_management.change_dayplanningtext"
    model = DayPlanningText
    form_class = DayPlanningTextForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("day-planning-detail", kwargs={"pk": self.object.dayplanning.id})


class DayPlanningTextCreateView(DvzoCreateView):
    permission_required = "train_management.add_dayplanningtext"
    model = DayPlanningText
    form_class = DayPlanningTextForm
    template_name_suffix = "_update_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, pk, **kwargs):
        self.dayplanning = get_object_or_404(DayPlanning, pk=pk)
        return super().post(request, **kwargs)

    def form_valid(self, form):
        form.instance.dayplanning = self.dayplanning
        return_value = super().form_valid(form)
        return return_value

    def get_success_url(self):
        return reverse_lazy("day-planning-detail", kwargs={"pk": self.object.dayplanning.id})


class DayPlanningTextDeleteView(DvzoDeleteView):
    permission_required = "train_management.delete_dayplanningtext"
    model = DayPlanningText

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy("day-planning-detail", kwargs={"pk": self.object.dayplanning.id})
