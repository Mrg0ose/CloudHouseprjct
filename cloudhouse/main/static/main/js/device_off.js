$(document).on('click', '#off-button', function() {
  var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
  $.ajax({
    url: '/button_off/',
    method: 'POST',
    data: {'csrfmiddlewaretoken': csrfToken},
    success: function(response) {
    console.log('button_off request success', response);
    location.reload();
    $('#on-button').prop('disabled', false);
    $('#off-button').prop('disabled', true);
    $('#off-button').addClass('disabled');
    $('#on-button').removeClass('disabled');
    },
    error: function(xhr, status, error) {
      console.error('button_off request error', error);
    }
  });
});