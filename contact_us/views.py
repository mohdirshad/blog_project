# Create your views here.
from contact_us.form import ContactUsForm
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http.response import  HttpResponseRedirect
from contact_us.models import ContactUs


def v_add_contact(req):
    form=ContactUsForm()
    if req.method=="POST":
        form=ContactUsForm(req.POST)
        if form.is_valid():
            ContactUs.objects.create(name=form.cleaned_data['name'],
                                     contact_no=form.cleaned_data['contact_no'],
                                     email=form.cleaned_data['email'],
                                     message=form.cleaned_data['message']
                                     )
            return HttpResponseRedirect('/')
            
    return render_to_response('new_contact.html',{'contact_form':form},context_instance=RequestContext(req))
    
    
# def v_test(req):
#     if req.method=="POST":
#         return HttpResponse(req.POST.get('var','XXX'))
#     return render_to_response('test.html',context_instance=RequestContext(req))