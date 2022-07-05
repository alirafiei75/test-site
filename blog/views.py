from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone


def blog_view(request):
    # determining which post to show based on publish date
    now = timezone.now()
    posts = Post.objects.filter(published_date__lte=now)
    # setting status for published posts
    for post in posts:
        post.status = True
        post.save()

    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)

def single_view(request, pid):
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

    context = {'post':post, 'previous':previous_post, 'next':next_post}
    return render(request, 'blog/blog-single.html', context)

