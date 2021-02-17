from datetime import date
import json

from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from train_management.models import DayPlanning
from train_management.models import Train


@login_required
def dashboard(request):
    return render(request, "train_management/dashboard.html")


@login_required
def day_planning_list(request):
    return render(request, "train_management/day_planning_list.html")


@login_required
def get_day_planning_data(request):
    plannings_out = []
    day_plannings = DayPlanning.objects.all()
    for day_planning in day_plannings:
        trains_for_planning = Train.objects.filter(day_planning=day_planning)

        for train in trains_for_planning:
            vehicles = train.vehicles
            current_vehicles = [{
                'vehicle_type': vehicle.vehicle_type,
                'vehicle_label': vehicle.label,
            } for vehicle in vehicles]

            # current_vehicles = "<span class="badge bg-success\">Peter</span>"
            planning = {
                'id': day_planning.id,
                'label': day_planning.label,
                'date': day_planning.date.isoformat(),
                'type': day_planning.day_planning_type,
                'vehicles': current_vehicles,
            }
            plannings_out.append(planning)

    return HttpResponse(
        json.dumps(plannings_out), content_type='application/json')
