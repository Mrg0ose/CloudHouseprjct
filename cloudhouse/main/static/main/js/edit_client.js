$('.editbtncl').hide();
$('.savebtncl').hide();
$(document).ready(function () {
    let parentRow;
    let ClientId;
    var csrf1Token = $('input[name="csrfmiddlewaretoken"]').val();
  $('.client-checkbox').change(function () {
    const selectedCheckboxes = $('.client-checkbox:checked');

    if (selectedCheckboxes.length === 1) {
      $('.editbtncl').show();
    } else {
      $('.editbtncl').hide();
    }
  });



  $('.editbtncl').click(function () {
    $('.editbtncl').hide();
    $('.client-checkbox').hide();
    $('.temp-allchecks').hide();
    $('.deletebtnt').hide();
    $('.addbtnt').hide();
    const selectedCheckbox = $('.client-checkbox:checked').first();
    parentRow = selectedCheckbox.closest('tr');
    const surname = parentRow.find('td:nth-child(2)').text();
    const name = parentRow.find('td:nth-child(3)').text();
    const patronymic = parentRow.find('td:nth-child(4)').text();
    const mobile = parentRow.find('td:nth-child(7)').text();
    const email = parentRow.find('td:nth-child(8)').text();
    ClientId = parentRow.data('id');
    parentRow.find('td:nth-child(2)').html(`<input type="text" class="edit-surname" placeholder="${surname}" value="${surname}">`);
    parentRow.find('td:nth-child(3)').html(`<input type="text" class="edit-name" placeholder="${name}" value="${name}">`);
    parentRow.find('td:nth-child(4)').html(`<input type="text" class="edit-patronymic" placeholder="${patronymic}" value="${patronymic}">`);
    parentRow.find('td:nth-child(7)').html(`<input type="number" class="edit-mobile" placeholder="${mobile}" value="${mobile}">`);
    parentRow.find('td:nth-child(8)').html(`<input type="email" class="edit-email" placeholder="${email}" value="${email}">`);

    $('.savebtncl').show();
  });


  $(document).on('click', '.savebtncl', function () {
    $('.savebtncl').hide();

    const nameInput = parentRow.find('.edit-name');
    const surnameInput = parentRow.find('.edit-surname');
    const patronymicInput = parentRow.find('.edit-patronymic');
    const mobileInput = parentRow.find('.edit-mobile');
    const emailInput = parentRow.find('.edit-email');

    const name = nameInput.val() || nameInput.attr('placeholder');
    const surname = surnameInput.val() || surnameInput.attr('placeholder');
    const patronymic = patronymicInput.val() || patronymicInput.attr('placeholder');
    const mobile = mobileInput.val() || mobileInput.attr('placeholder');
    const email = emailInput.val() || emailInput.attr('placeholder');



$.ajax({
  method: 'POST',
  url: '/updateclient/',
  data: {
    'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
    'id': ClientId,
    'name': name,
    'surname': surname,
    'patronymic': patronymic,
    'mobile': mobile,
    'email': email
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


parentRow.find('td:nth-child(2)').text(surname);
parentRow.find('td:nth-child(3)').text(name);
parentRow.find('td:nth-child(4)').text(patronymic);
parentRow.find('td:nth-child(7)').text(mobile);
parentRow.find('td:nth-child(8)').text(email);


$('.savebtncl').hide();
});
});
