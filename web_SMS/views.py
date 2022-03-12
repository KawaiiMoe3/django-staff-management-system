from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import datetime
# Create your views here.

#Page Index
def Index(request):
    return render(request, 'index.html')

#Page Login
def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #Verify that the username and password are correct
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

#Forgot password
def ForgotPassword(request):
    return render(request, 'forgot-password.html')

#Page Contact
def Contact(request):
    return render(request, 'contact.html')

#Dynamic time
def getTime(request):
    #get local time
    now = datetime.datetime.now()
