from django.conf.urls import patterns, include, url
from auth import urls
from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.site.urls
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog_project.views.home', name='home'),
    # url(r'^blog_project/', include('blog_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
      url(r'^commnet/$', 'blog.views.comment',name="jbdk"),  
    # url(r'^auth/', include('auth.urls')),
    (r'^search/', include('haystack.urls')),
    (r'^tinymce/', include('tinymce.urls')),    
    url(r'^news/', include('news.urls')),
    url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),  url(r'^admin/', include(admin.site.urls)),

    url(r'^newsletter/', include('newsletter.urls')),
    url(r'^subscribe', 'homepage.views.add_subscriber'),
    url(r'^activate/$', 'homepage.views.activate'),
    url(r'^imagefit/', include('imagefit.urls')),
    url(r'^$', include('homepage.urls'), name='homepage'),
    url(r'^about/', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contactUS/', include('contact_us.urls')),

)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += urls.urlpatterns





