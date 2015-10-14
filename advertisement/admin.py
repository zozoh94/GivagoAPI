from django.contrib import admin

from .models import Ad
from .models import View

class AdAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'sponsor')
    search_fields = ('name', 'sponsor__name')

class ViewAdmin(admin.ModelAdmin):
    list_display = ('ad', 'viewer', 'ong', 'date', 'type_name')
    list_display_links = ('ad', 'viewer', 'ong', 'date')
    search_fields = ('ad__name', 'viewer__username', 'ong__name')
    list_filter = ('date',)
   
admin.site.register(Ad, AdAdmin)
admin.site.register(View, ViewAdmin)
