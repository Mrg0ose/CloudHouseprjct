$(document).on('click', '#on-button', function() {
  var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
  $.ajax({
    url: '/button_on/',
    method: 'POST',
    data: {'csrfmiddlewaretoken': csrfToken},
    success: function(response) {
    console.log('button_on request success', response);
    $('#off-button').prop('disabled', false);
    $('#on-button').prop('disabled', true);
    $('#on-button').addClass('disabled');
    $('#off-button').removeClass('disabled');
    },
    error: function(xhr, status, error) {
      console.error('button_on request error', error);
    }
  });
});
