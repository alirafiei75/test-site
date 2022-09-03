from django import template
from blog.models import Post

register = template.Library()

@register.inclusion_tag('website/website-latest-posts.html')
def latestposts(arg=6):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts':posts }
