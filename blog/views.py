# Create your views here.
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from .models import Comment
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from tinymce.widgets import TinyMCE



def post_archive_index(request):
    all_posts = Post.published_objects.all()
    paginator = Paginator(all_posts, 7)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    ci = RequestContext(request)
    return render_to_response('blog/display_post_list.html', {'posts': posts}, ci)


class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={'cols': 90, 'rows': 5}))


def detail_view(request ,year, month, day, slug):
    """ view to get post detail and add comment """
    template_name = "blog/post_detail.html"  
    ci = RequestContext(request)
    form = CommentForm()
    post = get_object_or_404(Post.published_objects, slug=slug)
    post.no_views = post.no_views + 1
    post.save()
    return render_to_response(template_name ,{'form':form, 'post':post} , ci )



@csrf_exempt
def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    template_name = "blog/post_detail.html"
    year = post.pub_date.strftime("%Y")
    month = post.pub_date.strftime("%b").lower()
    day = post.pub_date.strftime("%d")
    slug = post.slug
    form = CommentForm(request.POST)
    ci = RequestContext(request)
    user = request.user
    if request.is_ajax():
        if request.method=="POST":
            comment=request.POST.get("comment",'')
            if comment:

                c = Comment.objects.create(post=post,user=user,body=comment)
                args = {'comment': c ,'profile':user.profile.image}
            else:
                args = {'error': 'Comment cannot be blank'}
            return render_to_response("blog/comment.html", args, ci)
        else:
            render_to_response("blog/comment.html", {}, ci)
    elif request.method == 'POST':
        if form.is_valid():
            comment = form.cleaned_data['comment']
            if comment:
                c = Comment.objects.create(post=post, user=user, body=comment)
                return HttpResponseRedirect(reverse('get_post_detail', kwargs={'year':year, 'month':month, 'day':day, 'slug':slug}))
        else:
            return render_to_response(template_name, {'form':form, 'post':post} , ci )
    else:
        return HttpResponseRedirect(reverse('get_post_detail', kwargs={'year':year, 'month':month, 'day':day, 'slug':slug}))



def get_blog_by_tag(request, tag):
    posts = Post.objects.filter(tags__name=tag)
    return render_to_response('blog/display_post_list.html', {'posts':posts, 'tag': tag})
	

def comment(request):
    c=Comment.objects.get(id=33)
    return render_to_response("blog/comment.html",{'comment':c},)