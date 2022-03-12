from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('forgot-password/', views.ForgotPassword, name='forgot-password'),
    path('index/', views.Index, name='index'),
    path('contact/', views.Contact, name='contact'),
]