$('.editbtnl').hide();
$('.savebtnl').hide();
$(document).ready(function () {
    let parentRow;
    let sensorId;
    var csrf3Token = $('input[name="csrfmiddlewaretoken"]').val();
  $('.light-checkbox').change(function () {
    const selectedCheckboxes = $('.light-checkbox:checked');

    if (selectedCheckboxes.length === 1) {
      $('.editbtnl').show();
    } else {
      $('.editbtnl').hide();
    }
  });


  $('.editbtnl').click(function () {
    $('.editbtnl').hide();
    $('.light-checkbox').hide();
    $('.light-allchecks').hide();
    $('.deletebtnl').hide();
    $('.addbtnl').hide();
    const selectedCheckbox = $('.light-checkbox:checked').first();
    parentRow = selectedCheckbox.closest('tr');
    const description = parentRow.find('td:nth-child(4)').text();
    sensorId = parentRow.data('id');
    parentRow.find('td:nth-child(4)').html(`<input type="text" class="edit-description" placeholder="${description}" value="${description}">`);
    $('.savebtnl').show();
  });


  $(document).on('click', '.savebtnl', function () {
    $('.savebtnl').hide();

    const descriptionInput = parentRow.find('.edit-description');

    const description = descriptionInput.val() || descriptionInput.attr('placeholder');

$.ajax({
  method: 'POST',
  url: '/updatelight/',
  data: {
    'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
    'id': sensorId,
    'description': description,
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


$('.savebtnl').hide();
});
});
