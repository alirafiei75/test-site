from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.forms import CommentForm
from django.contrib import messages



def blog_view(request, **kwargs):
    # determining which post to show based on publish date
    now = timezone.now()
    posts = Post.objects.filter(published_date__lte=now)
    # setting status for published posts
    for post in posts:
        post.status = True
        post.save()
    # category division
    if kwargs.get('cat_name') !=None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    # author division
    if kwargs.get('author_username') !=None:
        posts = posts.filter(author__username=kwargs['author_username'])
    # tag division
    if kwargs.get('tag_name') !=None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])

    #paginating
    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
        
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)

def single_view(request, pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your comment submitted successfully')
        else:
            messages.add_message(request, messages.ERROR, "Your comment didn't submitted")
    # determining which posts to show in single page
    posts = Post.objects.filter(status=True)
    post = get_object_or_404(posts,pk=pid)
    # counted view adding method
    post.counted_views += 1
    post.save()
    # previous post
    pre_posts = Post.objects.filter(id__lt= pid, status=True)
    try:
        previous_post = pre_posts[0]
    except:
        previous_post = None
    # next post
    nex_posts = Post.objects.filter(id__gt= pid, status=True)
    l = len(nex_posts)-1
    try:
        next_post = nex_posts[l]
    except:
        next_post = None
    # comments
    comments = Comment.objects.filter(post=post.id, approved=True)
    # comment form
    form = CommentForm()

    context = {'post':post, 'previous':previous_post, 'next':next_post, 'comments':comments, 'form':form}
    return render(request, 'blog/blog-single.html', context)

def blog_search(request):
    # determining which post to show based on publish date
    now = timezone.now()
    posts = Post.objects.filter(published_date__lte=now)
    # setting status for published posts
    for post in posts:
        post.status = True
        post.save()
    if request.method == 'GET':
        posts = posts.filter(content__contains=request.GET.get('s'))
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)
