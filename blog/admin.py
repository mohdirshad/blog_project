from django.contrib import admin
from blog.models import Tag, Post, Comment
from django.forms import *
from django.db.models import *



class TagAdmin(admin.ModelAdmin):
	pass


class PostAdmin(admin.ModelAdmin):
	date_hierarchy = 'pub_date'
	list_display = ('title', 'pub_date', 'status','allow_comment', 'tagged')
	list_display_links = ['title',]
	list_editable = ['status', 'allow_comment',]
	search_fields = ('title', 'body',)
	list_filter = ('pub_date','tags','status')
	prepopulated_fields = {'slug': ('title',)}
	ordering = ('-pub_date',)
	filter_horizontal = ('tags',)
	radio_fields = {'status': admin.HORIZONTAL}
	exclude = ['no_views', 'featured']


class CommentAdmin(admin.ModelAdmin):
	list_display = ('post', 'user', 'body', 'pub_date', 'visible')
	search_fields = ('body','pub_date')
	list_editable = ['visible',]
	list_filter = ('pub_date','post')


admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
