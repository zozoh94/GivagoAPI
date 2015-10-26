from django.contrib import admin
from .models import User, Staff
from django.contrib.auth.admin import UserAdmin

class MyUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('interest',)}),
    )

class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'position')
    list_display_links = ('first_name', 'position')
    search_fields =  ('first_name', 'position')
    
admin.site.register(User, MyUserAdmin)
admin.site.register(Staff, StaffAdmin)
