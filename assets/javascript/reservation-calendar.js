import Calendar from "js-year-calendar";
import 'js-year-calendar/locales/js-year-calendar.de';
import $ from 'jquery';

let tooltip = null;

/*$.ajax({
    type: "POST",
    url: "/reservation-calendar-data/",
    data: {},
    contentType: "application/json; charset=utf-8",
    dataType: "json",
    success: function (r) {
        for (let i = 0; i < r.d.length; i++) {
            r.d[i].startDate = ConvertJsonDateToDateTime(r.d[i].startDate);
            r.d[i].endDate = ConvertJsonDateToDateTime(r.d[i].endDate);
        }
    }
})*/

// const data = [
//                 {
//                     id: 0,
//                     name: 'Fahrsonntag 1',
//                     url: '/dayplanning/1',
//                     startDate: new Date(2021, 4, 2),
//                     endDate: new Date(2021, 4, 2),
//                     color: '#ed174b'
//                 },
//                 {
//                     id: 0,
//                     name: 'Extrafahrt 2',
//                     url: '/dayplanning/1',
//                     startDate: new Date(2021, 7, 2),
//                     endDate: new Date(2021, 7, 2),
//                     color: 'blue'
//                 },
//                 {
//                     id: 0,
//                     name: 'Überfuhr',
//                     url: '/dayplanning/1',
//                     startDate: new Date(2021, 8, 2),
//                     endDate: new Date(2021, 8, 2),
//                     color: 'grey'
//                 },
//                 {
//                     id: 0,
//                     name: 'Testdata',
//                     url: '/dayplanning/1',
//                     startDate: new Date(2021, 8, 2),
//                     endDate: new Date(2021, 8, 2),
//                     color: 'blue'
//                 },
//             ]

if ($('#reservation-calendar').length > 0) {
    const data = $.getJSON('/reservation-calendar-data/',)
    const responseData = data.responseJSON
    const calendar = new Calendar('#reservation-calendar', {
        style: 'background',
        language: 'de',
        dataSource: responseData,
        mouseOnDay: function (e) {
            if (e.events.length > 0) {
                let content = '';

                for (const i in e.events) {
                    content += '<div class="event-tooltip-content">'
                        + '<div class="event-name">' + e.events[i].name + '</div>'
                        + '</div>';
                }

                if (tooltip !== null) {
                    tooltip.destroy();
                    tooltip = null;
                }

                tooltip = tippy(e.element, {
                    placement: 'right',
                    content: content,
                    animateFill: false,
                    animation: 'shift-away',
                    arrow: true,
                    allowHTML: true
                });
                tooltip.show();
            }
        },
        mouseOutDay: function () {
            if (tooltip !== null) {
                tooltip.destroy();
                tooltip = null;
            }
        }
    });

    document.querySelector('#reservation-calendar').addEventListener('clickDay', function (e) {
        window.location.pathname = ('/dayplanning/detail/2');
    });
}
