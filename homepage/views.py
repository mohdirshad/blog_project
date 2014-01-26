from blog.models import Post, Comment
from news.models import News
from homepage.models import Subscriber
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.validators import validate_email
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from hashlib import sha1
from datetime import datetime

def homepage(request):
    posts = Post.published_objects.all()[:4]
    news = News.get_published.all()[:4]
    ci = RequestContext(request)
    return render_to_response('homepage/index.html', {'posts': posts, 
    	'news_list': news,}, ci)



@csrf_exempt
def add_subscriber(request, email=None):
	if request.method == 'POST':
		email = request.POST['email_field']
		try:
			validate_email(email)					
		except:
			msg = ""
			return HttpResponse(msg)
		
		try:
			instance = Subscriber.objects.get(email=email)
			msg ="email already exits"
			return HttpResponse(msg)	
		except:
			time = datetime.now().isoformat()
			plain = email + '\0' + time
			token = sha1(plain)
			linktoken=token.hexdigest()
			e = Subscriber.objects.create(email=email , token = linktoken)
			mail_msg='''
            Hi 
            
            click the following link to Subscribe"+"http://127.0.0.1:8002/activate/?token={token}
            
            Thanks & Regards,
            Moocs Mentors Team
            '''.format(
                       token=linktoken,
            ) 

			send_mail('Subcription Mail', mail_msg, 'Brentwoods',[email], fail_silently=False)
			msg = "{0} added activate from Your mail".format(email)	 
		return HttpResponse(msg)
		

def activate(request):
	linktoken = request.GET.get('token')
	instance=Subscriber.objects.get(token = linktoken)
	instance.active = True
	instance.save()
	return HttpResponseRedirect("/")
	