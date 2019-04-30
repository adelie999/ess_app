document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        plugins: ['dayGrid', 'timeGrid', 'list', 'interaction'],
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay,listWeek'
        },
        defaultDate: '2019-04-12',
        navLinks: true, // can click day/week names to navigate views
        editable: true,
        eventLimit: true, // allow "more" link when too many events
        locale: 'ja',
        events: [{
                title: 'All Day Event',
                start: '2019-04-01',
            },
            {
                title: 'Long Event',
                start: '2019-04-07',
                end: '2019-04-10'
            },
            {
                groupId: 999,
                title: 'Repeating Event',
                start: '2019-04-09T16:00:00'
            },
            {
                groupId: 999,
                title: 'Repeating Event',
                start: '2019-04-16T16:00:00'
            },
            {
                title: 'Conference',
                start: '2019-04-11',
                end: '2019-04-13'
            },
            {
                title: 'Meeting',
                start: '2019-04-12T10:30:00',
                end: '2019-04-12T12:30:00'
            },
            {
                title: 'Lunch',
                start: '2019-04-12T12:00:00'
            },
            {
                title: 'Meeting',
                start: '2019-04-12T14:30:00'
            },
            {
                title: 'Happy Hour',
                start: '2019-04-12T17:30:00'
            },
            {
                title: 'Dinner',
                start: '2019-04-12T20:00:00'
            },
            {
                title: 'Birthday Party',
                start: '2019-04-13T07:00:00'
            },
            {
                title: 'Click for Google',
                url: 'http://google.com/',
                start: '2019-04-28'
            }
        ]
    });

    calendar.render();
});