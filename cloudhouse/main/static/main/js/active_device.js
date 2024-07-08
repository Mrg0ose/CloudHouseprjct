var interval = 5000;
var intervalId = setInterval(checkConditions, interval);
var currentIntervalId;
function checkConditions() {
  $.ajax({
    url: '/ajaxbd/',
    type: 'GET',
    async: true,
    success: function(data) {
      var timeSetting = data['setting'];
      if (timeSetting.time_sensors == 1 && timeSetting.device_start_stop == 1 && data.contract.device.status == 'Активно') {
        interval = 5000;
        activateFunction = sendRequest1;
      } else if (timeSetting.time_sensors == 2 && timeSetting.device_start_stop == 1 && data.contract.device.status == 'Активно') {
        interval = 10000;
        activateFunction = sendRequest2;
      } else if (timeSetting.time_sensors == 3 && timeSetting.device_start_stop == 1 && data.contract.device.status == 'Активно') {
        interval = 15000;
        activateFunction = sendRequest3;
      } else {
        interval = 10000;
        activateFunction = null;
      }
      clearInterval(intervalId);
      intervalId = setInterval(checkConditions, interval);
      if (activateFunction) {
        activateFunction();
        clearTimeout(currentIntervalId);
        activateFunction();
        setTimeout(checkConditions, interval);
      } else {
        setTimeout(checkConditions, interval);
      }
    },
    error: function(error) {
      console.log(error);
      setTimeout(checkConditions, interval);
    }
  });
}

function sendRequest1() {
  $.ajax({
    url: '/activate/',
    type: 'GET',
    success: function(response) {
      console.log(response);
      setTimeout(sendRequest1, 5000);
    },
    error: function(error) {
      console.log(error);
    }
  });
}

function sendRequest2() {
  $.ajax({
    url: '/activate/',
    type: 'GET',
    success: function(response) {
      console.log(response);
      setTimeout(sendRequest2, 10000);
    },
    error: function(error) {
      console.log(error);
    }
  });
}

function sendRequest3() {
  $.ajax({
    url: '/activate/',
    type: 'GET',
    success: function(response) {
      console.log(response);
      setTimeout(sendRequest3, 15000);
    },
    error: function(error) {
      console.log(error);
    }
  });
}

$(document).ready(function() {
  setTimeout(checkConditions, 5000);
});
