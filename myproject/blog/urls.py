from django.urls import path
from blog.views import blogs_list

urlspatterns = [
    path("", blogs_list, name="blog_list")
]