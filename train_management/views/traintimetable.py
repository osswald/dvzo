from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from dvzo.views import DvzoCreateView, DvzoDeleteView, DvzoUpdateView
from train_management.forms import TrainTimetableForm
from train_management.models import Train, TrainTimetable


class TrainTimetableCreateView(DvzoCreateView):
    permission_required = 'train_management.add_traintimetable'
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


class TrainTimetableUpdateView(DvzoUpdateView):
    permission_required = 'train_management.change_traintimetable'
    model = TrainTimetable
    form_class = TrainTimetableForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("day-planning-detail", kwargs={'pk': self.object.train.day_planning.id})


class TrainTimetableDeleteView(DvzoDeleteView):
    permission_required = 'train_management.delete_traintimetable'
    model = TrainTimetable
    template_name = "train_management/confirm_delete.html"
    success_url = reverse_lazy("day-planning-list")
