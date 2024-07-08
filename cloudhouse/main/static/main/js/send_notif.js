  function sendnotif() {
  var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
  $.ajax({
    url: '/notification_send/',
    method: 'POST',
    data: {'csrfmiddlewaretoken': csrfToken},
    success: function(response) {
    },
    error: function(xhr, status, error) {
    }
  });
  }

  $(document).ready(function() {
  sendnotif();

  setInterval(function() {
    sendnotif();
  },10000);
});