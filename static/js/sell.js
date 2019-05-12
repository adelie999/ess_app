$(document).ready(function () {
    $.ajax({
        url: location.href + '/chart',
        type: 'GET',
        dataType: 'json',
        contentType: "application/json"
    }).done(function (result) {
        result = JSON.parse(result);
        var sells_data = get_sells_data(result);
        var ctx = document.getElementById("myChart").getContext('2d');
        myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: sells_data[0],
                datasets: [{
                    label: '売上（円）',
                    data: sells_data[1],
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)'
                    ],
                    borderColor: [
                        'rgba(255,99,132,1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });
    });

    function get_sells_data(result) {
        var data = [];
        var label = [];
        var sell = [];
        for (var i in result) {
            label.push(result[i].fields.year_month),
            sell.push(result[i].fields.sell)
        }
        data.push(label, sell)
        return data
    }
})