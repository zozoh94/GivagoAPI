from django.contrib import admin

from .models import Ad

class AdAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'sponsor')
    search_fields = ('name', 'author', 'sponsor')

admin.site.register(Ad, AdAdmin)
