from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MvUser

# Register your models here.

admin.site.register(MvUser, UserAdmin)