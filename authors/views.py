from django.shortcuts import render

# Create your views here.
def signUp(request):
    return render(request, "authors/register.html")

def logIn(request):
    return render(request, "authors/login.html")