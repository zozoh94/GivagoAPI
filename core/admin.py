from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

class MyUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('interest',)}),
    )

admin.site.register(User, MyUserAdmin)
