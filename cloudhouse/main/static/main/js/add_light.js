$(document).ready(function () {
  $('.addingl').hide();
var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

  $('.addbtnl').click(function () {
    $('.addbtnl').hide();
    $('.addingl').show();
  });

  $('.saveaddbtnl').click(function () {
    const deviceCodelight = $('.device-code-select-light').val();
    const sensorName = $('.add-description-light:eq(0)').val();
    const ip = $('.add-description-light:eq(1)').val();
    const mesto = $('.add-description-light:eq(2)').val();


    $.ajax({
      method: 'POST',
      url: '/addlight/',
      data: {
        'csrfmiddlewaretoken': csrfToken,
        'deviceCodelight': deviceCodelight,
        'sensorName': sensorName,
        'ip':ip,
        'location': mesto,
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