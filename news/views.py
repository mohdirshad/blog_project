# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.views.generic import ListView
from django.shortcuts import render_to_response
from .models import News
from blog.models import Post, Comment
from django.views.generic.base import View
from django.shortcuts import get_object_or_404


class NewsList(ListView):
    context_object_name = "news_list"
    queryset = News.get_published.all()
    template_name = 'news/newslist.html'
    paginate_by = 7


class NewsDetail(View):
    template_name = 'news/newsdetail.html'
    def get(self, request,pk):
        ci = RequestContext(request)
        news=get_object_or_404(News.get_published , pk=pk)
        popular_posts = Post.published_objects.order_by('-no_views')[:5]
    	recent_comments = Comment.objects.all()[:4]
        return render_to_response(self.template_name ,{'news_detail':news, 'popular_posts': popular_posts, 
                        'recent_comments': recent_comments,}, ci)




