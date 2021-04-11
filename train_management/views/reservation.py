from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from train_management.forms import ReservationForm
from train_management.models import Reservation, TrainTimetable


@method_decorator(login_required, name='dispatch')
class ReservationListView(generic.ListView):
    model = Reservation
    context_object_name = "reservations"

    def get_queryset(self):
        return Reservation.objects.all()


@method_decorator(login_required, name='dispatch')
class ReservationCreateView(generic.CreateView):
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


@method_decorator(login_required, name='dispatch')
class ReservationUpdateView(generic.UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("day-planning-detail", kwargs={'pk': self.object.train_timetable.train.day_planning.id})


@method_decorator(login_required, name='dispatch')
class ReservationDeleteView(generic.DeleteView):
    model = Reservation
    template_name = "train_management/confirm_delete.html"
    success_url = reverse_lazy("day-planning-list")
