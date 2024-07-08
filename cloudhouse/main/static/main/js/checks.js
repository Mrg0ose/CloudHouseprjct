$(document).ready(function() {
  $('.checkbox-round').click(function() {
    $('.checkbox-round').not(this).prop('checked', false);
  });
});
