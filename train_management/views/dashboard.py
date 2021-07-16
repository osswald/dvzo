from datetime import date

from django.db.models import Q
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import dateformat
from django.utils import formats

from dvzo.views import DvzoView
from train_management.models import DayPlanning
from train_management.models import Train


class Dashboard(DvzoView):
    permission_required = "train_management.view_dayplanning"

    def get(self, request):
        future_dayplannings = DayPlanning.objects.filter(date__gte=date.today())
        next_sundays = future_dayplannings.filter(day_planning_type="sunday").order_by("date")[:3]
        next_extras = future_dayplannings.filter(day_planning_type="extra").order_by("date")[:3]
        next_others = future_dayplannings.filter(day_planning_type="other").order_by("date")[:3]
        personnel_missing = future_dayplannings.filter(personnel_disposition="open").order_by("date")[:5]
        slot_missing = future_dayplannings.filter(
            Q(slot_ordered_st="open")
            | Q(slot_ordered_st="ordered")
            | Q(slot_ordered_sbb="open")
            | Q(slot_ordered_sbb="ordered")
        ).order_by("date")[:5]
        return render(
            request,
            "train_management/dashboard.html",
            {
                "next_sundays": next_sundays,
                "next_extras": next_extras,
                "next_others": next_others,
                "personnel_missing": personnel_missing,
                "slot_missing": slot_missing,
            },
        )


class FrequencyChartData(DvzoView):
    permission_required = "train_management.view_dayplanning"

    def get(self, request):
        labels = []
        data = []

        sunday_2021 = (
            DayPlanning.objects.filter(date__lte=date.today(), day_planning_type="sunday")
            .filter(date__gte=date(2021, 1, 1))
            .order_by("date")
        )
        for sundays in sunday_2021:
            trains = Train.objects.filter(day_planning=sundays).aggregate(Sum("frequency"))
            date_formatted = dateformat.format(sundays.date, formats.get_format("DATE_FORMAT"))
            labels.append(date_formatted)
            data.append(trains["frequency__sum"])

        return JsonResponse(data={"labels": labels, "data": data}, safe=False)
