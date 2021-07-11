from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils import dateformat, formats

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


class ReservationCalendarData(DvzoView):
    permission_required = 'train_management.view_dayplanning'

    def get(self, request):
        dayplannings_out = []
        color = 'grey'
        dayplannings = DayPlanning.objects.\
            exclude(Q(booking_status=DayPlanning.DayPlanningBookingStatus.CANCELLED_CUSTOMER) |
                    Q(booking_status=DayPlanning.DayPlanningBookingStatus.CANCELLED_DVZO))

        for dayplanning in dayplannings:
            date_formatted = dayplanning.date.strftime("%Y, %m, %d")
            dayplanning_type = dayplanning.day_planning_type

            if dayplanning_type == "sunday":
                color = '#ed174b'
            elif dayplanning_type == "extra":
                color = 'blue'

            single_dayplanning = {
                'id': dayplanning.id,
                'name': dayplanning.label,
                'startDate': date_formatted,
                'endDate': date_formatted,
                'color': color,
            }
            dayplannings_out.append(single_dayplanning)

        return JsonResponse(dayplannings_out, safe=False)
