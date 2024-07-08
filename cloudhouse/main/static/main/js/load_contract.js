const conCheckboxess = document.querySelectorAll('.contract-checkbox');

const loConBtnn = document.querySelector('.load_contr');



loConBtnn.addEventListener('click', function () {
  const checkedCheckbox = Array.from(conCheckboxess).find(function (checkbox) {
    return checkbox.checked;
  });

  if (checkedCheckbox) {
    if (confirm('Выгрузить выбранный договор?')) {
      const contractId = checkedCheckbox.parentNode.parentNode.dataset.id;
        console.log(contractId)
      $.ajax({
        url: '/loadcontract/',
        type: 'POST',
        data: {
          'contractId': contractId,
          'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function (data) {
          $('#messsuc').show();
        $('#messsuc').text(`Договор был выгружен успешно`);
        var newWindow = window.open('', '_blank', 'height=600,width=800');
        newWindow.document.write(data);
        newWindow.document.close();
        newWindow.focus();
        setTimeout(function() {
          $('#messsuc').hide();
        }, 3000);

        },
        error: function(error) {
          console.log('Ошибка при выгрузке договора');
          $('#messdang').show();
          $('#messdang').text('Ошибка при выгрузке договора');
          setTimeout(function() {
            $('#messdang').hide();
          }, 3000);
        }
      });
    }
  } else {
    alert('Выберите договор для выгрузки.');
  }
});
