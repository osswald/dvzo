from django.http import JsonResponse
from django.shortcuts import render
from django.utils import dateformat, formats

from dvzo.views import DvzoView
from train_management.models import Availability, Vehicle


class Calendar(DvzoView):
    permission_required = 'train_management.view_dayplanning'

    def get(self, request):

        return render(request, "train_management/calendar.html")


class CalendarAvailabilityData(DvzoView):
    permission_required = 'train_management.view_dayplanning'

    def get(self, request):
        availabilities_out = []
        availabilites = Availability.objects.all()

        for availability in availabilites:
            if availability.dayplanning:
                title = availability.dayplanning.label or ''
                color = 'blue'
            else:
                start_formatted = dateformat.format(availability.start, formats.get_format('DATE_FORMAT'))
                end_formatted = dateformat.format(availability.end, formats.get_format('DATE_FORMAT'))
                title = "%s (%s - %s)" % (availability.get_availability_status_display(),
                                          start_formatted, end_formatted)
                color = 'red' or ''

            single_availability = {
                'id': availability.id,
                'resourceId': availability.vehicle.id,
                'title': title,
                'start': availability.start.isoformat(),
                'end': availability.end.isoformat(),
                'color': color,
                'url': ''
            }
            availabilities_out.append(single_availability)

        return JsonResponse(availabilities_out, safe=False)


class CalendarResourceData(DvzoView):
    permission_required = 'train_management.view_dayplanning'

    def get(self, request):
        resources_out = []
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
