const arCheckboxes = document.querySelectorAll('.contract-arch-checkbox');
const arConBtn = document.querySelector('.contr_arh');

arConBtn.style.display = 'none';
arCheckboxes.forEach(function (checkbox) {
  checkbox.addEventListener('change', function () {
    arCheckboxes.forEach(function (otherCheckbox) {
      if (otherCheckbox !== checkbox) {
        otherCheckbox.checked = false;
      }
    });


    togglearchConBtn();
  });
});


function togglearchConBtn() {
  const checkedCheckboxar = Array.from(arCheckboxes).find(function (checkbox) {
    return checkbox.checked;
  });

  if (checkedCheckboxar) {
    arConBtn.style.display = '';
  } else {
    arConBtn.style.display = 'none';
  }
}

arConBtn.addEventListener('click', function () {
  const checkedCheckboxar = Array.from(arCheckboxes).find(function (checkbox) {
    return checkbox.checked;
  });

  if (checkedCheckboxar) {
    if (confirm('Вы уверены, что хотите вернуть контракт из архива?')) {
      const contractIdar = checkedCheckboxar.parentNode.parentNode.dataset.id;

      $.ajax({
        url: '/unarch_admin_contract/',
        type: 'POST',
        data: {
          'contractId': contractIdar,
          'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function (data) {
          location.reload();
        },
        error: function(error) {
          console.log('Ошибка при разархивации договора');
          $('#messdang').show();
          $('#messdang').text('Ошибка при разархивации договора');
          setTimeout(function() {
            $('#messdang').hide();
          }, 3000);
        }
      });
    }
  } else {
    alert('Выберите запись для разархивации.');
  }
});
