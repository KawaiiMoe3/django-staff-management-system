from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from web_SMS.models import *
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

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

#TakeAttendanceStaff
def TakeAttendanceStaff(request):
    staff = Staffs.objects.get(admin=request.user.id)
    #Get current time
    now = datetime.now()
    #Change the time format
    timeFormat = now.strftime("%d/%m/%Y %H:%M:%S")
    #Create a dictionary
    context = {
        #For Timing
        'year' : now.year,
        'month' : now.month,
        'day' : now.day,
        'hour' : now.hour,
        'min' : now.minute,
        'sec' : now.second,
        'staff' : staff,
    }
    return render(request, 'smsys_staff/takeAttendanceStaff.html', context)

#doClockInStaff
def doClockInStaff(request):
    if request.method == "POST":
        #Get the attendance date from user input
        attendance_date = request.POST.get("attendance_date")
        #Accessing the current user ID 
        staff_id = Staffs.objects.get(admin=request.user.id)
        try:
            #Passing the value to AttendanceReport model
            attendance_report = AttendanceReport(attendance_date=attendance_date,status="1", staff_id=staff_id)
            attendance_report.save()
            messages.success(request, "Clock in successfully!")
            return redirect('takeAttendanceStaff')
        except:
            messages.error(request, "Somethings error...Please try again.")
            return redirect('takeAttendanceStaff')
    else:
        return redirect('takeAttendanceStaff')

#AttendanceRecordStaff
def AttendanceRecordStaff(request):
    staff = Staffs.objects.get(admin=request.user.id)
    #Show the AttendanceReport that filter by curret user ID
    attendance_data = AttendanceReport.objects.filter(staff_id=staff)

    #Show the specify attendance data by start and end date if fetch button pressed, else show all the attendance data
    if request.method == "POST":
        #Get Start and End date from user's input
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')

        #Fetch attendance report data using raw('SQL statement') from AttendanceReport model that filter by staff ID
        fetchData = AttendanceReport.objects.filter(staff_id=staff).raw('SELECT * FROM web_sms_attendancereport WHERE attendance_date BETWEEN "'+startDate+'" AND "'+endDate+'"')
        
        #Create a dictionary
        context = {
            'staff' : staff,
            'attendance_data' : fetchData,
        }
        return render(request, 'smsys_staff/attendanceRecord.html', context)
    else:
        context = {
            'staff' : staff,
            'attendance_data' : attendance_data,
        }
        return render(request, 'smsys_staff/attendanceRecord.html', context)

#doClockOutStaff
def doClockOutStaff(request, attendance_id):
    #Get the attendance data by ID from AttendanceReport model's objects
    attendance_report = AttendanceReport.objects.get(id=attendance_id)
    #Change the status to Clocked Out (2) and update clock out timing
    attendance_report.status = 2
    attendance_report.updated_at = datetime.now()
    attendance_report.save()
    return redirect('attendanceRecordStaff')

#Todo
def TodoList(request):
    #Get the current staff ID
    staff = Staffs.objects.get(admin=request.user.id)
    #Filter task by staff ID
    tasks = TodoTask.objects.filter(staff_id=staff)
    #Count all the incomplete tasks 
    incompleteTaskCount = TodoTask.objects.filter(staff_id=staff, complete=False).count()

    #Create a dictionary
    context = {
        'staff' : staff,
        'tasks' : tasks,
        'incompleteTaskCount' : incompleteTaskCount,
    }
    return render(request, 'smsys_staff/todoList.html', context)

#doAddTask
def doAddTask(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        complete = request.POST.get("complete")

        #Accessing the current user ID 
        staff_id = Staffs.objects.get(admin=request.user.id)
        
        try:
            #Check whether complete checkbox is checked or not
            if complete == "True":
                completeIsChecked = complete
            else:
                completeIsChecked = False
            #Passing the value from TodoTask model
            todoTask = TodoTask(staff_id=staff_id, title=title, description=description, complete=completeIsChecked)
            todoTask.save()
            return redirect('todoList')
        except:
            return redirect('todoList')
    else:
        return redirect('todoList')

#doEditTask
def doEditTask(request, task_id):
    pass

#doDeleteTask
def doDeleteTask(request, task_id):
    #Get the task ID from TodoTask models
    task = TodoTask.objects.get(id=task_id)
    #Delete the following task
    task.delete()
    return redirect('todoList')