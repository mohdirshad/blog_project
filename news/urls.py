from django.conf.urls import patterns, include, url
from .views import NewsList , NewsDetail

urlpatterns = patterns('',
    url(r'^$', NewsList.as_view() , name='newslist'),  
    url(r'^detail/(?P<pk>\d+)/$', NewsDetail.as_view() , name='newsdetail'),

)




