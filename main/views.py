from django.shortcuts import redirect, render
from .models import Blog, BlogComment, Contact
from .forms import ContactForm
from django.contrib import messages

# Create your views here.
def blog_home(request):
    all_blogs = Blog.objects.all()
    context = {
        'blogs': all_blogs
    }
    return render(request, "main/blog_home.html", context)

def blog_detail(request, slug_url):
    blog = Blog.objects.get(slug=slug_url)
    all_blogs = Blog.objects.all().order_by('-post_date')[:10]
    context = {
        'blog':blog,
        'all_blogs': all_blogs
    }
    return render(request, "main/blog_detail.html", context)

def profile(request):
    return render(request, "main/profile.html")

def contactUs(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "your form is submitted successfully")
    else:
        form = ContactForm()
    return render(request, "main/contact_us.html", {"form": form})