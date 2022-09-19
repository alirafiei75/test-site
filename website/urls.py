from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('', index_view, name='index'),
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact'),
    path('password_reset', password_reset_view, name='password_reset'),
    path('password_reset/done', password_reset_done_view, name='password_reset_done'),
    path('password_reset_confirm/<str:username>/<str:uidb64>/<str:token>', password_reset_confirm_view, name='password_reset_confirm'),
    path('password_reset/complete', password_reset_complete_view, name='password_reset_complete'),
]