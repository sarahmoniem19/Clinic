$("#clinic").click(function(){
  $("#lab_analysis").hide();
  $("#level").hide();
  $("#spec").show();
  $("#price").show();
  $("#location").show();
    $("#ranking").show();
});

$("#lab").click(function(){
  $("#spec").hide();
  $("#price").hide();
  $("#lab_analysis").show();
  $("#location").show();
  $("#level").show();
    $("#ranking").show();
});

$("#hospital").click(function(){
  $("#spec").hide();
  $("#price").hide();
  $("#lab_analysis").hide();
  $("#location").show();
  $("#level").show();
  $("#ranking").show();
});
