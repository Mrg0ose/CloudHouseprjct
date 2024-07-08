var previousData = null;
var dataChanged = false;

function updateSensorData() {
  $.ajax({
    url: "ajaxbd",
    type: "GET",
    success: function(data) {
    if (!previousData || JSON.stringify(data) !== JSON.stringify(previousData)) {
        previousData = data;
      var tbodyEnergy = $(".tabsen .enn");
      tbodyEnergy.empty();
      var tbodyTemp = $(".tabsen .tempp");
      tbodyTemp.empty();
      var tbodyLight = $(".tabsen .svett");
      tbodyLight.empty();
      var tbodyVoice = $(".tabsen .voicee");
      tbodyVoice.empty();
      var favwin = $(".fav_win");
      favwin.empty();

      var contracts = data.contract;
      var client = data.client;
      var light = data.light;
      var temp = data.temp;
      var energy = data.energy;
      var voice = data.voice;
      var contractCount = data.count;

      if (contractCount === 1) {
        var contractData = contracts;
        var clientData = client;
        var lightData = light;
        var tempData = temp;
        var energyData = energy;
        var voiceData = voice;
        displayContractData(contractData);
      } else {
        var contractCodes = Object.keys(contracts);
        var currentContractIndex = 0;
        var currentContractData = contracts[contractCodes[currentContractIndex]];

        $(".squarecontract_con").click(function() {
            tbodyEnergy.empty();
    tbodyTemp.empty();
    tbodyLight.empty();
    tbodyVoice.empty();
    favwin.empty();

          currentContractIndex = (currentContractIndex + 1) % contractCount;
          currentContractData = contracts[contractCodes[currentContractIndex]];
          displayContractData(currentContractData);
        });

        displayContractData(currentContractData);
      }

      function displayContractData(contractData) {
        $(".status").text('Статус: ' + contractData.device.status);
        $("#namee").text('Название: ' + contractData.device.device_name);
        $("#desc").text('Описание: ' + contractData.device.device_description);
        $("#ipp").text('Адрес: ' + contractData.device.ip);
        var date_pay = new Date(contractData.contract.contract_payment);
        $(".szcont").text('Следующая оплата: ' + date_pay.toLocaleDateString());
        $(".prss").text('К оплате: ' + contractData.contract.price + "₽");
        $(".szcontr").text(contractData.contract.code_contract);
        $(".bldname").text(data.client.surname + " " + data.client.name + " " + data.client.patronymic);
        $(".adrs").text('Адрес: ' + contractData.address.address);
        $("#hoz").text(data.client.surname + " " + data.client.name + " " + data.client.patronymic);
        $("#adrhoz").text(contractData.address.address);
        $("#mobb").text('Телефон: ' + data.client.mobile);
        $("#emm").text('Почта: ' + data.client.email);

        var energySensors = contractData.energy;
        var temperatureSensors = contractData.temp;
        var lightSensors = contractData.light;
        var voiceSensors = contractData.voice;
        var energyf = contractData.fenergy;
        var temperaturef = contractData.ftemp;
        var lightf = contractData.flight;
        var voicef = contractData.fvoice;

        $.each(energySensors, function(i, energy) {
          var tr = $("<tr>").appendTo(tbodyEnergy);
          var date = new Date(energy.lastpar_date);
          $("<td>").html("<img class='sensor_imaga' src='/static/main/img/molnia_yslygi.png'>").appendTo(tr);
        $("<td>").text(energy.sensor_name).appendTo(tr);
        $("<td>").text(energy.description).appendTo(tr);
        $("<td>").text(energy.ip).appendTo(tr);
        $("<td>").text(date && date.getTime() !== 0 ? date.toLocaleDateString() : "Нет данных").appendTo(tr);
        $("<td>").text(energy.lastpar_time ? energy.lastpar_time : "Нет данных").appendTo(tr);
        $("<td>").text(energy.sensor_result_voltage ? energy.sensor_result_voltage + "V" : "Нет данных").appendTo(tr);
        $("<td>").text(energy.sensor_result_energy ? energy.sensor_result_energy + " КлВт/ч" : "Нет данных").appendTo(tr);
        $("<td>").text(energy.sensor_type).appendTo(tr);
        favorite = energy.favorite == 0 ? "unfavorit.png" : "favorit.png";
        $("<td>").html("<a class='tb_but' data-tag='" + energy.sensor_type + "' data-id='" + energy.sensor_id + "'><img src='/static/main/img/" + favorite + "' class='favorit_button' alt=''></a>").appendTo(tr);
        });

        $.each(temperatureSensors, function(i, temp) {
          var tr = $("<tr>").appendTo(tbodyTemp);
          var date = new Date(temp.lastpar_date);
          $("<td>").html("<img class='sensor_imaga' src='/static/main/img/temperatyra_yslygi.png'>").appendTo(tr);
        $("<td>").text(temp.sensor_name).appendTo(tr);
        $("<td>").text(temp.description).appendTo(tr);
        $("<td>").text(temp.ip).appendTo(tr);
        $("<td>").text(date && date.getTime() !== 0 ? date.toLocaleDateString() : "Нет данных").appendTo(tr);
        $("<td>").text(temp.lastpar_time ? temp.lastpar_time : "Нет данных").appendTo(tr);
        $("<td>").text(temp.temperature_result ? temp.temperature_result + "°C" : "Нет данных").appendTo(tr);
        $("<td>").text(temp.sensor_type).appendTo(tr);
        favorite = temp.favorite == 0 ? "unfavorit.png" : "favorit.png";
        $("<td>").html("<a class='tb_but' data-tag='" + temp.sensor_type + "' data-id='" + temp.sensor_id + "'><img src='/static/main/img/" + favorite + "' class='favorit_button' alt=''></a>").appendTo(tr);
        });

        $.each(lightSensors, function(i, light) {
          var tr = $("<tr>").appendTo(tbodyLight);
          var date = new Date(light.lastpar_date);
          $("<td>").html("<img class='sensor_imaga' src='/static/main/img/svet_yslygi.png'>").appendTo(tr);
        $("<td>").text(light.sensor_name).appendTo(tr);
        $("<td>").text(light.description).appendTo(tr);
        $("<td>").text(light.ip).appendTo(tr);
        $("<td>").text(date && date.getTime() !== 0 ? date.toLocaleDateString() : "Нет данных").appendTo(tr);
        $("<td>").text(light.lastpar_time ? light.lastpar_time : "Нет данных").appendTo(tr);
        if (light.light_result == 0) {
          $("<td>").text("Off").appendTo(tr);
        } else {
          $("<td>").text("On").appendTo(tr);
        }
        $("<td>").text(light.sensor_type).appendTo(tr);
        favorite = light.favorite == 0 ? "unfavorit.png" : "favorit.png";
        $("<td>").html("<a class='tb_but' data-tag='" + light.sensor_type + "' data-id='" + light.sensor_id + "'><img src='/static/main/img/" + favorite + "' class='favorit_button' alt=''></a>").appendTo(tr);
        });

        $.each(voiceSensors, function(i, voice) {
          var tr = $("<tr>").appendTo(tbodyVoice);
          var date = new Date(voice.lastpar_date);
          $("<td>").html("<img class='sensor_imaga' src='/static/main/img/zvyk_yslygi.png'>").appendTo(tr);
        $("<td>").text(voice.sensor_name).appendTo(tr);
        $("<td>").text(voice.description).appendTo(tr);
        $("<td>").text(voice.ip).appendTo(tr);
        $("<td>").text(date && date.getTime() !== 0 ? date.toLocaleDateString() : "Нет данных").appendTo(tr);
        $("<td>").text(voice.lastpar_time ? voice.lastpar_time : "Нет данных").appendTo(tr);
        $("<td>").text(voice.voice_result ? voice.voice_result + "Db" : "Нет данных").appendTo(tr);
        $("<td>").text(voice.sensor_type).appendTo(tr);
        favorite = voice.favorite == 0 ? "unfavorit.png" : "favorit.png";
        $("<td>").html("<a class='tb_but' data-tag='" + voice.sensor_type + "' data-id='" + voice.sensor_id + "'><img src='/static/main/img/" + favorite + "' class='favorit_button' alt=''></a>").appendTo(tr);
        });

        $.each(temperaturef, function(i, ftemp) {
          var date = new Date(ftemp.lastpar_date);
          var senstemp = '<div class="fav_sensor_win">'+
'<div class="sensor_image">'+
    '<img src="static/main/img/temperatyra_yslygi.png" alt="" class="sen_img">'+
'</div>'+
    '<div class="sensor_description">' +
        '<h3 class="tag_name">' + ftemp.description + '</h3>' +
        '<h4 class="data_par">' + 'Название: ' + ftemp.sensor_name + '</h4>' +
        '<h4 class="data_par">' + 'Дата показания: ' + date.toLocaleDateString() + '</h4>' +
        '<h4 class="data_par">' + 'Время показания: ' + ftemp.lastpar_time + '</h4>' +
    '</div>'+
    '<div class="parameter">'+'<h4 class="param">'+ftemp.temperature_result+'°C'+'</h4>'+
    '</div>'+
        '</div>';
        $(".fav_win").append(senstemp);
        });

        $.each(voicef, function(i, fvoice) {
          var date = new Date(fvoice.lastpar_date);
          var senstemp = '<div class="fav_sensor_win">'+
'<div class="sensor_image">'+
    '<img src="static/main/img/zvyk_yslygi.png" alt="" class="sen_img">'+
'</div>'+
    '<div class="sensor_description">' +
        '<h3 class="tag_name">' + fvoice.description + '</h3>' +
        '<h4 class="data_par">' + 'Название: ' + fvoice.sensor_name + '</h4>' +
        '<h4 class="data_par">' + 'Дата показания: ' + date.toLocaleDateString() + '</h4>' +
        '<h4 class="data_par">' + 'Время показания: ' + fvoice.lastpar_time + '</h4>' +
    '</div>'+
    '<div class="parameter">'+'<h4 class="param">'+fvoice.voice_result+'Db'+'</h4>'+
    '</div>'+
        '</div>';
        $(".fav_win").append(senstemp);
        });


        $.each(energyf, function(i, fenergy) {
          var date = new Date(fenergy.lastpar_date);
          var senstemp = '<div class="fav_sensor_win_en">'+
'<div class="sensor_image">'+
    '<img src="static/main/img/molnia_yslygi.png" alt="" class="sen_img">'+
'</div>'+
    '<div class="sensor_description">' +
        '<h3 class="tag_name">' + fenergy.description + '</h3>' +
        '<h4 class="data_par">' + 'Название: ' + fenergy.sensor_name + '</h4>' +
        '<h4 class="data_par">' + 'Дата показания: ' + date.toLocaleDateString() + '</h4>' +
        '<h4 class="data_par">' + 'Время показания: ' + fenergy.lastpar_time + '</h4>' +
    '</div>'+
    '<div class="parameter1">' + '<h6 class="param">' + 'Напряжение: '+ fenergy.sensor_result_voltage+'V'+'<br>' + '<br>' +
    'Энергия:' +fenergy.sensor_result_energy + 'КлВт/ч' + '</h6>' +
    '</div>'+
        '</div>';
        $(".fav_win").append(senstemp);
        });

        $.each(lightf, function(i, flight) {
  var date = new Date(flight.lastpar_date);
  var lightStatus = flight.light_result == 0 ? "Off" : "On";
  var senstemp = '<div class="fav_sensor_win_light" data-sensor_id="' + flight.sensor_id + '">' +
  '<div class="sensor_image">' +
    '<img src="static/main/img/svet_yslygi.png" alt="" class="sen_img">' +
  '</div>' +
  '<div class="sensor_description">' +
    '<h3 class="tag_name">' + flight.description + '</h3>' +
    '<h4 class="data_par">' + 'Название: ' + flight.sensor_name + '</h4>' +
    '<h4 class="data_par">' + 'Дата показания: ' + date.toLocaleDateString() + '</h4>' +
    '<h4 class="data_par">' + 'Время показания: ' + flight.lastpar_time + '</h4>' +
  '</div>' +
  '<div class="parameter">' +
    '<h4 class="param">' + lightStatus + '</h4>' +
  '</div>' +
'</div>';

  $(".fav_win").append(senstemp);
});
      }
     }
    },
    error: function(xhr, errmsg, err) {
      console.log(xhr.status + ": " + xhr.responseText);
    }
  });
}
updateSensorData();
setInterval(updateSensorData, 1000);