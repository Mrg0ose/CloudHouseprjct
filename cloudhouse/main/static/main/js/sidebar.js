var sidebar = document.getElementById("sidebar");
var toggle = document.getElementById("sidebar-toggle");

toggle.addEventListener('mouseenter', function() {
  sidebar.classList.add("active");
});

sidebar.addEventListener('mouseleave', function() {
  sidebar.classList.remove("active");
});


