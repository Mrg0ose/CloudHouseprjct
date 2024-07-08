const conCheckboxes = document.querySelectorAll('.contract-checkbox');
const crConBtn = document.querySelector('.create_contract');
const deleteConBtn = document.querySelector('.delete_contr');
const loConBtn = document.querySelector('.load_contr');
const morConBtn = document.querySelector('.create_more_contract');

deleteConBtn.style.display = 'none';
loConBtn.style.display = 'none';
morConBtn.style.display = 'none';


conCheckboxes.forEach(function (checkbox) {
  checkbox.addEventListener('change', function () {
    conCheckboxes.forEach(function (otherCheckbox) {
      if (otherCheckbox !== checkbox) {
        otherCheckbox.checked = false;
      }
    });


    toggledeleteConBtn();
  });
});


function toggledeleteConBtn() {
  const checkedCheckbox = Array.from(conCheckboxes).find(function (checkbox) {
    return checkbox.checked;
  });

  if (checkedCheckbox) {
    loConBtn.style.display = '';
    deleteConBtn.style.display = '';
    morConBtn.style.display = '';
    crConBtn.style.display = 'none';
  } else {
    deleteConBtn.style.display = 'none';
    crConBtn.style.display = '';
    morConBtn.style.display = 'none';
    loConBtn.style.display ='none';
  }
}

deleteConBtn.addEventListener('click', function () {
  const checkedCheckbox = Array.from(conCheckboxes).find(function (checkbox) {
    return checkbox.checked;
  });

  if (checkedCheckbox) {
    if (confirm('Вы уверены, что хотите архивировать выбранный договор?')) {
      const contractId = checkedCheckbox.parentNode.parentNode.dataset.id;

      $.ajax({
        url: '/arch_admin_contract/',
        type: 'POST',
        data: {
          'contractId': contractId,
          'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function (data) {
          location.reload();
        },
        error: function(error) {
          console.log('Ошибка при архивации договора');
          $('#messdang').show();
          $('#messdang').text('Ошибка при архивации договора');
          setTimeout(function() {
            $('#messdang').hide();
          }, 3000);
        }
      });
    }
  } else {
    alert('Выберите запись для архивации.');
  }
});
