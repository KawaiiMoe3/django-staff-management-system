#create adminViews
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from web_SMS.models import CustomUser, Staffs
from django.core.files.storage import FileSystemStorage

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

        profile_pic = request.FILES['profile_pic']
        # create a new instance of FileSystemStorage
        fs = FileSystemStorage()
        filename = fs.save(profile_pic.name, profile_pic)
        # the fileurl variable now contains the url to the file. This can be used to serve the file when needed.
        profile_pic_url = fs.url(filename)

        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, user_type=2)
            user.staffs.gender = gender
            user.staffs.telno = telno
            user.staffs.address = address
            user.staffs.profile_pic = profile_pic_url
            user.save()
            messages.success(request, "Staff added successfully!")
            return redirect('add_staff')
        except:
            messages.error(request, "Staff added failure...Please try again.")
            return redirect('add_staff')
    else:
        return HttpResponse("Method not allowed")

#Page List staff
def listStaff(request):
    #Get all the objects of staffs
    staffs = Staffs.objects.all()
    #Passing the Staffs objects to Dictionary
    context = {
        'staffs' : staffs
    }
    return render(request, 'smsys_admin/listStaff.html', context)

#Page Edit staff
def editStaff(request, staff_id):
    staff = Staffs.objects.get(admin=staff_id)
    context = {
        'staff' : staff,
        'id' : staff_id,
    }
    return render(request, 'smsys_admin/editStaff.html', context)

#Do edit staff
def doEditStaff(request):
    if request.method == "POST":
        staff_id = request.POST.get("staff_id")
        username = request.POST.get('username')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        telno = request.POST.get('telno')
        address = request.POST.get('address')

        #Save a new picture if file is selected, else will not update old picture
        if request.FILES.get('profile_pic', False):
            profile_pic = request.FILES['profile_pic']
            # create a new instance of FileSystemStorage
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            # the fileurl variable now contains the url to the file. This can be used to serve the file when needed.
            profile_pic_url = fs.url(filename)
        else:
            profile_pic_url = None

        try:
            user = CustomUser.objects.get(id=staff_id)
            user.username = username
            user.email = email
            user.save()

            staff_model = Staffs.objects.get(admin=staff_id)
            staff_model.gender = gender
            staff_model.telno = telno
            staff_model.address = address
            #If file is selected, save a new picture
            if profile_pic_url != None:
                staff_model.profile_pic = profile_pic_url
            staff_model.save()

            messages.success(request, "Staff edited successfully!")
            return redirect('edit_staff/'+staff_id)
        except:
            messages.error(request, "Staff edited failure...Please try again.")
            return redirect('edit_staff/'+staff_id)
    else:
        return HttpResponse("Method not allowed!")

#Page Contact
def Contact(request):
    return render(request, 'smsys_admin/contact.html')