from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def signUp(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "Your account is created successfully")
        return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, "authors/register.html", {'form': form})

def logIn(request):
    return render(request, "authors/login.html")