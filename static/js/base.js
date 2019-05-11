$(document).ready(function () {
    $.ajax({
        url: 'http://127.0.0.1:8000/setting/url',
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
    }).done(function (result) {
        result = JSON.parse(result);
        console.log(result)
        $("#twitter").attr("href", result[0].fields.url)
        $('#line').attr("href", result[1].fields.url)
        $('#facebook').attr("href", result[2].fields.url)
        $('#instagram').attr("href", result[3].fields.url)
    });

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
});