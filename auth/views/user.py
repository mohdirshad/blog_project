from auth.forms.user import RegistrationForm, EditRegistrationForm
from django.http.response import  HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import login
from auth.config import AUTH_ROOT, USER_UPLOAD_DIR
from auth.models import UserProfile
from django.contrib.auth import authenticate


# class DivErrorList(ErrorList):
#     def __unicode__(self):
#         return self.as_divs()
#     def as_divs(self):
#         #if not self: return []
#         #return u'<div class="errorlist">%s</div>' % ''.join([u'<div class="error">%s</div>' % e for e in self])
#         #return []
#         return u'' 

              
def upload(file_,fileName,subDir):
    import os
    try:
        with open(AUTH_ROOT+'static/UPLOADED/'+subDir+'/'+str(fileName), 'w') as destination:
            for chunk in file_.chunks():
                destination.write(chunk)
        return "UPLOADED/"+subDir+'/'+fileName
    except:
        os.makedirs(AUTH_ROOT+'static/UPLOADED/'+subDir)
        with open(AUTH_ROOT+'static/UPLOADED/'+subDir+'/'+str(fileName), 'w') as destination:
            for chunk in file_.chunks():
                destination.write(chunk)
        return "UPLOADED/"+subDir+'/'+fileName



def v_add_user(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    
    form=RegistrationForm(auto_id=False)
    if request.method=="POST":
        form = RegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            #username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            image=None
            
            if request.FILES.get('image'):
                image=upload(form.cleaned_data['image'],email+".jpg",USER_UPLOAD_DIR)
                
            user=User.objects.create_user(username=email,email=email,password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            user.is_staff=False
            
            UserProfile.objects.create(user=user,image=image)
            new_user=authenticate(username=user.username, password=password)
            login(request,new_user)
            return HttpResponseRedirect('/')
        else:
            return render_to_response('user/add_user.html',{'form':form},context_instance=RequestContext(request))
    else:
        return render_to_response('user/add_user.html',{'form':form},context_instance=RequestContext(request))


def v_edit_user(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/")
    
    cu=User.objects.get(id=request.user.id)
    form=EditRegistrationForm(initial=cu.__dict__)
    if request.method=="POST":
        form = EditRegistrationForm(request.POST,request.FILES)
        #form.setter(cu.email)
        if form.is_valid():
            #email=cu.email
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
                         
                            
            cu.first_name = first_name
            cu.last_name = last_name
            #cu.email=email
            cu.save()
            
            if request.FILES.get('image'):
                image=upload(form.cleaned_data['image'],cu.email+".jpg",USER_UPLOAD_DIR)
                cu_profile=UserProfile.objects.get(user=cu)
                cu_profile.image=image
                cu_profile.save()
            return HttpResponseRedirect('/')
        else:
            return render_to_response('user/edit_user.html',locals(),context_instance=RequestContext(request))
    else:
        return render_to_response('user/edit_user.html',locals(),context_instance=RequestContext(request))


    
    
    