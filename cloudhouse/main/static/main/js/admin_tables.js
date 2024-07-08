  var contractsLink = document.getElementById('contracts');
  var clientsLink = document.getElementById('clients');
  var devicesLink = document.getElementById('devices');
  var tempLink = document.getElementById('temp');
  var energyLink = document.getElementById('energy');
  var lightLink = document.getElementById('light');
  var voiceLink = document.getElementById('voice');
  var notificationsLink = document.getElementById('notifications');
  var settingsLink = document.getElementById('settings');
  var favoritesLink = document.getElementById('favorites');
  var reportsLink = document.getElementById('reports');

  var contractsTable = document.getElementById('contractsTable');
  var clientsTable = document.getElementById('clientsTable');
  var devicesTable = document.getElementById('devicesTable');
  var tempTable = document.getElementById('tempTable');
  var energyTable = document.getElementById('energyTable');
  var lightTable = document.getElementById('lightTable');
  var voiceTable = document.getElementById('voiceTable');
  var notificationsTable = document.getElementById('notificationsTable');
  var settingsTable = document.getElementById('settingsTable');
  var favoritesTable = document.getElementById('favoritesTable');
  var reportsTable = document.getElementById('reportsTable');

  function hideAllTables() {
    contractsTable.style.display = 'none';
    clientsTable.style.display = 'none';
    devicesTable.style.display = 'none';
    tempTable.style.display = 'none';
    energyTable.style.display = 'none';
    lightTable.style.display = 'none';
    voiceTable.style.display = 'none';
    notificationsTable.style.display = 'none';
    settingsTable.style.display = 'none';
    favoritesTable.style.display = 'none';
    reportsTable.style.display = 'none';
  }

  function showTable(tableId) {
    hideAllTables();
    var table = document.getElementById(tableId);
    if (table) {
      table.style.display = 'block';
    }
  }


function saveActiveTable(tableId) {
  localStorage.setItem('activeTable', tableId);
}


function loadActiveTable() {
  return localStorage.getItem('activeTable');
}


var activeTableId = loadActiveTable();
if (activeTableId) {
  showTable(activeTableId);
} else {
  showTable('contractsTable');
}

contractsLink.addEventListener('click', function() {
  showTable('contractsTable');
  saveActiveTable('contractsTable');
});

clientsLink.addEventListener('click', function() {
  showTable('clientsTable');
  saveActiveTable('clientsTable');
});

devicesLink.addEventListener('click', function() {
  showTable('devicesTable');
  saveActiveTable('devicesTable');
});

tempLink.addEventListener('click', function() {
  showTable('tempTable');
  saveActiveTable('tempTable');
});

energyLink.addEventListener('click', function() {
  showTable('energyTable');
  saveActiveTable('energyTable');
});

lightLink.addEventListener('click', function() {
  showTable('lightTable');
  saveActiveTable('lightTable');
});

voiceLink.addEventListener('click', function() {
  showTable('voiceTable');
  saveActiveTable('voiceTable');
});

notificationsLink.addEventListener('click', function() {
  showTable('notificationsTable');
  saveActiveTable('notificationsTable');
});

settingsLink.addEventListener('click', function() {
  showTable('settingsTable');
  saveActiveTable('settingsTable');
});

favoritesLink.addEventListener('click', function() {
  showTable('favoritesTable');
  saveActiveTable('favoritesTable');
});

reportsLink.addEventListener('click', function() {
  showTable('reportsTable');
  saveActiveTable('reportsTable');
});