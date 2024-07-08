var mymap = L.map('mapid').setView([54.72837296812841, 55.970597211988185], 17);
L.marker([54.72837296812841, 55.970597211988185], {title: "CloudHouse"}).addTo(mymap).bindPopup("Мы здесь!");
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors',
    maxZoom: 18
}).addTo(mymap);


L.control.locate().addTo(mymap);
