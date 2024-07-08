$(document).on('click', '.tb_but', function() {
      var sens_id = $(this).data('id');
      var sens_type = $(this).data('tag');
      var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
      $.ajax({
        url: '/favorite_add/',
        method: 'POST',
        data: {'sens_id': sens_id,'sens_type': sens_type, 'csrfmiddlewaretoken': csrfToken},
        success: function(response) {
        },
        error: function(xhr, status, error) {
        }
      });
    });

