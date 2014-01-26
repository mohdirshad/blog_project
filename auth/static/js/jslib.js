

//alert("loading libjs.js");

$(document).ready(function() {
		        $('#login p').click(function() {
		            $('#login-form').slideToggle(300);
		            $(this).toggleClass('close');
		        });
		    }); // end ready
	


$(document).ready(function() {
			$('#login p').click(function() {
					 $("#forget-form").hide();
					 $('#login-form').show();
                $('.login-txt').slideDown(300);
				 });
          	
 			$(".forpass").click( function(){
				$('#login-form').hide();
				$("#forget-form").show();
				});
                                                                                                                    
		}); // end ready
        
function validate(email,pwd)
{
		
		
		
	try{
		
		
		var xmlhttp;
		if (window.XMLHttpRequest)
		  {// code for IE7+, Firefox, Chrome, Opera, Safari
		  xmlhttp=new XMLHttpRequest();
		  }
		else
		  {// code for IE6, IE5
		  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
		  }
		
		xmlhttp.onreadystatechange=function()
		  {
		  if (xmlhttp.readyState==4 && xmlhttp.status==200)
		    {
		    
		    //alert(xmlhttp.responseText);
		    arr=xmlhttp.responseText.split(":");
		    
			    if(xmlhttp.responseText=='200')
			    {
			    location.href = "/";
			    }
			    else
			    {
			    //var newLi = document.createElement("li");
			    //var text = document.createTextNode(arr[0]);
			    //newLi.appendChild(text);
			    //var ulnew = document.getElementById('login_error_ul');
			    //ulnew.appendChild(newLi);
			    
			    var temp="<div class='invalid_error'><ul><li>"+arr[0]+"</li></ul></div>";
			        
		        document.getElementById('login_error_div').innerHTML=temp;
		          
			    //alert(arr[0]);
			    }
		    }
		  }
		
		url="/validate?email="+email+"&password="+pwd
		
		xmlhttp.open("GET",url,true);
		xmlhttp.send();
		
		}
		catch(e)
		{alert(e);}
		   
}	
		
		
		
	
function forgetPWD(email)
{

	try{
		
		
		var xmlhttp;
		if (window.XMLHttpRequest)
		  {// code for IE7+, Firefox, Chrome, Opera, Safari
		  xmlhttp=new XMLHttpRequest();
		  }
		else
		  {// code for IE6, IE5
		  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
		  }
		
		xmlhttp.onreadystatechange=function()
		  {
		  if (xmlhttp.readyState==4 && xmlhttp.status==200)
		    {
		    
		    //alert(xmlhttp.responseText);
		    arr=xmlhttp.responseText.split(":");
		    
			    if(xmlhttp.responseText=='200')
			    {
			    location.href = "/";
			    }
			    else
			    {
			    
			    if(arr[0]=='200')
			    {
			    var temp="<div class='success_message'><ul><li>"+arr[1]+"</li></ul></div>";
			    document.getElementById('forget_error_div').innerHTML=temp;
			    document.getElementById('forget_email').value="";
			    }
			    else{
			    var temp="<div class='invalid_error'><ul><li>"+arr[0]+"</li></ul></div>";
		        document.getElementById('forget_error_div').innerHTML=temp;
		          
			    //alert(arr[0]);
			    }
			    }
		    }
		  }
		
		url="/recoverPassword?email="+email
		
		xmlhttp.open("GET",url,true);
		xmlhttp.send();
		
		}
		catch(e)
		{alert(e);}
		   
}	
		