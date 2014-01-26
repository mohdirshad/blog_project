from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

    # All post listing
    url(r'^$', 'homepage.views.homepage', name='homepage'),
)


