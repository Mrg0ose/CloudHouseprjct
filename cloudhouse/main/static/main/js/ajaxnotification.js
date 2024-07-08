function showNotifications(notifications) {
  var notificationWindow = $('.notinfo');

  // очищаем окно уведомлений перед отображением новых уведомлений
  notificationWindow.empty();

  // перебираем массив уведомлений и добавляем их в окно уведомлений
  notifications.forEach(function(notification) {
    var message = notification.notification_description;
    var type = notification.notification_type;

    // создаем элемент для отображения уведомления
    var notificationElement = $('<div class="notification">');

    // добавляем класс в зависимости от типа уведомления
    if (type === 'Тревога') {
      notificationElement.addClass('notification_window_warning');
    } else if (type === 'Успешно') {
      notificationElement.addClass('notification_window_except');
    } else {
      notificationElement.addClass('notification_window_stady');
    }

     // добавляем текст уведомления в элемент уведомления
    notificationElement.append('<p>' + message + '</p>');

    // добавляем кнопку удаления уведомления в элемент уведомления
    var deleteButton = $(`<button data-id="${notification.notification_id}" class="delete_button-not"><img src="/static/main/img/delete.png" class="img_del_not" alt=""></button>`);
    notificationElement.append(deleteButton);

    // добавляем элемент уведомления в окно уведомлений
    notificationWindow.append(notificationElement);
  });

  // показываем окно уведомлений, если есть уведомления
  if (notifications.length > 0) {
    $('.notinfo').show();
    $('.notno').hide();
  } else {
    $('.notinfo').hide();
    $('.notno').show();
  }
}

function getNotifications() {
  $.ajax({
    url: 'ajaxbd',
    method: 'GET',
    dataType: 'json',
    success: function(data) {
      showNotifications(data.notification);
    },
    error: function(error) {
      console.log(error);
    }
  });
}

$(document).ready(function() {

  getNotifications();


  setInterval(function() {
    getNotifications();
  },2000);
});