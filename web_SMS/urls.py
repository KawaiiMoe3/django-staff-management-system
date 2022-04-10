from django.contrib import admin
from django.urls import path, include
from web_SMS import adminViews, staffViews
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.Login, name='login'), #login page
    path('doLogin', views.doLogin, name='doLogin'), #data login will submit at this view
    path('logout/', views.Logout, name='logout'), #logout
    path('forgot-password/', views.ForgotPassword, name='forgot-password'),
    #For adminViews:
    path('index/', adminViews.Index, name='index'), 
    path('add_staff', adminViews.addStaff, name='add_staff'),
    path('doAddStaff', adminViews.doAddStaff, name='doAddStaff'),
    path('list_staff', adminViews.listStaff, name='list_staff'),
    path('edit_staff/<str:staff_id>', adminViews.editStaff, name='edit_staff'),
    path('doEditStaff', adminViews.doEditStaff, name='doEditStaff'),
    path('contact/', adminViews.Contact, name='contact'), 
    path('check-email-exist', adminViews.checkEmailExist, name='checkEmailExist'), 
    path('check-username-exist', adminViews.checkUsernameExist, name='checkUsernameExist'), 
    path('feedback-message', adminViews.FeedbackMessage, name='feedbackMessage'), 
    path('feedback-message-reply', adminViews.FeedbackMessageReply, name='feedbackMessageReply'), 
    path('view-staff-leave', adminViews.ViewStaffLeave, name='viewStaffLeave'),
    path('doApproveStaffLeave/<str:leave_id>', adminViews.doApproveStaffLeave, name='doApproveStaffLeave'),
    path('doRejectStaffLeave/<str:leave_id>', adminViews.doRejectStaffLeave, name='doRejectStaffLeave'),
    path('edit-profile-admin', adminViews.editProfileAdmin, name='editProfileAdmin'),
    path('doEditProfileAdmin', adminViews.doEditProfileAdmin, name='doEditProfileAdmin'),
    path('staff-profile', adminViews.StaffProfile, name='staffProfile'),
    path('viewStaffProfile/<str:staff_id>', adminViews.ViewStaffProfile, name='viewStaffProfile'),
    path('doEditProfileStaffByAdmin', adminViews.doEditProfileStaffByAdmin, name='doEditProfileStaffByAdmin'),
    path('about-us', adminViews.AboutUsAdmin, name='aboutUsAdmin'),
    path('attendance-record', adminViews.AttendanceRecord, name='attendanceRecord'),
    #For staffViews:
    path('index', staffViews.Index, name='index_staff'),
    path('apply-leave', staffViews.ApplyLeaveStaff, name='applyLeaveStaff'),
    path('doApplyLeaveStaff', staffViews.doApplyLeaveStaff, name='doApplyLeaveStaff'),
    path('leave-applied-history', staffViews.LeaveAppliedHistory, name='leaveAppliedHistory'),
    path('feedback', staffViews.FeedbackStaff, name='feedbackStaff'),
    path('doFeedbackStaff', staffViews.doFeedbackStaff, name='doFeedbackStaff'),
    path('feedback-history-staff', staffViews.FeedbackHistoryStaffs, name='feedbackHistoryStaffs'),
    path('profile-staff', staffViews.profileStaff, name='profileStaff'),
    path('doEditProfileStaff', staffViews.doEditProfileStaff, name='doEditProfileStaff'),
    path('about-us-staff', staffViews.AboutUsStaff, name='aboutUsStaff'),
    path('take-attendance-staff', staffViews.TakeAttendanceStaff, name='takeAttendanceStaff'),
    path('doClockInStaff', staffViews.doClockInStaff, name='doClockInStaff'),
    path('doClockOutStaff/<str:attendance_id>', staffViews.doClockOutStaff, name='doClockOutStaff'),
    path('attendance-record-staff', staffViews.AttendanceRecordStaff, name='attendanceRecordStaff'),
    path('todo-list', staffViews.TodoList, name='todoList'),
    path('doAddTask', staffViews.doAddTask, name='doAddTask'),
    path('doEditTask/<str:task_id>', staffViews.doEditTask, name='doEditTask'),
    path('doDeleteTask/<str:task_id>', staffViews.doDeleteTask, name='doDeleteTask'),
]