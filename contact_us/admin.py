

from django.contrib import admin
from contact_us.models import ContactUs



class decorateContactUs(admin.ModelAdmin):
    
    list_display = ('name','email','contact_no')
    #list_display_links = ["user",]
    
        

admin.site.register(ContactUs,decorateContactUs)