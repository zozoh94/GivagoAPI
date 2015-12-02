from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from .resources import UserResource
from import_export.admin import ExportMixin

class MyUserAdmin(ExportMixin, UserAdmin):
    resource_class = UserResource
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('interest', 'date_birth', 'gender', 'income_level', 'avatar')}),
    )
    
admin.site.register(User, MyUserAdmin)
