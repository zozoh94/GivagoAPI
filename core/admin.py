from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    can_delete = False
    verbose_name_plural = 'user'

admin.site.register(User, UserAdmin)
