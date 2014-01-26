from django.conf.urls import patterns, include, url
from django.conf import settings

from django.conf.urls import *
from django.conf import settings
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, DateDetailView
from blog.models import Post

post_info_dict = {
	'model': Post,
	'date_field': 'pub_date',
	'paginate_by': 10,
	'template_name': 'blog/display_object_list.html',
}

urlpatterns = patterns('',

    # All post listing
    url(r'^$', 'blog.views.post_archive_index', name='post_archive_index'),

    # Yearly Archieve
    url(r'^(?P<year>\d{4})/$', YearArchiveView.as_view(make_object_list = True, allow_future = True, **post_info_dict), name='post_archive_year'),
    
    # Monthly Archieve
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$', MonthArchiveView.as_view(**post_info_dict), name='post_archive_month'),
    
    # Daily Archieve
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$', DayArchiveView.as_view(**post_info_dict), name='post_archive_day'),

    # Post by Tag
    url(r'^tag/(?P<tag>[-\w]+)/$', 'blog.views.get_blog_by_tag', name='blog_by_tag'),
   
    # Post Entry Detail View
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'blog.views.detail_view', name="get_post_detail"),

    # Add Comment
    url(r'^add_comment/(?P<post_id>\d+)', 'blog.views.add_comment', name='add_comment'),

)


