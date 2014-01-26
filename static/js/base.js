


		       


$(document).ready(function(){

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

jQuery.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

 
$(".addcomment").click(function(e){

    e.preventDefault();
    var post_id = this.id;

    var comment = $("#id_comment").val(); 
    $("#id_comment").val(""); 
    if(comment != ""){
    $.ajax({
            type: "POST",
            url: "/blog/add_comment/"+post_id+"/",
            data: {'comment':comment} ,
            datatype:"image/jpg",
            success: function(data){
              
                    // alert(data);
                    $( ".commentbody li:last" ).html( "<li>"+data+"</li>" );
                    },
                

    });
}
});
$('#id_comment').keypress(function(e){
	$('.addcomment').attr('disabled',false);
   		 if(e.which == 13){
        $(".addcomment").click();//Trigger search button click event
        e.preventDefault();
    }
     });

$(".login-required").click(function(){

   window.open('/login/','_self'); 

});

$(".login-required").keypress(function(){

   window.open('/login/','_self'); 

});




function validateEmail($email) {
  var emailReg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
  if( !emailReg.test( $email ) ) {
    return false;
  } else {
    return true;
  }
}



$("#submit-button").click(function(e){

    var email_field = $('#id_email_field').val();


    if (email_field==""){ 




        $(".errormsg").css({'color':'red'});
        $(".errormsg").text('This field id required');
        $(".errormsg").show(500) ;
    e.preventDefault();
    return false;
};


    if( !validateEmail(email_field)) {  
$(".errormsg").css({'color':'red'});
        $(".errormsg").text('Please enter a valid email id');
        $(".errormsg").show(500) ;
    e.preventDefault();
    return false;

    }
  if( validateEmail(email_field))  {
            
    $('#id_email_field').slideUp(500);

        $(".errormsg").css({'color':'green'});
       $(".errormsg").text('Your request has been send for subcription');
            $(".errormsg").show(00,function(){ 
                $(".errormsg").delay(3000).fadeOut(500 ,function(){
                $('#id_email_field').val("");
                $('#id_email_field').slideDown(1000); 
                });
                });

            $.ajax({
        type: "POST",
        url: "/subscribe/",
        data: {'email_field': email_field},
        success: function(data){

            console.log(data) ; 

            }
               
    });
   
e.preventDefault();
}

    

});


<<<<<<< HEAD
$("#login_button_id").click(function(e){
    e.preventDefault();
    
    var email = $("#login_email_id").val();
    var password = $("#login_password_id").val(); 
    
    $.ajax({
            type: "POST",
            url: "/validate/",
            data: {'email':email,'password':password} ,
            success: function(data){
                    alert(data);
                    },

    });
=======

>>>>>>> f05a5cbbc348be5ee2c04e3761af500aa726e3e0
});



});
