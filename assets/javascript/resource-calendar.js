import {Calendar} from "@fullcalendar/core";
import resourceTimelinePlugin from '@fullcalendar/resource-timeline';

document.addEventListener('DOMContentLoaded', function () {
  const calendarEl = document.getElementById('calendar');
  if (calendarEl !== null) {
    let calendar = new Calendar(calendarEl, {
      plugins: [resourceTimelinePlugin],
      schedulerLicenseKey: 'CC-Attribution-NonCommercial-NoDerivatives',
      locale: 'de',
      timeZone: 'UTC',
      slotLabelFormat: [
        {day: '2-digit'}
      ],
      initialView: 'resourceTimelineMonth',
      resourceAreaWidth: '20%',
      aspectRatio: 1.5,
      editable: true,
      resourceAreaHeaderContent: 'Fahrzeuge',
      resourceOrder: 'title',
      resourceGroupField: 'vehicleType',
      resources: '/calendar/resource_data',
      events: '/calendar/event_data'
    });

    calendar.render();
  }
});
