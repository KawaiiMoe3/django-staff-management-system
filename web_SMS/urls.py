from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('index/', views.Index, name='index'),
]