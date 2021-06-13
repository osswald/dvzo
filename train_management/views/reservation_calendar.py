from django.shortcuts import get_object_or_404, render

from dvzo.views import DvzoView
from train_management.models import DayPlanning, TrainTimetable


class ReservationCalendar(DvzoView):
    permission_required = ''
    def get(self, request):
        return render(request, "train_management/reservation_calendar.html")


class ReservationCalendarTrains(DvzoView):
    permission_required = ''

    def get(self, request, pk, **kwargs):
        dayplanning = get_object_or_404(DayPlanning, pk=pk)
        traintimetables = TrainTimetable.objects.filter(train__in=dayplanning.train_set.all()).order_by("label")

        return render(self.request, 'train_management/reservation_calendar_trains.html',
                      {'traintimetables': traintimetables, 'dayplanning': dayplanning})
