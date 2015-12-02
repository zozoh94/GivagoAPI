from django.contrib import admin

from .models import Ad
from .models import View
from .models import App
from .models import AppClick

class AdAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'sponsor', 'remaining_views')
    search_fields = ('name', 'sponsor__name')

class ViewAdmin(admin.ModelAdmin):
    list_display = ('ad', 'viewer', 'ong', 'date', 'type')
    list_display_links = ('ad', 'viewer', 'ong', 'date')
    search_fields = ('ad__name', 'viewer__username', 'ong__name')
    list_filter = ('date', 'type')

class AppAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'os', 'country')
    search_fields = ('name',)
    list_filter = ('os', 'country')

class AppClickAdmin(admin.ModelAdmin):
    list_display = ('app', 'viewer', 'ong', 'date', 'installed', 'date_installed')
    search_fields = ('ad__name', 'viewer__username', 'ong__name')
    list_filter = ('date', 'date_installed', 'installed')


admin.site.register(Ad, AdAdmin)
admin.site.register(View, ViewAdmin)
admin.site.register(App, AppAdmin)
admin.site.register(AppClick, AppClickAdmin)
