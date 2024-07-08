$(document).on('click', '.clear_not', function() {
  var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
  $.ajax({
    url: '/clear_notification_all/',
    method: 'POST',
    data: {'csrfmiddlewaretoken': csrfToken},
    success: function(response) {
    },
    error: function(xhr, status, error) {
      console.error(error);
    }
  });
});