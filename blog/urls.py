from django.urls import path
from blog.views import *

urlpatterns = [
    path('', blog_home_view, name='blog-home'),
    path('single', blog_single_view, name='blog-single')
]