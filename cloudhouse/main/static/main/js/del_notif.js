const notCheckboxes = document.querySelectorAll('.not-checkbox');
const notAllCheck = document.querySelector('.not-allchecks');

const deleteNotBtn = document.querySelector('.deletebtnn');
deleteNotBtn.style.display = 'none';

notAllCheck.addEventListener('change', function () {
const isChecked = notAllCheck.checked;

notCheckboxes.forEach(function (checkbox) {
checkbox.checked = isChecked;
});

toggledeleteNotBtn();
});

notCheckboxes.forEach(function (checkbox) {
checkbox.addEventListener('change', function () {

toggledeleteNotBtn();
});
});

function toggledeleteNotBtn() {
const anyChecked = Array.from(notCheckboxes).some(function (checkbox) {
return checkbox.checked;
});

if (anyChecked) {
deleteNotBtn.style.display = 'block';
} else {
deleteNotBtn.style.display = 'none';
}
}


deleteNotBtn.addEventListener('click', function () {
const checkedRows = Array.from(notCheckboxes).filter(function (checkbox) {
return checkbox.checked;
}).map(function (checkbox) {
return checkbox.parentNode.parentNode;
});

checkedRows.forEach(function (row) {
row.parentNode.removeChild(row);
});

const idsn = checkedRows.map(function (row) {
return row.dataset.id;
});
if (idsn.length > 0) {
$.ajax({
url: '/delete_notif/',
type: 'POST',
data: {
'idsn': idsn,
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