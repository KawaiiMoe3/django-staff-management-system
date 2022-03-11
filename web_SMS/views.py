from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

#Page Index
def Index(request):
    return render(request, 'index.html')

#Page Login
def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('index')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, "Username or Password are wrong!")
            return redirect('login')
    else:
        return render(request, 'login.html')

#Logout
def Logout(request):
    #log out 
    logout(request)
    messages.success(request, "You were logged out, see you next time!")
    return redirect('login')