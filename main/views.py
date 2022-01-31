from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog_home(request):
    return HttpResponse("Blog home")

def blog_detail(request):
    return HttpResponse("Blog detail")

def profile(request):
    return HttpResponse("User Profile")