from django.contrib import admin
from .models import News
from django.db.models import *
from tinymce.widgets import TinyMCE


class NewsAdmin(admin.ModelAdmin):
    date_hierarchy = 'posted_on'
    list_display = ('title', 'posted_on')
    search_fields = ('title',)
    list_filter = ('posted_on',) 
    ordering = ('-posted_on',)


admin.site.register(News , NewsAdmin)

