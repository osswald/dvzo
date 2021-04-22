from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.utils import dateformat, formats

from train_management.models import Availability, Vehicle


@login_required
def calendar(request):
    return render(request, "train_management/calendar.html")


def get_availability_data(peter):
    availabilities_out = []
    title = ''
    color = ''
    url = ''
    start_formatted = ''
    end_formatted = ''
    availabilites = Availability.objects.all()

    for availability in availabilites:
        if availability.dayplanning:
            title = availability.dayplanning.label
            url = ''
            color = 'blue'
        else:
            start_formatted = dateformat.format(availability.start, formats.get_format('DATE_FORMAT'))
            end_formatted = dateformat.format(availability.end, formats.get_format('DATE_FORMAT'))
            title = "%s (%s - %s)" % (availability.get_availability_status_display(),
                                      start_formatted, end_formatted)
            color = 'red'

        single_availability = {
            'id': availability.id,
            'resourceId': availability.vehicle.id,
            'title': title,
            'start': availability.start.isoformat(),
            'end': availability.end.isoformat(),
            'color': color,
            'url': url
        }
        availabilities_out.append(single_availability)

    return JsonResponse(availabilities_out, safe=False)


def get_resource_data(peter):
    resources_out = []
    vehicle_type = ''
    resources = Vehicle.objects.all()

    for resource in resources:
        if resource.vehicle_type == 'engine':
            vehicle_type = resource.get_vehicle_type_display()
        else:
            vehicle_type = resource.get_carriage_type_display()

        single_resource = {
            'id': resource.id,
            'vehicleType': vehicle_type,
            'title': resource.label
        }
        resources_out.append(single_resource)

    return JsonResponse(resources_out, safe=False)
