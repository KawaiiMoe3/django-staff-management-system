from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages

#Page Index
def Index(request):
    return render(request, 'smsys_staff/index.html')

#Page Contact
def Contact(request):
    return render(request, 'smsys_staff/contact.html')