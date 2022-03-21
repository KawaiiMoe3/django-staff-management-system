from django.contrib import admin
from django.urls import path
from web_SMS import adminViews, staffViews
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Login, name='login'), #login page
    path('doLogin', views.doLogin, name='doLogin'), #data login will submit at this view
    path('logout/', views.Logout, name='logout'), #logout
    path('forgot-password/', views.ForgotPassword, name='forgot-password'),
    #For adminViews:
    path('index/', adminViews.Index, name='index'), 
    path('add_staff', adminViews.addStaff, name='add_staff'),
    path('doAddStaff', adminViews.doAddStaff, name='doAddStaff'),
    path('list_staff', adminViews.listStaff, name='list_staff'),
    path('edit_staff/<str:staff_id>', adminViews.editStaff, name='edit_staff'),
    path('doEditStaff', adminViews.doEditStaff, name='doEditStaff'),
    path('contact/', adminViews.Contact, name='contact'), 
    #For staffViews:
    path('index', staffViews.Index, name='index_staff'),
    path('contact', staffViews.Contact, name='contact_staff'),
]