

from django.contrib import admin
from auth.models import UserProfile


class decorateUserProfile(admin.ModelAdmin):
    
    list_display = ('user','image','isActive')
    list_display_links = ["user",]
    
        

admin.site.register(UserProfile,decorateUserProfile)