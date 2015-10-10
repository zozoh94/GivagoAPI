from django.contrib import admin

from .models import Gift
from .models import ONG

class GiftAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Gift, GiftAdmin)
admin.site.register(ONG)
