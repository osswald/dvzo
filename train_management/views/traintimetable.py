from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from train_management.forms import TrainTimetableForm
from train_management.models import TrainTimetable, Train


@method_decorator(login_required, name='dispatch')
class TrainTimetableCreateView(generic.CreateView):
    model = TrainTimetable
    form_class = TrainTimetableForm
    template_name_suffix = "_update_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, pk, **kwargs):
        self.train = get_object_or_404(Train, pk=pk)
        return super().post(request, **kwargs)

    def form_valid(self, form):
        form.instance.train = self.train
        return_value = super().form_valid(form)
        return return_value

    def get_success_url(self):
        return reverse_lazy("day-planning-detail", kwargs={'pk': self.object.train.day_planning.id})


@method_decorator(login_required, name='dispatch')
class TrainTimetableUpdateView(generic.UpdateView):
    model = TrainTimetable
    form_class = TrainTimetableForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("day-planning-detail", kwargs={'pk': self.object.train.day_planning.id})


@method_decorator(login_required, name='dispatch')
class TrainTimetableDeleteView(generic.DeleteView):
    model = TrainTimetable
    success_url = reverse_lazy("day-planning-list")
