from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
	"""user profile model"""
	class Meta:
		verbose_name="Blog Users"
		verbose_name_plural="Blog Users"
	
	user=models.OneToOneField(User , related_name="profile")
	image=models.ImageField(upload_to='django_upload/')
	
	def __unicode__(self):
		return self.user.username
	
	def isActive(self):
		if self.user.is_active:
			return True
		else:
			return False
	
	def display_name(self):
		return self.user.email.split('@')[0]
		




