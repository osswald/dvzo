import Calendar from "js-year-calendar";

const calendar = new Calendar('#reservation-calendar', {
  style:'background',
  language: 'de',
  dataSource: [
    {
      id: 0,
      name: 'Testfahrt 1',
      url: '/dayplanning/1',
      startDate: new Date(2021, 4, 2),
      endDate: new Date(2021, 4, 2),
      color: '#ed174b'
    },
  ]
});

document.querySelector('#reservation-calendar').addEventListener('clickDay', function (e) {
  window.location.pathname = ('/dayplanning/detail/2');
});

const dateToDisable = new Date(2021, 9, 5);
calendar.setDisabledDays([dateToDisable]);
