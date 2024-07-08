const repCheckboxes = document.querySelectorAll('.report-checkbox');
const repAllCheck = document.querySelector('.report-allchecks');

const deleteRepBtn = document.querySelector('.deletebtnr');
deleteRepBtn.style.display = 'none';

repAllCheck.addEventListener('change', function () {
const isChecked = repAllCheck.checked;

repCheckboxes.forEach(function (checkbox) {
checkbox.checked = isChecked;
});

toggledeleteRepBtn();
});

repCheckboxes.forEach(function (checkbox) {
checkbox.addEventListener('change', function () {
toggledeleteRepBtn();
});
});

function toggledeleteRepBtn() {
const anyChecked = Array.from(repCheckboxes).some(function (checkbox) {
return checkbox.checked;
});

if (anyChecked) {
deleteRepBtn.style.display = 'block';
} else {
deleteRepBtn.style.display = 'none';
}
}

deleteRepBtn.addEventListener('click', function () {
const checkedRows = Array.from(repCheckboxes).filter(function (checkbox) {
return checkbox.checked;
}).map(function (checkbox) {
return checkbox.parentNode.parentNode;
});

checkedRows.forEach(function (row) {
row.parentNode.removeChild(row);
});

const idsr = checkedRows.map(function (row) {
return row.dataset.id;
});
if (idsr.length > 0) {
$.ajax({
url: '/delete_report/',
type: 'POST',
data: {
'idsr': idsr,
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