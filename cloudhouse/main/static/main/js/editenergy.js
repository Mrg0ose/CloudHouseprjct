$('.editbtne').hide();
$('.savebtne').hide();
$(document).ready(function () {
    let parentRow;
    let sensorId;
    var csrf2Token = $('input[name="csrfmiddlewaretoken"]').val();
  $('.energy-checkbox').change(function () {
    const selectedCheckboxes = $('.energy-checkbox:checked');

    if (selectedCheckboxes.length === 1) {
      $('.editbtne').show();
    } else {
      $('.editbtne').hide();
    }
  });


  $('.editbtne').click(function () {
    $('.editbtne').hide();
    $('.energy-checkbox').hide();
    $('.energy-allchecks').hide();
    $('.deletebtne').hide();
    $('.addbtne').hide();
    const selectedCheckbox = $('.energy-checkbox:checked').first();
    parentRow = selectedCheckbox.closest('tr');
    const description = parentRow.find('td:nth-child(4)').text();
    const minVoltage = parentRow.find('td:nth-child(10)').text();
    const maxVoltage = parentRow.find('td:nth-child(11)').text();
    const minEnergy = parentRow.find('td:nth-child(12)').text();
    const maxEnergy = parentRow.find('td:nth-child(13)').text();
    sensorId = parentRow.data('id');
    parentRow.find('td:nth-child(4)').html(`<input type="text" class="edit-description" placeholder="${description}" value="${description}">`);
    parentRow.find('td:nth-child(10)').html(`<input type="text" class="edit-min-voltage" placeholder="${minVoltage}" value="${minVoltage}">`);
    parentRow.find('td:nth-child(11)').html(`<input type="text" class="edit-max-voltage" placeholder="${maxVoltage}" value="${maxVoltage}">`);
    parentRow.find('td:nth-child(12)').html(`<input type="text" class="edit-min-energy" placeholder="${minEnergy}" value="${minEnergy}">`);
    parentRow.find('td:nth-child(13)').html(`<input type="text" class="edit-max-energy" placeholder="${maxEnergy}" value="${maxEnergy}">`);

    $('.savebtne').show();
  });


  $(document).on('click', '.savebtne', function () {
    $('.savebtne').hide();

    const descriptionInput = parentRow.find('.edit-description');
    const minEnergyInput = parentRow.find('.edit-min-energy');
    const maxEnergyInput = parentRow.find('.edit-max-energy');
    const minVoltageInput = parentRow.find('.edit-min-voltage');
    const maxVoltageInput = parentRow.find('.edit-max-voltage');

    const description = descriptionInput.val() || descriptionInput.attr('placeholder');
    const minEnergy = minEnergyInput.val() || minEnergyInput.attr('placeholder');
    const maxEnergy = maxEnergyInput.val() || maxEnergyInput.attr('placeholder');
    const minVoltage = minVoltageInput.val() || minVoltageInput.attr('placeholder');
    const maxVoltage = maxVoltageInput.val() || maxVoltageInput.attr('placeholder');

$.ajax({
  method: 'POST',
  url: '/updateenergy/',
  data: {
    'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
    'id': sensorId,
    'description': description,
    'minEnergy': minEnergy,
    'maxEnergy': maxEnergy,
    'minVoltage': minVoltage,
    'maxVoltage': maxVoltage
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
      location.reload();
      setTimeout(function() {
        $('#messdang').hide();
      }, 3000);
  }
});


parentRow.find('td:nth-child(4)').text(description);
parentRow.find('td:nth-child(10)').text(minVoltage);
parentRow.find('td:nth-child(11)').text(maxVoltage);
parentRow.find('td:nth-child(12)').text(minEnergy);
parentRow.find('td:nth-child(13)').text(maxEnergy);


$('.savebtne').hide();
});
});
