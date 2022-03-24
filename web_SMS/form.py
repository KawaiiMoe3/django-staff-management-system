from django import forms

#Create AddStaffForm for addStaff.html
class AddStaffForm(forms.Form):
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter username", "autocomplete":"off"}))
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"Enter password"}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"class":"form-control", "placeholder":"Enter email", "autocomplete":"off"}))
    gender_choice = [
        ('Male','Male'),
        ('Female','Female')
    ]
    gender = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=gender_choice))
    telno = forms.RegexField(label="Telno", regex='^(\+?6?01)[02-46-9]-*[0-9]{7}$|^(\+?6?01)[1]-*[0-9]{8}$', widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter telno, exp:+60,60,0123456789"}))
    address = forms.CharField(label="Address", max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter address"}))
    profile_pic = forms.FileField(label="Profile Image", max_length=50,widget=forms.FileInput(attrs={"class":"form-control"}))

#Create EditStaffForm for editStaff.html
class EditStaffForm(forms.Form):
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter username"}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"class":"form-control", "placeholder":"Enter email"}))
    gender_choice = [
        ('Male','Male'),
        ('Female','Female')
    ]
    gender = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=gender_choice))
    telno = forms.RegexField(label="Telno", regex='^(\+?6?01)[02-46-9]-*[0-9]{7}$|^(\+?6?01)[1]-*[0-9]{8}$', widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter telno, exp:+60,60,0123456789"}))
    address = forms.CharField(label="Address", max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter address"}))
    profile_pic = forms.FileField(label="Profile Image", max_length=50,widget=forms.FileInput(attrs={"class":"form-control"}), required=False)