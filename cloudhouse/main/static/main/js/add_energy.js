$(document).ready(function () {
  $('.addinge').hide();
var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

  $('.addbtne').click(function () {
    $('.addbtne').hide();
    $('.addinge').show();
  });

  $('.saveaddbtne').click(function () {
    const deviceCodeenergy = $('.device-code-select-energy').val();
    const sensorName = $('.add-description-energy:eq(0)').val();
    const ip = $('.add-description-energy:eq(1)').val();
    const mesto = $('.add-description-energy:eq(2)').val();
    const minThresholdv = $('.add-description-energy:eq(3)').val();
    const maxThresholdv = $('.add-description-energy:eq(4)').val();
    const minThresholde = $('.add-description-energy:eq(5)').val();
    const maxThresholde = $('.add-description-energy:eq(6)').val();



    $.ajax({
      method: 'POST',
      url: '/addenergy/',
      data: {
        'csrfmiddlewaretoken': csrfToken,
        'deviceCodeenergy': deviceCodeenergy,
        'sensorName': sensorName,
        'ip':ip,
        'location': mesto,
        'minThresholde': minThresholde,
        'maxThresholde': maxThresholde,
        'minThresholdv': minThresholdv,
        'maxThresholdv': maxThresholdv
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
