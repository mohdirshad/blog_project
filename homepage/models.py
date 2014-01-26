from django.db import models

# Create your models here.
class Subscriber(models.Model):
	email = models.EmailField(unique=True)
	active = models.BooleanField(default =False)
	token = models.CharField(max_length=200)

	def __unicode__(self):
		return self.email