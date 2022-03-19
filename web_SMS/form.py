from django import forms

#Create addStaffForm
class addStaffForm(forms.Form):
    username = forms.CharField(label="Username", max_length=50)
    password = forms.CharField(label="Password", max_length=50)
    email = forms.CharField(label="Email", max_length=50)
    gender = forms.CharField(label="Gender", max_length=50)
    telno = forms.CharField(label="Telno", max_length=50)
    address = forms.CharField(label="Address", max_length=50)
    profile_pic = forms.CharField(label="Profile Image", max_length=50)