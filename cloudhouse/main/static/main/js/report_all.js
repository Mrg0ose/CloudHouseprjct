$(document).on('click', '#reportall', function() {
  var start_date = $('#from').val();
  var end_date = $('#to').val();

  if (start_date === '' || end_date === '') {
    $('#emsudr').show();
    $('#emsudr').text('Пожалуйста, выберите даты');
    setTimeout(function() {
      $('#emsudr').hide();
    }, 3000);
    return;
  }

  var start_timestamp = Date.parse(start_date);
  var end_timestamp = Date.parse(end_date);

  if (isNaN(start_timestamp) || isNaN(end_timestamp)) {
    $('#emsudr').show();
    $('#emsudr').text('Пожалуйста, выберите корректные даты');
    setTimeout(function() {
      $('#emsudr').hide();
    }, 3000);
    return;
  }

  var now_timestamp = new Date().getTime();
  if (start_timestamp > now_timestamp || end_timestamp > now_timestamp) {
    $('#emsudr').show();
    $('#emsudr').text('Выберите дату, которая уже наступила');
    setTimeout(function() {
      $('#emsudr').hide();
    }, 3000);
    return;
  }

  if (start_timestamp > end_timestamp) {
    $('#emsudr').show();
    $('#emsudr').text('Начальная дата не может быть больше конечной');
    setTimeout(function() {
      $('#emsudr').hide();
    }, 3000);
    return;
  }

  var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
  $.ajax({
    url: '/report_sens_all/',
    method: 'POST',
    data: {'csrfmiddlewaretoken': csrfToken, 'start_date': start_date, 'end_date': end_date},
    success: function(data) {
        $('#emsur').show();
        $('#emsur').text(`Отчёт был создан успешно`);
        var newWindow = window.open('', '_blank', 'height=600,width=800');
        newWindow.document.write(data);
        newWindow.document.close();
        newWindow.focus();
        setTimeout(function() {
          $('#emsur').hide();
        }, 3000);
    },
    error: function(xhr, status, error) {
      $('#emsudr').show();
      $('#emsudr').text(`Ошибка формирования отчёта...`);
      setTimeout(function() {
        $('#emsudr').hide();
      }, 3000);
    }
  });
});
