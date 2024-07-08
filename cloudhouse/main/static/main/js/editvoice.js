$('.editbtnv').hide();
$('.savebtnv').hide();
$(document).ready(function () {
    let parentRow;
    let sensorId;
    var csrf4Token = $('input[name="csrfmiddlewaretoken"]').val();
  $('.voice-checkbox').change(function () {
    const selectedCheckboxes = $('.voice-checkbox:checked');

    if (selectedCheckboxes.length === 1) {
      $('.editbtnv').show();
    } else {
      $('.editbtnv').hide();
    }
  });


  $('.editbtnv').click(function () {
    $('.editbtnv').hide();
    $('.voice-checkbox').hide();
    $('.voice-allchecks').hide();
    $('.deletebtnv').hide();
    $('.addbtnv').hide();
    const selectedCheckbox = $('.voice-checkbox:checked').first();
    parentRow = selectedCheckbox.closest('tr');
    const description = parentRow.find('td:nth-child(4)').text();
    const minVoice = parentRow.find('td:nth-child(9)').text();
    const maxVoice = parentRow.find('td:nth-child(10)').text();
    sensorId = parentRow.data('id');
    parentRow.find('td:nth-child(4)').html(`<input type="text" class="edit-description" placeholder="${description}" value="${description}">`);
    parentRow.find('td:nth-child(9)').html(`<input type="text" class="edit-min-voice" placeholder="${minVoice}" value="${minVoice}">`);
    parentRow.find('td:nth-child(10)').html(`<input type="text" class="edit-max-voice" placeholder="${maxVoice}" value="${maxVoice}">`);

    $('.savebtnv').show();
  });


  $(document).on('click', '.savebtnv', function () {
    $('.savebtnv').hide();

    const descriptionInput = parentRow.find('.edit-description');
    const minVoiceInput = parentRow.find('.edit-min-voice');
    const maxVoiceInput = parentRow.find('.edit-max-voice');

    const description = descriptionInput.val() || descriptionInput.attr('placeholder');
    const minVoice = minVoiceInput.val() || minVoiceInput.attr('placeholder');
    const maxVoice = maxVoiceInput.val() || maxVoiceInput.attr('placeholder');

$.ajax({
  method: 'POST',
  url: '/updatevoice/',
  data: {
    'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
    'id': sensorId,
    'description': description,
    'minVoice': minVoice,
    'maxVoice': maxVoice
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
parentRow.find('td:nth-child(9)').text(minVoice);
parentRow.find('td:nth-child(10)').text(maxVoice);


$('.savebtnv').hide();
});
});
