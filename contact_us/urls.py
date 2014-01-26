
from django.conf.urls import url,patterns
from django.http.response import HttpResponse




urlpatterns = patterns('contact_us.views',
                       url(r'^$','v_add_contact', name='contact'),
                       )


    