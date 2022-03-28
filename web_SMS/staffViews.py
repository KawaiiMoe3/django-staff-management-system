from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from web_SMS.models import LeaveReportStaff, Staffs, FeedBackStaffs, CustomUser
from django.views.decorators.csrf import csrf_exempt

#Page Index
def Index(request):
    return render(request, 'smsys_staff/index.html')

#Page Contact
def Contact(request):
    return render(request, 'smsys_staff/contact.html')

#Page ApplyLeaveStaff
def ApplyLeaveStaff(request):
    return render(request, 'smsys_staff/applyLeaveStaff.html')

# doApplyLeaveStaff
def doApplyLeaveStaff(request):
    if request.method == "POST":
        leave_date = request.POST.get("leave_date")
        leave_message = request.POST.get("leave_message")

        #Accessing the current user ID 
        staff_obj = Staffs.objects.get(admin=request.user.id)
        try:
            #Passing the value from LeaveReportStaff model
            leave_report = LeaveReportStaff(staff_id=staff_obj, leave_date=leave_date, leave_message=leave_message, leave_status=0)
            leave_report.save()
            messages.success(request, "Leave applied successfully!")
            return redirect('applyLeaveStaff')
        except:
            messages.error(request, "Leave applied failure...Please try again.")
            return redirect('applyLeaveStaff')
    else:
        return redirect('applyLeaveStaff')

#Page Leave Applied History
def LeaveAppliedHistory(request):
    #Accessing the current user ID 
    staff_obj = Staffs.objects.get(admin=request.user.id)
    #Show the Leave Applied History that filter by curret user ID
    leave_data = LeaveReportStaff.objects.filter(staff_id=staff_obj)
    context = {
        'leave_data' : leave_data,
    }
    return render(request, 'smsys_staff/leaveAppliedHistory.html', context)

#FeedbackStaff
def FeedbackStaff(request):
    return render(request, 'smsys_staff/feedbackStaff.html')

# doApplyLeaveStaff
def doFeedbackStaff(request):
    if request.method == "POST":
        feedback = request.POST.get("feedback")

        #Accessing the current user ID 
        staff_id = Staffs.objects.get(admin=request.user.id)
        
        try:
            #Passing the value from FeedbackStaff model
            feedbackStaff = FeedBackStaffs(staff_id=staff_id, feedback=feedback, feedback_reply="")
            feedbackStaff.save()
            messages.success(request, "Feedback sent successfully!")
            return redirect('feedbackStaff')
        except:
            messages.error(request, "Feedback sent failure...Please try again.")
            return redirect('feedbackStaff')
    else:
        return redirect('feedbackStaff')

#FeedbackHistoryStaff
def FeedbackHistoryStaffs(request):
    #Accessing the current user ID 
    staff_id = Staffs.objects.get(admin=request.user.id)
    #Show the Feedback History Staffs that filter by curret user ID
    feedback_data = FeedBackStaffs.objects.filter(staff_id=staff_id)
    context = {
        'feedback_data' : feedback_data,
    }
    return render(request, 'smsys_staff/feedbackHistoryStaff.html', context)

#profileStaff
def profileStaff(request):
    #Get id from CustomUser model
    user = CustomUser.objects.get(id=request.user.id)
    staff = Staffs.objects.get(admin=user)
    #Create a dictionary
    context = {
        'user' : user,
        'staff' : staff,
    }
    return render(request, 'smsys_staff/profile_staff.html', context)

#doEditProfileAdmin
def doEditProfileStaff(request):
    if request.method == "POST":
        #Get the field value from user input
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        gender = request.POST.get("gender")
        telno = request.POST.get("telno")
        address = request.POST.get("address")
        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.username = username
            customuser.email = email
            #Change password if password field is not none and empty
            if password != None and password != "":
                customuser.set_password(password)
            customuser.save()

            staff = Staffs.objects.get(admin=customuser.id)
            staff.gender = gender
            staff.telno = telno
            staff.address = address
            staff.save()
            
            messages.success(request, "Profile edited successfully!")
            return redirect('profileStaff')
        except:
            messages.error(request, "Profile edited failure...Please try again.")
            return redirect('profileStaff')
    else:
        return redirect('profileStaff')

#checkEmailExist
@csrf_exempt #Ajax request work without csrf_token
def checkEmailExistStaff(request):
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
def checkUsernameExistStaff(request):
    username = request.POST.get("username")
    #filter email check isit any username exists
    user_obj = CustomUser.objects.filter(username=username).exists()
    #Checking if object is not false then return true, else false
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)