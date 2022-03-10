from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#Page Index
def Index(request):
    return render(request, 'index.html')

#Page Login
def Login(request):
    return render(request, 'login.html')