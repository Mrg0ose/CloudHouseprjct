const energyCheckboxes = document.querySelectorAll('.energy-checkbox');
const energyAllCheck = document.querySelector('.energy-allchecks');

const deleteEnergyBtn = document.querySelector('.deletebtne');
deleteEnergyBtn.style.display = 'none';

energyAllCheck.addEventListener('change', function () {
  const isChecked = energyAllCheck.checked;

  energyCheckboxes.forEach(function (checkbox) {
    checkbox.checked = isChecked;
  });

  toggleDeleteEnergyBtn();
});

energyCheckboxes.forEach(function (checkbox) {
  checkbox.addEventListener('change', function () {
    toggleDeleteEnergyBtn();
  });
});

function toggleDeleteEnergyBtn() {
  const anyChecked = Array.from(energyCheckboxes).some(function (checkbox) {
    return checkbox.checked;
  });

  if (anyChecked) {
    deleteEnergyBtn.style.display = 'block';
  } else {
    deleteEnergyBtn.style.display = 'none';
  }
}

deleteEnergyBtn.addEventListener('click', function () {
  const checkedRows = Array.from(energyCheckboxes).filter(function (checkbox) {
    return checkbox.checked;
  }).map(function (checkbox) {
    return checkbox.parentNode.parentNode;
  });

  checkedRows.forEach(function (row) {
    row.parentNode.removeChild(row);
  });

  const ids = checkedRows.map(function (row) {
    return row.dataset.id;
  });

  if (ids.length > 0) {
    $.ajax({
      url: '/delete_energy/',
      type: 'POST',
      data: {
        'ids': ids,
        'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
      },
      success: function (data) {
        location.reload();
      }
    });
  } else {
    alert('Выберите записи для удаления.');
  }
});
