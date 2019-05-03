document.addEventListener('DOMContentLoaded', function () {
    ajax_post()
        .done(function (result) {
            var calendarEl = document.getElementById('calendar');
            var calendarEl_list = document.getElementById('calendar-list');
            var events = events_build(result);
            var calendar = new FullCalendar.Calendar(calendarEl, {
                height: 580,
                plugins: ['dayGrid', 'timeGrid', 'interaction'],
                header: {
                    left: 'prev,next today',
                    center: 'title',
                    right: 'dayGridMonth'
                },
                navLinks: true,
                editable: true,
                eventLimit: true,
                selectable: true,
                locale: 'ja',
                events: events,
                dateClick: function (info) {
                    $(selectDay).val(info.dateStr)
                    $(ModalCenter2).modal();
                },
                eventClick: function (info) {
                    $(delete_id).val(info.event.id);
                    $(ModalTitle1).html(info.event.title);
                    $(ModalBodyStart).html(date_format2(info.event.start));
                    $(ModalBodyEnd).html(date_format2(info.event.end));
                    $(ModalBodyDescription).html(info.event.extendedProps.description);
                    $(ModalCenter1).modal();
                }
            });

            var calendar_list = new FullCalendar.Calendar(calendarEl_list, {
                plugins: ['list', 'interaction'],
                height: 580,
                defaultView: 'listDay',
                navLinks: true,
                editable: true,
                eventLimit: true,
                locale: 'ja',
                events: events
            });

            calendar.render();
            calendar_list.render();
        });

    // 予定登録
    $('#register').click(function () {
        var fm = document.getElementById("register_form");
        fm.registerTitle.val = $(registerTitle).val();
        fm.registerDescription.val = $(registerDescription).val();
        fm.select_day,val = $(selectDay).val();
        fm.method = "post";
        fm.target = "_self";
        fm.action = "ajax/schedule/register";
        fm.submit();
    });

    // 予定削除 
    $('#delete').click(function () {
        var fm = document.getElementById("delete_form");
        fm.delete_id.value = $(delete_id).val();
        fm.method = "post";
        fm.target = "_self";
        fm.action = "ajax/schedule/delete";
        fm.submit();
    });
});


// イベント設定
function events_build(data) {
    var parse_data = JSON.parse(data);
    var events = [];
    for (var i in parse_data) {
        events.push({
            id: parse_data[i].pk,
            title: parse_data[i].fields.title,
            start: date_format(parse_data[i].fields.start_date),
            end: date_format(parse_data[i].fields.end_date),
            description: parse_data[i].fields.description,
            textColor: "white"
        });
    }
    return events;
}

// 日付フォーマット1
function date_format(date) {
    return date.replace('T', ' ').replace('Z', '');
}

// 日付フォーマット2
function date_format2(date) {
    console.log(date)
    var f_date = new Date(date);
    var y = f_date.getFullYear();
    var m = f_date.getMonth() + 1;
    var d = f_date.getDate();
    var h = f_date.getHours();
    var mm = ('0' + f_date.getMinutes()).slice(-2);
    return y + '/' + m + '/' + d + ' ' + h + ':' + mm;
}

// db参照
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