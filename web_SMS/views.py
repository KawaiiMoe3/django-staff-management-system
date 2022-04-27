from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import datetime
# Create your views here.

#Page Login
def Login(request):
    #Get cookie if username have stored in cookie
    if 'username' in request.COOKIES:
        #Remember username
        username = request.COOKIES['username']
    else:
        username = ''

    #Create a dictionary
    context = {
        'username' : username,
    }
    return render(request, 'login.html', context)

#doLogin function
def doLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        remember = request.POST.get('remember')
        #Verify that the username and password are correct
        user = authenticate(request, username=username, password=password)
        if user is not None:
            #Username and password exists, login and redirect to index page respectively
            responseAdmin = redirect('index') 
            responseStaff = redirect('index_staff')
            login(request, user)
            #If "remember me" was checked, store their cookie for 3days period
            if remember == "True":
                #Set cookie username and will expire in 3 days
                responseAdmin.set_cookie('username', username, max_age=3*24*3600)
                responseStaff.set_cookie('username', username, max_age=3*24*3600)
                # print(request.COOKIES.get('username')) print to ensure isit get cookie or not
            #Check user_type
            if user.user_type == "1":
                # Redirect to an admin template.
                return responseAdmin
            elif user.user_type == "2":
                # Redirect to a staff template.
                return responseStaff
        else:
            # Return an 'invalid login' error message.
            messages.error(request, "Username or Password are wrong!")
            return redirect('login')
    else:
        return render(request, 'login.html')

#Logout
def Logout(request):
    response = redirect('login')
    #log out 
    logout(request)
    #Delete cookie if username have stored in cookie after user logged out
    if 'username' in request.COOKIES:
        response.delete_cookie('username')
    messages.success(request, "You were logged out, see you next time!")
    return response

#Forgot password
def ForgotPassword(request):
    return render(request, 'registration/password_reset_form.html')

#Dynamic time
def getTime(request):
    #get local time
    now = datetime.datetime.now()
