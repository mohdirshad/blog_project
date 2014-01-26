from django.db import models

# Create your models here.


class ContactUs(models.Model):
    name=models.CharField(max_length=150)
    contact_no=models.CharField(max_length=15,null=True,blank=True)
    email=models.EmailField()
    message=models.TextField()
    
    def __unicode__(self):
        return "%s - %s "%(self.name,self.email)
    
    class Meta:
        
        verbose_name="Contacts And Queries"
        verbose_name_plural="Contacts And Queries"
    
    
    
    