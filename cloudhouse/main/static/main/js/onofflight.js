$(document).on('click', '.fav_sensor_win_light', function() {
      var sens_id = $(this).data('sensor_id');
      console.log(sens_id);
      var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
      $.ajax({
        url: '/light_onoff/',
        method: 'POST',
        data: {'sens_id': sens_id, 'csrfmiddlewaretoken': csrfToken},
        success: function(data) {

        },
        error: function(xhr, status, error) {
        }
      });
    });