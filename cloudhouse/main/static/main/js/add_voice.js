$(document).ready(function () {
  $('.addingv').hide();
var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

  $('.addbtnv').click(function () {
    $('.addbtnv').hide();
    $('.addingv').show();
  });

  $('.saveaddbtnv').click(function () {
    const deviceCodevoice = $('.device-code-select-voice').val();
    const sensorName = $('.add-description-voice:eq(0)').val();
    const ip = $('.add-description-voice:eq(1)').val();
    const mesto = $('.add-description-voice:eq(2)').val();
    const minThreshold = $('.add-description-voice:eq(3)').val();
    const maxThreshold = $('.add-description-voice:eq(4)').val();


    $.ajax({
      method: 'POST',
      url: '/addvoice/',
      data: {
        'csrfmiddlewaretoken': csrfToken,
        'deviceCodevoice': deviceCodevoice,
        'sensorName': sensorName,
        'ip':ip,
        'location': mesto,
        'minThreshold': minThreshold,
        'maxThreshold': maxThreshold
      },
      success: function (response) {

      if (response.status === 'success') {
            console.log('Датчик успешно создан!');
        location.reload()

        $('#messsuc').show();
      $('#messsuc').text(`Датчик добавлен успешно`);
      setTimeout(function() {
        $('#messsuc').hide();
      }, 3000);
        } else if (response.status === 'error') {
        $('#messdang').show();
            $('#messdang').text(response.message);
             setTimeout(function() {
        $('#messdang').hide();
      }, 3000);
        }

      },
      error: function (error) {
        console.log('Ошибка при создании датчика!');
        location.reload()
        $('#messdang').show();
      $('#messdang').text(`Ошибка при добавлении датчика...`);
      setTimeout(function() {
        $('#messdang').hide();
      }, 3000);
      }
    });
  });
});
