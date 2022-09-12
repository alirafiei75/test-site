from django import template
from blog.models import Post, Category, Comment

register = template.Library()

@register.inclusion_tag('blog/blog-popular-posts.html')
def popularposts(arg=3):
    posts = Post.objects.filter(status=1).order_by('-counted_views')[:arg]
    return {'posts':posts }

@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat = {}
    for name in categories:
        cat[name] = posts.filter(category=name).count()
    return {'categories':cat}

@register.simple_tag(name='comments_count')
def function(pid):
    return Comment.objects.filter(post=pid, approved=True).count()
