$(document).on('click', '#accept', function() {
  var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
  var speed1 = $('#speed-1').is(":checked");
  var speed2 = $('#speed-2').is(":checked");
  var speed3 = $('#speed-3').is(":checked");
  $.ajax({
    url: '/accept_settings/',
    method: 'POST',
    data: {'csrfmiddlewaretoken': csrfToken,'spd1': speed1, 'spd2': speed2, 'spd3': speed3},
    success: function(data) {
    if (data.success) {
        console.log('Save success');
        if (data.message) {
          alert(data.message);
        } else {
          location.reload();
        }
      }
    },
    error: function(xhr, status, error) {
    }
  });
});

