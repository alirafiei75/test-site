from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone


def blog_view(request):
    now = timezone.now()
    posts = Post.objects.filter(published_date__lte=now)
    for post in posts:
        post.status = True
        post.save()
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)

def single_view(request, pid):
    posts = Post.objects.filter(status=True)
    post = get_object_or_404(posts,pk=pid)
    post.counted_views += 1
    post.save()
    context = {'post':post}
    return render(request, 'blog/blog-single.html', context)

