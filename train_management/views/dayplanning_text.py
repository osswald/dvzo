from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from train_management.forms import DayPlanningTextForm
from train_management.models import DayPlanning, DayPlanningText


@method_decorator(login_required, name='dispatch')
class DayPlanningTextUpdateView(generic.UpdateView):
    model = DayPlanningText
    form_class = DayPlanningTextForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("day-planning-detail", kwargs={'pk': self.object.dayplanning.id})


@method_decorator(login_required, name='dispatch')
class DayPlanningTextCreateView(generic.CreateView):
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
        return reverse_lazy("day-planning-detail", kwargs={'pk': self.object.dayplanning.id})


@method_decorator(login_required, name='dispatch')
@method_decorator(permission_required('delete_dayplanning_text', raise_exception=True), name='dispatch')
class DayPlanningTextDeleteView(generic.DeleteView):
    model = DayPlanningText

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy("day-planning-detail", kwargs={'pk': self.object.dayplanning.id})
