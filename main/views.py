from django.shortcuts import render
from .models import Blog, BlogComment

# Create your views here.
def blog_home(request):
    all_blogs = Blog.objects.all()
    context = {
        'blogs': all_blogs
    }
    return render(request, "main/blog_home.html", context)

def blog_detail(request, slug_url):
    blog = Blog.objects.get(slug=slug_url)
    context = {
        'blog':blog
    }
    return render(request, "main/blog_detail.html", context)

def profile(request):
    return render(request, "main/profile.html")

def contactUs(request):
    return render(request, "main/contact_us.html")