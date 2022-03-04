from pyexpat import model
from django.shortcuts import redirect, render
from .models import Blog, BlogComment, Contact
from .forms import ContactForm
from django.contrib import messages
from django.views import generic

# Create your views here.
# def blog_home(request):
#     all_blogs = Blog.objects.all()
#     context = {
#         'blogs': all_blogs
#     }
#     return render(request, "main/blog_home.html", context)

class blog_home(generic.ListView):
    model = Blog
    template_name = "main/blog_home.html"

# def blog_detail(request, slug_url):
#     blog = Blog.objects.get(slug=slug_url)
#     all_blogs = Blog.objects.all().order_by('-post_date')[:10]
#     context = {
#         'blog':blog,
#         'all_blogs': all_blogs
#     }
#     return render(request, "main/blog_detail.html", context)

class blog_detail(generic.DetailView):
    model = Blog
    template_name = "main/blog_detail.html"
    

# def contactUs(request):
#     form = ContactForm()
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "your form is submitted successfully")
#     else:
#         form = ContactForm()
#     return render(request, "main/contact_us.html", {"form": form})

class contactUs(generic.CreateView):
    form_class = ContactForm
    template_name = "main/contact_us.html"
    success_url = "/"