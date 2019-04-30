
document.addEventListener('DOMContentLoaded', function () {
    
    var calendarEl1 = document.getElementById('calendar-list');

    var calendar2 = new FullCalendar.Calendar(calendarEl1, {
        plugins: ['list', 'interaction'],
        height: 580,
        defaultView: 'listDay',
        navLinks: true, // can click day/week names to navigate views
        editable: true,
        eventLimit: true, // allow "more" link when too many events
        locale: 'ja',
        events: [{
        }
        ]
    });

    calendar2.render();
});