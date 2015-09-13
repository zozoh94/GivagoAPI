from django.contrib import admin

from .models import Gift

class GiftAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Gift, GiftAdmin)
