from django import template
register = template.Library()
from django.db.models import Count


from blog.models import *
from django.template.loader import get_template
t = get_template('tags.html')
post = get_template('popularpost.html')


def populartags():
	popular=Tag.objects.annotate(no_of_post=Count('post')).order_by('-no_of_post').filter(no_of_post__gt=0)[:15]
	return {'popular' : popular}


register.inclusion_tag(t)(populartags)
populartags.is_safe = True


def popularposts():
	popular_posts = Post.published_objects.order_by('-no_views')[:5]
	return {'popular_posts': popular_posts}

register.inclusion_tag(post)(popularposts)
popularposts.is_safe = True




