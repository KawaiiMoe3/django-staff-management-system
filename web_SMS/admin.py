from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from web_SMS.models import CustomUser

# Register your models here.

#Create blank UserModel for password encrypted, if not, password will not encrypted
class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser, UserModel)