from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='weblog'),
    path('<int:pid>', single_view, name='single'),
]