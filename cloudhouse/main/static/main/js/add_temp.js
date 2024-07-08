$(document).ready(function () {
  $('.addingt').hide();
var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

  $('.addbtnt').click(function () {
    $('.addbtnt').hide();
    $('.addingt').show();
  });

  $('.saveaddbtnt').click(function () {
    const deviceCodetemp = $('.device-code-select-temp').val();
    const sensorName = $('.add-description-temp:eq(0)').val();
    const ip = $('.add-description-temp:eq(1)').val();
    const mesto = $('.add-description-temp:eq(2)').val();
    const minThreshold = $('.add-description-temp:eq(3)').val();
    const maxThreshold = $('.add-description-temp:eq(4)').val();


    $.ajax({
      method: 'POST',
      url: '/addtemp/',
      data: {
        'csrfmiddlewaretoken': csrfToken,
        'deviceCodetemp': deviceCodetemp,
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
