from django.shortcuts import render
from blog.models import Blog
# Create your views here.

def blogs_list(request):
    blogs = Blog.objects.all()
    context = {
        "blogs_list": blogs
    }
    return render(
        request, 
        template_name="blog/blog_list.html",
        context=context
    )