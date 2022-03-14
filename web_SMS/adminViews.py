#create adminViews
from django.shortcuts import render

#Page Index
def Index(request):
    return render(request, 'smsys_admin/index.html')

#Page addStaff
def addStaff(request):
    return render(request, 'smsys_admin/addStaff.html')

#Page Contact
def Contact(request):
    return render(request, 'smsys_admin/contact.html')