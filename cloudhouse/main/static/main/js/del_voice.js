const voiceCheckboxes = document.querySelectorAll('.voice-checkbox');
const voiceAllCheck = document.querySelector('.voice-allchecks');

const deleteVoiceBtn = document.querySelector('.deletebtnv');
deleteVoiceBtn.style.display = 'none';

voiceAllCheck.addEventListener('change', function () {
  const isChecked = voiceAllCheck.checked;

  voiceCheckboxes.forEach(function (checkbox) {
    checkbox.checked = isChecked;
  });

  toggleDeleteVoiceBtn();
});

voiceCheckboxes.forEach(function (checkbox) {
  checkbox.addEventListener('change', function () {
    toggleDeleteVoiceBtn();
  });
});

function toggleDeleteVoiceBtn() {
  const anyChecked = Array.from(voiceCheckboxes).some(function (checkbox) {
    return checkbox.checked;
  });

  if (anyChecked) {
    deleteVoiceBtn.style.display = 'block';
  } else {
    deleteVoiceBtn.style.display = 'none';
  }
}

deleteVoiceBtn.addEventListener('click', function () {
  const checkedRows = Array.from(voiceCheckboxes).filter(function (checkbox) {
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
      url: '/delete_voice/',
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
