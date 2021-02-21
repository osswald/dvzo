from datetime import date
import json

from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from train_management.forms import DayPlanningForm
from train_management.models import DayPlanning
from train_management.models import Train


@login_required
def dashboard(request):
    return render(request, "train_management/dashboard.html")


@login_required
def day_planning_list(request):
    return render(
        request, "train_management/day_planning_list.html", {'data': DayPlanning.objects.all()})


@login_required
def day_planning_detail(request, day_planning):
    if request.method == 'POST':
        day_planning_obj = DayPlanning.objects.get(id=day_planning)
        form = DayPlanningForm(request.POST, instance=day_planning_obj)
        if form.is_valid():
            form.save()
            return redirect('day-planning-list')

    day_planning_obj = DayPlanning.objects.get(id=day_planning)
    form = DayPlanningForm(instance=day_planning_obj)
    day_planning = DayPlanning.objects.get(id=day_planning)
    return render(
        request, "train_management/day_planning_detail.html",
        {'day_planning': day_planning_obj, 'form': form})

