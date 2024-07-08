$(document).ready(function() {
  $("#win_table").show();
  $("#win_form_contract").hide();

  $(".create_contract").click(function() {
    $("#win_table").hide();
    $("#win_form_contract").show();
  });

  $(".form_contract_akk").click(function(e) {
    e.preventDefault();

    var lastName = $("#last-name").val();
    var firstName = $("#first-name").val();
    var middleName = $("#middle-name").val();
    var phone = $("#phone").val();
    var address = $("#address").val();
    var email = $("#email").val();
    var login = $("#login").val();
    var password = $("#password").val();
    var deviceName = $("#name_dev").val();
    var ipAddress = $("#ip_adress").val();

    if (
      lastName === "" ||
      firstName === "" ||
      phone === "" ||
      address === "" ||
      email === "" ||
      login === "" ||
      password === "" ||
      deviceName === "" ||
      ipAddress === ""
    ) {
      $('#dangcreate').show();
      $('#dangcreate').text(`Заполните все обязательные поля *`);
      setTimeout(function() {
        $('#dangcreate').hide();
      }, 3000);
      return;
    }

    $.ajax({
      method: 'POST',
      url: '/createcontract/',
      data: {
        'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
        'lastName': lastName,
        'firstName': firstName,
        'middleName': middleName,
        'phone': phone,
        'address': address,
        'email': email,
        'login': login,
        'password': password,
        'deviceName': deviceName,
        'ipAddress': ipAddress
      },
      success: function(response) {
        if (response.status === 'success') {
          console.log('Договор создан');
          $('#messsuc').show();
          $('#messsuc').text(`Договор и аккаунт создан и был внесен в базу`);
          setTimeout(function() {
            $('#messsuc').hide();
          }, 3000);
          location.reload();
        } else if (response.status === 'error') {
          $('#dangcreate').show();
          $('#dangcreate').text(response.message);
          setTimeout(function() {
            $('#dangcreate').hide();
          }, 3000);
        }
      },
      error: function(error) {
        console.log('Ошибка при формировании договора');
        location.reload();
        $('#messdang').show();
        $('#messdang').text(`Ошибка при формировании договора`);
        setTimeout(function() {
          $('#messdang').hide();
        }, 3000);
      }
    });
  });

  $("#back_win").click(function() {
    $("#win_table").show();
    $("#win_form_contract").hide();
  });
});
