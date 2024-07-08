const lightCheckboxes = document.querySelectorAll('.light-checkbox');
const lightAllCheck = document.querySelector('.light-allchecks');
const deleteLightBtn = document.querySelector('.deletebtnl');

deleteLightBtn.style.display = 'none';

lightAllCheck.addEventListener('change', function () {
  const isChecked = lightAllCheck.checked;

  lightCheckboxes.forEach(function (checkbox) {
    checkbox.checked = isChecked;
  });

  toggleDeleteBtn();
});

lightCheckboxes.forEach(function (checkbox) {
  checkbox.addEventListener('change', function () {
    toggleDeleteBtn();
  });
});

function toggleDeleteBtn() {
  const anyChecked = Array.from(lightCheckboxes).some(function (checkbox) {
    return checkbox.checked;
  });

  if (anyChecked) {
    deleteLightBtn.style.display = 'block';
  } else {
    deleteLightBtn.style.display = 'none';
  }
}

deleteLightBtn.addEventListener('click', function () {
  const checkedRows = Array.from(lightCheckboxes).filter(function (checkbox) {
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
      url: '/delete_light/',
      type: 'POST',
      data: {
        'ids': ids,
        'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
      },
      success: function (data) {
        // Обновить страницу после успешного удаления записей
        location.reload();
      }
    });
  } else {
    alert('Выберите записи для удаления.');
  }
});
