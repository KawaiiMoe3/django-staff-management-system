#create adminViews
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from web_SMS.models import CustomUser, Staffs

#Page Index
def Index(request):
    return render(request, 'smsys_admin/index.html')

#Page addStaff
def addStaff(request):
    return render(request, 'smsys_admin/addStaff.html')

#Do add staff
def doAddStaff(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        telno = request.POST.get('telno')
        address = request.POST.get('address')
        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, user_type=2)
            user.staffs.gender = gender
            user.staffs.telno = telno
            user.staffs.address = address
            user.staffs.profile_pic = ""
            user.save()
            messages.success(request, "Staff added successfully!")
            return redirect('add_staff')
        except:
            messages.error(request, "Staff added failure...Please try again.")
            return redirect('add_staff')
    else:
        return HttpResponse("Method not allowed")

#Page Contact
def Contact(request):
    return render(request, 'smsys_admin/contact.html')