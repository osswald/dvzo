from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views import generic, View

from train_management.models import DayPlanning, TrainTimetable


class ReservationCalendar(View):
    def get(self, request):
        return render(request, "train_management/reservation_calendar.html")


@method_decorator(login_required, name='dispatch')
class ReservationCalendarTrains(generic.View):

    def get(self, request, pk, **kwargs):
        dayplanning = get_object_or_404(DayPlanning, pk=pk)
        traintimetables = TrainTimetable.objects.filter(train__in=dayplanning.train_set.all()).order_by("label")

        return render(self.request, 'train_management/reservation_calendar_trains.html',
            {'traintimetables': traintimetables, 'dayplanning': dayplanning})
