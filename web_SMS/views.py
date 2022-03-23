from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import datetime
# Create your views here.

#Page Login
def Login(request):
    return render(request, 'login.html')

#doLogin function
def doLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #Verify that the username and password are correct
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #Check user_type
            if user.user_type == "1":
                # Redirect to an admin template.
                return redirect('index')
            elif user.user_type == "2":
                # Redirect to a staff template.
                return redirect('index_staff')
        else:
            # Return an 'invalid login' error message.
            messages.error(request, "Username or Password are wrong!")
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
    return render(request, 'registration/password_reset_form.html')

#Dynamic time
def getTime(request):
    #get local time
    now = datetime.datetime.now()
