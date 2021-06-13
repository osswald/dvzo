from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from dvzo.views import DvzoCreateView, DvzoDeleteView, DvzoListView, DvzoUpdateView
from train_management.forms import ReservationForm
from train_management.models import Reservation, TrainTimetable


class ReservationListView(DvzoListView):
    permission_required = ''
    model = Reservation
    context_object_name = "reservations"

    def get_queryset(self):
        return Reservation.objects.all()


class ReservationCreateView(DvzoCreateView):
    permission_required = ''
    model = Reservation
    form_class = ReservationForm
    template_name_suffix = "_update_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, pk, **kwargs):
        self.train = get_object_or_404(TrainTimetable, pk=pk)
        return super().post(request, **kwargs)

    def form_valid(self, form):
        form.instance.train_timetable = self.train
        return_value = super().form_valid(form)
        return return_value

    def get_success_url(self):
        return reverse_lazy("day-planning-detail", kwargs={'pk': self.object.train_timetable.train.day_planning.id})


class ReservationUpdateView(DvzoUpdateView):
    permission_required = ''
    model = Reservation
    form_class = ReservationForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("day-planning-detail", kwargs={'pk': self.object.train_timetable.train.day_planning.id})


class ReservationDeleteView(DvzoDeleteView):
    permission_required = ''
    model = Reservation
    template_name = "train_management/confirm_delete.html"
    success_url = reverse_lazy("day-planning-list")
