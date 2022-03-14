from unicodedata import name
from django.contrib import admin
from django.urls import path
from web_SMS import adminViews
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Login, name='login'), #login page
    path('doLogin', views.doLogin, name='doLogin'), #data login will submit at this view
    path('logout/', views.Logout, name='logout'), #logout
    path('forgot-password/', views.ForgotPassword, name='forgot-password'),
    path('index/', adminViews.Index, name='index'), #adminViews's index page
    path('add_staff', adminViews.addStaff, name='add_staff'),
    path('contact/', adminViews.Contact, name='contact'), #adminViews's contact page
]