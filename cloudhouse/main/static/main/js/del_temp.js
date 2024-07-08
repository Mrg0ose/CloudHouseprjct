const tempCheckboxes = document.querySelectorAll('.temp-checkbox');
const tempAllCheck = document.querySelector('.temp-allchecks');

const deleteTempBtn = document.querySelector('.deletebtnt');
deleteTempBtn.style.display = 'none';

tempAllCheck.addEventListener('change', function () {
const isChecked = tempAllCheck.checked;

tempCheckboxes.forEach(function (checkbox) {
checkbox.checked = isChecked;
});

toggleDeleteTempBtn();
});

tempCheckboxes.forEach(function (checkbox) {
checkbox.addEventListener('change', function () {
toggleDeleteTempBtn();
});
});

function toggleDeleteTempBtn() {
const anyChecked = Array.from(tempCheckboxes).some(function (checkbox) {
return checkbox.checked;
});

if (anyChecked) {
deleteTempBtn.style.display = 'block';
} else {
deleteTempBtn.style.display = 'none';
}
}

deleteTempBtn.addEventListener('click', function () {
const checkedRows = Array.from(tempCheckboxes).filter(function (checkbox) {
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
url: '/delete_temp/',
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