import datetime
from time import time
from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from django import template
from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils.timezone import utc
from sorl.thumbnail import ImageField


register = template.Library()
# Generate timestamp based filename of uploaded articles
def get_upload_file_name(instance, filename):
	return 'uploaded_files/%s_%s'%(str(time()).replace('.','_'), filename)



class Tag(models.Model):
	name = models.CharField(max_length=30, unique=True)
	
	def __unicode__(self):
		return self.name



class PostManager(models.Manager):
	def get_query_set(self):
		return super(PostManager, self).get_query_set().filter(status='l')


class Post(models.Model):
	STATUS_CHOICES = (
	('d', 'Draft'),
	('l', 'Live'),
	)
	title = models.CharField(max_length=200, help_text='Give a Short and Meaningful Title')
	body = models.TextField(blank=True, null=True)
	image = models.FileField(upload_to=get_upload_file_name, default='', blank=True, null=True, help_text='\
		Post with Descriptive Image attract more Visitors.')
	pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Publish Date')
	last_modified = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='l')
	allow_comment = models.BooleanField(default=True, help_text='Allow Users to Comment on this Post?')
	featured = models.BooleanField(default=False, verbose_name="Is Featured Article?", help_text='Check if this Post has to be Featured on Home Page!')
	tags = models.ManyToManyField(Tag, blank=True, null=True,  help_text='Descriptive Tags let user search your article with ease.')
	slug = models.SlugField(max_length=20, unique=True, 
		verbose_name=u'Unique Identifier For Post Url.',
		help_text="Slug Value is unique and generated automatically. If Slug error occur on save, please try to make it unique but keeping it meaningful.")
	no_views = models.IntegerField(max_length = 5 , verbose_name ="No of views " , default=0)
	objects = models.Manager()
	published_objects = PostManager()

	class Meta:
		verbose_name_plural = ("Posts")
		ordering = ["-pub_date"]

	def save(self, *args, **kwargs):
		if self.body == '':
			self.status = 'd'
		super(Post, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title

	def tagged(self):
		return ', '.join([t.name for t in self.tags.all()])
    	#admin_names.short_description = "Admin Names"

	@register.filter
	def time_hours(self):
		t= (datetime.datetime.now().replace(tzinfo=utc)-self.pub_date).days
		return t

	@register.filter
	def get_class_name(value):
		return value.__class__.__name__


	@models.permalink
	def get_absolute_url(self):
		return ('get_post_detail', (), {'year': self.pub_date.strftime("%Y"),
											'month': self.pub_date.strftime("%b").lower(),
											'day': self.pub_date.strftime("%d"),
											'slug': self.slug})

	
class Comment(models.Model):
	post = models.ForeignKey(Post)
	user = models.ForeignKey(User)
	body = models.TextField()
	pub_date = models.DateTimeField(auto_now_add=True)
	visible = models.BooleanField(default=True)
	
	class Meta:
		ordering = ["pub_date"]

	def __unicode__(self):
		return self.user.username


	@register.filter
	def time_hours(self):
		t= (datetime.datetime.now().replace(tzinfo=utc)-self.pub_date).days
		return t

