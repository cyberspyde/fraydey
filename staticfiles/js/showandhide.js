$(document).ready(function(){
  $('.myElement').slideUp('slow');
  $('.myElementPartlyPaid').slideUp('slow');
  
  $(".up-down").change(function(){
    if (!$('.up-down:checked').length) {
      $('.myElement').slideUp('slow');
    } else {
      $('.myElement').slideDown('slow');
    }
  });

  
  $(".up-down-partlypaid").change(function(){
    if ($('.up-down-partlypaid:checked').length) {
      $('.myElementPartlyPaid').slideDown('slow');
    } else {
      $('.myElementPartlyPaid').slideUp('slow');
    }
  });
});
