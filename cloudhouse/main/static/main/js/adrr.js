$('.editaddr').hide();
$('.savebtnadr').hide();
$(document).ready(function () {
    let parentRow;
    let addrid;
    var csrf1Token = $('input[address="csrfmiddlewaretoken"]').val();
  $('.address-checkbox').change(function () {
    const selectedCheckboxes = $('.address-checkbox:checked');

    if (selectedCheckboxes.length === 1) {
      $('.editaddr').show();
    } else {
      $('.editaddr').hide();
    }
  });





  $('.editaddr').click(function () {
    $('.editaddr').hide();
    $('.address-checkbox').hide();
    const selectedCheckbox = $('.address-checkbox:checked').first();
    parentRow = selectedCheckbox.closest('tr');
    const address = parentRow.find('td:nth-child(5)').text();
    addrid = parentRow.data('id');
    parentRow.find('td:nth-child(5)').html(`<input type="text" class="edit-address" placeholder="${address}" value="${address}">`);
    $('.savebtnadr').show();
  });


  $(document).on('click', '.savebtnadr', function () {
    $('.savebtnadr').hide();

    const addressInput = parentRow.find('.edit-address');

    const address = addressInput.val() || addressInput.attr('placeholder');



$.ajax({
  method: 'POST',
  url: '/editaddr/',
  data: {
    'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
    'id': addrid,
    'address': address,
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
      $('#messdang').text(error.responseJSON.status);
      location.reload();
      setTimeout(function() {
        $('#messdang').hide();
      }, 3000);
  }
});


parentRow.find('td:nth-child(5)').text(address);



$('.savebtnadr').hide();
});
});
