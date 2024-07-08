$(document).ready(function() {
  $("#win_table").show();
  $("#win_form_contractt").hide();

  var selectedContractId = null; // Переменная для хранения ID выбранного чекбокса

  $(".create_more_contract").click(function() {
    $("#win_table").hide();
    $("#win_form_contractt").show();
  });

  const conadd = document.querySelectorAll('.contract-checkbox');

  conadd.forEach(function(checkbox) {
    checkbox.addEventListener('click', function() {
      if (this.checked) {
        selectedContractId = this.parentNode.parentNode.dataset.id;
      }
    });
  });

  $(".form_contract_akkk").click(function(e) {
    e.preventDefault();

    var address = $("#addresss").val();
    var deviceName = $("#name_devv").val();
    var ipAddress = $("#ip_adresss").val();

    if (
      address === "" ||
      deviceName === "" ||
      ipAddress === "" ||
      selectedContractId === null
    ) {
      $('#dangcreatee').show();
      $('#dangcreatee').text(`Заполните все обязательные поля *`);
      setTimeout(function() {
        $('#dangcreatee').hide();
      }, 3000);
      return;
    }

    $.ajax({
      method: 'POST',
      url: '/morecontract/',
      data: {
        'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
        'contractid': selectedContractId,
        'address': address,
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
          $('#dangcreatee').show();
          $('#dangcreatee').text(response.message);
          setTimeout(function() {
            $('#dangcreatee').hide();
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

  $("#back_winn").click(function() {
    $("#win_table").show();
    $("#win_form_contractt").hide();
  });
});
