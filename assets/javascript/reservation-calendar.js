import Calendar from "js-year-calendar";
import 'js-year-calendar/locales/js-year-calendar.de';
import $ from 'jquery';

let tooltip = null;

if ($('#reservation-calendar').length > 0) {
    $(function () {
        function ConvertJsonDateToDateTime(date) {
            let parsedDate = new Date(date);
            return new Date(parsedDate);
        }

        const data = $.getJSON('/reservation-calendar-data/')
            .done(function (responseData) {
                for (let i = 0; i < responseData.length; i++) {
                    responseData[i].startDate = ConvertJsonDateToDateTime(responseData[i].startDate);
                    responseData[i].endDate = ConvertJsonDateToDateTime(responseData[i].endDate);
                }
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
            })
    })

    document.querySelector('#reservation-calendar').addEventListener('clickDay', function (e) {
        if (e.events.length > 0){
            const id = e.events[0].id;
            window.location.pathname = ('/dayplanning/detail/' + id);
        }

    });
}
