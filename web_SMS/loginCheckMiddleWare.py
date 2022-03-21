from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

#Create LoginCheckMiddleWare()
class LoginCheckMiddleWare(MiddlewareMixin):

    def process_view(self, request, view_func, view_args, view_kwargs):
        #modulename is file name where our request has been sent to which file
        modulename = view_func.__module__
        #Accessing logged in user data from request user and storing into user variable
        user = request.user
        #Check whether user is logged in or not 
        if user.is_authenticated:
            #If user_type = 1 (admin) then can access function of adminViews.py and views.py
            if user.user_type == "1":
                if modulename == "web_SMS.adminViews":
                    pass
                elif modulename == "web_SMS.views":
                    pass
                else:
                    return redirect('index')
            #If user_type = 2 (staff) then can only access function of staffViews.py and views.py
            elif user.user_type == "2":
                if modulename == "web_SMS.staffViews":
                    pass
                elif modulename == "web_SMS.views":
                    pass
                else:
                    return redirect('index_staff')
            else:
                return redirect('login')
        else:
            #Check if user is accessing login page then no need do anything, else will redirect to login page
            if request.path == reverse("login") or request.path == reverse("doLogin") or request.path == reverse("forgot-password"):
                pass
            else:
                return redirect('login')
