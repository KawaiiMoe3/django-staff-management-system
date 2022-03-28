#create adminViews
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect, render
from django.contrib import messages
from web_SMS.form import AddStaffForm, EditStaffForm
from web_SMS.models import CustomUser, LeaveReportStaff, Staffs, FeedBackStaffs
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt

#Page Index
def Index(request):
    return render(request, 'smsys_admin/index.html')

#Page addStaff
def addStaff(request):
    #Get the AddStaffForm() model
    form = AddStaffForm()
    context = {
        'form' : form
    }
    return render(request, 'smsys_admin/addStaff.html', context)

#Do add staff
def doAddStaff(request):
    if request.method == "POST":
        #Get the AddStaffForm() model
        form = AddStaffForm(request.POST, request.FILES)
        #Check whether user's input is valid or not
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            gender = form.cleaned_data['gender']
            telno = form.cleaned_data['telno']
            address = form.cleaned_data['address']

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
            form = AddStaffForm(request.POST)
            context = {
                'form' : form
            }
            return render(request, 'smsys_admin/addStaff.html', context)
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
    #Add ID into session
    #Store the staff_id into Session in Backend when admin edit staff before showing the data into form
    request.session['staff_id'] = staff_id
    staff = Staffs.objects.get(admin=staff_id)
    form = EditStaffForm()
    form.fields['username'].initial = staff.admin.username
    form.fields['email'].initial = staff.admin.email
    form.fields['gender'].initial = staff.gender
    form.fields['telno'].initial = staff.telno
    form.fields['address'].initial = staff.address
    form.fields['profile_pic'].initial = staff.profile_pic
    context = {
        'form' : form,
        'id' : staff_id,
        'username' : staff.admin.username,
    }
    return render(request, 'smsys_admin/editStaff.html', context)

#Do edit staff
def doEditStaff(request):
    if request.method == "POST":
        #staff_id come from which stored in the session
        staff_id = request.session.get("staff_id")
        #Check whether staff_id is exists or not
        if staff_id == None:
            return redirect('list_staff')
        
        #Get the EditStaffForm() model
        form = EditStaffForm(request.POST, request.FILES)
        #Check whether user's input is valid or not
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            gender = form.cleaned_data['gender']
            telno = form.cleaned_data['telno']
            address = form.cleaned_data['address']

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
                #Deleting the staff_id from session after staff edited
                del request.session['staff_id']
                messages.success(request, "Staff edited successfully!")
                return redirect('edit_staff/'+staff_id)
            except:
                messages.error(request, "Staff edited failure...Please try again.")
                return redirect('edit_staff/'+staff_id)
        else:
            form = EditStaffForm(request.POST)
            staff = Staffs.objects.get(admin=staff_id)
            context = {
                'form' : form,
                'id' : staff_id,
                'username' : staff.admin.username,
            }
            return render(request, 'smsys_admin/editStaff.html', context)
    else:
        return HttpResponse("Method not allowed!")

#Page Contact
def Contact(request):
    return render(request, 'smsys_admin/contact.html')

#checkEmailExist
@csrf_exempt #Ajax request work without csrf_token
def checkEmailExist(request):
    email = request.POST.get("email")
    #filter email check isit any email exists
    user_obj = CustomUser.objects.filter(email=email).exists()
    #Checking if object is not false then return true, else false
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

#checkUsernameExist
@csrf_exempt #Ajax request work without csrf_token
def checkUsernameExist(request):
    username = request.POST.get("username")
    #filter email check isit any username exists
    user_obj = CustomUser.objects.filter(username=username).exists()
    #Checking if object is not false then return true, else false
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

#FeedbackMessage 
def FeedbackMessage(request):
    #Get all the element of FeedBackStaffs model
    messages = FeedBackStaffs.objects.all()
    context = {
        'messages' : messages,
    }
    return render(request, 'smsys_admin/feedback_message.html', context)

#FeedbackMessageReply
@csrf_exempt #Ajax request work without csrf_token
def FeedbackMessageReply(request):
    #Get id and reply_message from user input
    feedback_id = request.POST.get("reply_id")
    reply_message = request.POST.get("reply_message")

    try:
        feedback = FeedBackStaffs.objects.get(id=feedback_id)
        feedback.feedback_reply = reply_message
        feedback.save()
        return HttpResponse("True")
    except:
        return HttpResponse("False")

#ViewStaffLeave
def ViewStaffLeave(request):
    #Get all the LeaveReportStaff model's objects
    leaves = LeaveReportStaff.objects.all()
    #Create a dictionary
    context = {
        "leaves" : leaves,
    }
    return render(request, 'smsys_admin/viewStaffLeave.html', context)

#doApproveStaffLeave
def doApproveStaffLeave(request, leave_id):
    #Get the leave data by ID from LeaveReportStaff model's objects
    leave = LeaveReportStaff.objects.get(id=leave_id)
    #Change the leave_status to Approved (1)
    leave.leave_status = 1
    leave.updated_at = datetime.now()
    leave.save()
    return redirect('viewStaffLeave')

#doApproveStaffLeave
def doRejectStaffLeave(request, leave_id):
    #Get the leave data by ID from LeaveReportStaff model's objects
    leave = LeaveReportStaff.objects.get(id=leave_id)
    #Change the leave_status to Rejected (2)
    leave.leave_status = 2
    leave.updated_at = datetime.now()
    leave.save()
    return redirect('viewStaffLeave')

#profileAdmin
def editProfileAdmin(request):
    #Get id from CustomUser model
    user = CustomUser.objects.get(id=request.user.id)
    #Create a dictionary
    context = {
        'user' : user,
    }
    return render(request, 'smsys_admin/edit_profile_admin.html', context)

#doEditProfileAdmin
def doEditProfileAdmin(request):
    if request.method == "POST":
        #Get the field value from user input
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.username = username
            customuser.email = email
            #Change password if password field is not none and empty
            if password != None and password != "":
                customuser.set_password(password)
            customuser.save()
            messages.success(request, "Profile edited successfully!")
            return redirect('editProfileAdmin')
        except:
            messages.error(request, "Profile edited failure...Please try again.")
            return redirect('editProfileAdmin')
    else:
        return redirect('editProfileAdmin')