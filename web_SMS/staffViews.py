from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from web_SMS.models import LeaveReportStaff, Staffs, FeedBackStaffs, CustomUser
from django.views.decorators.csrf import csrf_exempt

#Page Index
def Index(request):
    staff = Staffs.objects.get(admin=request.user.id)
    context = {
        'staff' : staff,
    }
    return render(request, 'smsys_staff/index.html', context)

#Page ApplyLeaveStaff
def ApplyLeaveStaff(request):
    staff = Staffs.objects.get(admin=request.user.id)
    context = {
        'staff' : staff,
    }
    return render(request, 'smsys_staff/applyLeaveStaff.html', context)

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
    staff = Staffs.objects.get(admin=request.user.id)
    #Show the Leave Applied History that filter by curret user ID
    leave_data = LeaveReportStaff.objects.filter(staff_id=staff)
    context = {
        'leave_data' : leave_data,
        'staff' : staff,
    }
    return render(request, 'smsys_staff/leaveAppliedHistory.html', context)

#FeedbackStaff
def FeedbackStaff(request):
    staff = Staffs.objects.get(admin=request.user.id)
    context = {
        'staff' : staff,
    }
    return render(request, 'smsys_staff/feedbackStaff.html', context)

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
    staff = Staffs.objects.get(admin=request.user.id)
    #Show the Feedback History Staffs that filter by curret user ID
    feedback_data = FeedBackStaffs.objects.filter(staff_id=staff)
    context = {
        'feedback_data' : feedback_data,
        'staff' : staff,
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

#doEditProfileStaff
def doEditProfileStaff(request):
    if request.method == "POST":
        #Get the field value from user input
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        gender = request.POST.get("gender")
        position = request.POST.get("position")
        telno = request.POST.get("telno")
        address = request.POST.get("address")
        education = request.POST.get("education")
        skills = request.POST.get("skills")
        description = request.POST.get("description")
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
            staff.position = position
            staff.telno = telno
            staff.address = address
            staff.education = education
            staff.skills = skills
            staff.description = description
            staff.save()
            
            messages.success(request, "Profile edited successfully!")
            return redirect('profileStaff')
        except:
            messages.error(request, "Profile edited failure...Please try again.")
            return redirect('profileStaff')
    else:
        return redirect('profileStaff')

#AboutUsStaff
def AboutUsStaff(request):
    staff = Staffs.objects.get(admin=request.user.id)
    context = {
        'staff' : staff,
    }
    return render(request, 'smsys_staff/aboutUsStaff.html', context)