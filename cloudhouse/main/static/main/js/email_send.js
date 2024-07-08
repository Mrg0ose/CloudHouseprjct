$(document).on('click', '#payb', function() {
  var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
  $.ajax({
    url: '/pay/',
    method: 'POST',
    data: {'csrfmiddlewaretoken': csrfToken},
    success: function(data) {
        $('#emsu').show();
        $('#emsu').text(`Чек об оплате был отправлен вам на почту`);
setTimeout(function() {
  $('#emsu').hide();
}, 3000);
    },
    error: function(xhr, status, error) {
    $('#emsud').show();
        $('#emsud').text(`Произошла непредвиденная ошибка...`);
      setTimeout(function() {
  $('#emsud').hide();
}, 3000);
    }
  });
});