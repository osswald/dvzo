from datetime import date

from django.contrib.auth.decorators import login_required
from django.db.models import Q, Sum
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import dateformat, formats

from train_management.models import DayPlanning, Train


@login_required
def dashboard(request):
    future_dayplannings = DayPlanning.objects.filter(date__gte=date.today())
    next_sundays = future_dayplannings.filter(day_planning_type='sunday').order_by('date')[:3]
    next_extras = future_dayplannings.filter(day_planning_type='extra').order_by('date')[:3]
    next_others = future_dayplannings.filter(day_planning_type='other').order_by('date')[:3]
    personnel_missing = future_dayplannings.filter(personnel_disposition='open').order_by('date')[:5]
    slot_missing = future_dayplannings.filter(Q(slot_ordered='open') | Q(slot_ordered='ordered')).order_by('date')[:5]
    return render(request, "train_management/dashboard.html",
                  {
                      'next_sundays': next_sundays,
                      'next_extras': next_extras,
                      'next_others': next_others,
                      'personnel_missing': personnel_missing,
                      'slot_missing': slot_missing,
                  })


def get_frequency_chart_data(self):
    labels = []
    data = []

    sunday_2021 = DayPlanning.objects.filter(date__lte=date.today()).filter(date__gte=date(2021, 1, 1)).order_by('date')
    for sundays in sunday_2021:
        trains = Train.objects.filter(day_planning=sundays).aggregate(Sum('frequency'))
        date_formatted = dateformat.format(sundays.date, formats.get_format('DATE_FORMAT'))
        labels.append(date_formatted)
        data.append(trains['frequency__sum'])

    return JsonResponse(data={'labels': labels, 'data': data}, safe=False)
