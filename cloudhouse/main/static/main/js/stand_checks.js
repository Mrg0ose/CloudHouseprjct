$(document).ready(function() {
  $.ajax({
    url: 'ajaxbd',
    method: 'GET',
    success: function(data) {
      if (data.setting.time_sensors == 1) {
        $('#speed-1').prop('checked', true);
      } else if (data.setting.time_sensors == 2) {
        $('#speed-2').prop('checked', true);
      } else if (data.setting.time_sensors == 3) {
        $('#speed-3').prop('checked', true);
      }
      if (data.setting.device_start_stop == "Неактивно") {
        $('#on-button').prop('disabled', false);
        $('#off-button').prop('disabled', true);
        $('#off-button').addClass('disabled');
        $('#on-button').removeClass('disabled');
      } else if (data.setting.device_start_stop == "Активно") {
      $('#off-button').prop('disabled', false);
        $('#on-button').prop('disabled', true);
        $('#on-button').addClass('disabled');
        $('#off-button').removeClass('disabled');

      }
    },
    error: function(xhr, status, error) {
      console.log('Error:', error);
    }
  });
});





