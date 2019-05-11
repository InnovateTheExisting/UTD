$(document).ready(function() {

	$("#username").focusin(function(){ 
        $("#username").next().remove();   
		$("#username").after( "<span class=info><strong>Username:</strong> Only alpha numeric</span>" );
	});

	$("#username").focusout(function(){
		$(".info").remove();
        var username = $("#username").val();
        var alpha_num = /^[A-Za-z0-9]+$/;

        if(alpha_num.test(username)){
            $("#username").after( "<span class=ok>Ok!</span>" );
        }
        else{
            $("#username").after( "<span class=error>Error!</span>" );
        }
	});

	$("#password").focusin(function(){
        $("#password").next().remove();
		$("#password").after( "<span class=info><strong>Password:</strong> Should be atleast 8 characters</span>" );
	});

	$("#password").focusout(function(){
		$(".info").remove();
        if($("#password").val().length>=8){
            $("#password").after( "<span class=ok>Ok!</span>" );
        }
        else{
            $("#password").after( "<span class=error>Error!</span>" );
        }
	});

	$("#email").focusin(function(){
        $("#email").next().remove();
		$("#email").after( "<span class=info><strong>Email:</strong> Enter valid email ID</span>" );
	});

	$("#email").focusout(function(){
		$(".info").remove();
        var email = $("#email").val();
        var email_val = /^[+a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i;

        if(email_val.test(email)){
            $("#email").after( "<span class=ok>Ok!</span>" );
        }
        else{
            $("#email").after( "<span class=error>Error!</span>" );
        }
	});  

                       
});