$(document).on('click', '#accept', function() {
  var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
  var sensname = $('#sensorname').val();
  var minr = $('#min').val();
  var maxr = $('#max').val();

  if (sensname && minr && maxr) {
    if (parseInt(minr) > parseInt(maxr) || parseInt(minr) == parseInt(maxr)) {
      $('#al').show();
      $('#al').text('Ошибка! Минимальное значение не может быть больше или равно максимальному');
      return;
      }
    $.ajax({
      url: '/accept_settings_upd/',
      method: 'POST',
      data: {'csrfmiddlewaretoken': csrfToken, 'sname': sensname, 'rmin': minr, 'rmax': maxr},
      success: function(data) {
        console.log('Save minmax success');
        $('#al').empty();
        $('#al').hide();
        $('#su').show();
        $('#su').text(`Успешно! Min и Max датчика ${sensname} были изменены`);
        $('#sensorname').val('');
        $('#min').val('');
        $('#max').val('');
        setTimeout(function() {
  $('#su').hide();
}, 3000);
      },
      error: function(xhr, status, error) {
        $('#al').show();

        $('#su').empty();
        $('#al').text(error);
      }
    });
  }
});