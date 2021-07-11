import Calendar from "js-year-calendar";
import 'js-year-calendar/locales/js-year-calendar.de';
import $ from 'jquery';

let tooltip = null;

if ($('#reservation-calendar').length > 0) {
    $(function () {
        function ConvertJsonDateToDateTime(date) {
            return new Date(date);
        }

        const data = $.getJSON('/reservation-calendar-data/')
            .done(function (responseData) {
                responseData.forEach((entry) => {
                    entry.startDate = ConvertJsonDateToDateTime(entry.startDate);
                    entry.endDate = ConvertJsonDateToDateTime(entry.endDate);
                })
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
            })
    })

    document.querySelector('#reservation-calendar').addEventListener('clickDay', function (e) {
        if (e.events.length > 0){
            const id = e.events[0].id;
            window.location.pathname = ('/dayplanning/detail/' + id);
        }

    });
}
