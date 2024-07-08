$(document).on('click', '.delete_button-not', function() {
      var notificationId = $(this).data('id');
      var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
      $.ajax({
        url: '/clear_notification/',
        method: 'POST',
        data: {'notification_id': notificationId, 'csrfmiddlewaretoken': csrfToken},
        success: function(response) {
        },
        error: function(xhr, status, error) {
        }
      });
    });
