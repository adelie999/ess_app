document.addEventListener('DOMContentLoaded', function () {

    ajax_post()
    .done(function (result) {
        var calendarEl = document.getElementById('calendar');
        var calendar = new FullCalendar.Calendar(calendarEl, {
            height: 580,
            plugins: ['dayGrid', 'timeGrid', 'interaction'],
            header: {
                left: 'prev,next today',
                center: 'title',
                right: 'dayGridMonth,timeGridWeek,timeGridDay'
            },
            navLinks: true,
            editable: true,
            eventLimit: true,
            selectable: true,
            locale: 'ja',
            events: [{
                title: result.title,
                start: result.start,
                end: result.end
            }],
            dateClick: function (info) {
                alert('Date: ' + info.dateStr);
                alert('Resource ID: ' + info.resource);
            },
            eventClick: function(info) {
                alert(info.event.title)
                console.log(info.event.title)
            }
        });
        calendar.render();
    });
});

// db問い合わせ
function ajax_post() {
    return $.ajax({
        url: 'ajax/schedule',
        type: 'POST',
        dataType: 'json',
        contentType: "application/json",
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
            }
        },
        error: function (xhr, status, error) {
            alert(status + "\n" + "Status: " + xhr.status + "\n" + error);
        }
    });
}

// csrf_token対策1
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// csrf_token対策2
function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}