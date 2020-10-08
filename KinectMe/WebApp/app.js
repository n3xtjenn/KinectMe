$("#cambio").click(function(){
  var comodin = $("#comodin").val();
  if (comodin == 1) {
    $("#signup").show();
    $("#login").hide();
    $("#comodin").val("2");
    $("#cambio").html("Go to Login");
  }else {
    $("#signup").hide();
    $("#login").show();
    $("#comodin").val("1");
    $("#cambio").html("Go to Sign Up");
  }

});



