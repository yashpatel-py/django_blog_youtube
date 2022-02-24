from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignupForm
from django.contrib.auth import authenticate, login

# Create your views here.
def signUp(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account is created successfully")
            new_user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1']
            )
            
            login(request, new_user)
            return redirect('home')
        else:
            messages.error(request, "Error")
    else:
        form = SignupForm()
    return render(request, "authors/register.html", {'form': form})

def logIn(request):
    return render(request, "authors/login.html")