$(document).ready(function(){
  $('.switch').click(function(){
    $(this).toggleClass("switch--off");
    taggleCmd();
    if($(this).hasClass("switch--off")){ 
        $(this).find(".switch__status").text("OFF");    
    } else {   
        $(this).find(".switch__status").text("ON");    
    }
  });
});