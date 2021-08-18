from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
# admin.site.register(MyUser, UserAdmin)

@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    ordering = ('-created',)
    list_display = ('email', 'first_name', 'last_name', 'created', 'modified', 'last_login', 'is_staff')