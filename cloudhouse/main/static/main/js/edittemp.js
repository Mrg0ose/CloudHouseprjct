$('.editbtnt').hide();
$('.savebtnt').hide();
$(document).ready(function () {
    let parentRow;
    let sensorId;
    var csrf1Token = $('input[name="csrfmiddlewaretoken"]').val();
  $('.temp-checkbox').change(function () {
    const selectedCheckboxes = $('.temp-checkbox:checked');

    if (selectedCheckboxes.length === 1) {
      $('.editbtnt').show();
    } else {
      $('.editbtnt').hide();
    }
  });


  $('.editbtnt').click(function () {
    $('.editbtnt').hide();
    $('.temp-checkbox').hide();
    $('.temp-allchecks').hide();
    $('.deletebtnt').hide();
    $('.addbtnt').hide();
    const selectedCheckbox = $('.temp-checkbox:checked').first();
    parentRow = selectedCheckbox.closest('tr');
    const description = parentRow.find('td:nth-child(4)').text();
    const minTemperature = parentRow.find('td:nth-child(9)').text();
    const maxTemperature = parentRow.find('td:nth-child(10)').text();
    sensorId = parentRow.data('id');
    parentRow.find('td:nth-child(4)').html(`<input type="text" class="edit-description" placeholder="${description}" value="${description}">`);
    parentRow.find('td:nth-child(9)').html(`<input type="text" class="edit-min-temperature" placeholder="${minTemperature}" value="${minTemperature}">`);
    parentRow.find('td:nth-child(10)').html(`<input type="text" class="edit-max-temperature" placeholder="${maxTemperature}" value="${maxTemperature}">`);

    $('.savebtnt').show();
  });


  $(document).on('click', '.savebtnt', function () {
    $('.savebtnt').hide();

    const descriptionInput = parentRow.find('.edit-description');
    const minTemperatureInput = parentRow.find('.edit-min-temperature');
    const maxTemperatureInput = parentRow.find('.edit-max-temperature');

    const description = descriptionInput.val() || descriptionInput.attr('placeholder');
    const minTemperature = minTemperatureInput.val() || minTemperatureInput.attr('placeholder');
    const maxTemperature = maxTemperatureInput.val() || maxTemperatureInput.attr('placeholder');

$.ajax({
  method: 'POST',
  url: '/updatetemp/',
  data: {
    'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
    'id': sensorId,
    'description': description,
    'minTemperature': minTemperature,
    'maxTemperature': maxTemperature
  },
  success: function (response) {
    $('#messsuc').show();
      $('#messsuc').text(`Данные обновлены успешно!`);
      location.reload();
      setTimeout(function() {
        $('#messsuc').hide();
      }, 3000);
  },
  error: function (error) {
    $('#messdang').show();
      $('#messdang').text(`Ошибка обновления данных...`);
      //location.reload();
      setTimeout(function() {
        $('#messdang').hide();
      }, 3000);
  }
});


parentRow.find('td:nth-child(4)').text(description);
parentRow.find('td:nth-child(9)').text(minTemperature);
parentRow.find('td:nth-child(10)').text(maxTemperature);


$('.savebtnt').hide();
});
});
