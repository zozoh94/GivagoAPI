from django.contrib import admin

from .models import Sponsor
from .models import SponsorManager

class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')

# Define a new User admin
class SponsorManagerAdmin(admin.ModelAdmin):
    list_display = ('user', 'sponsor')
    search_fields = ('sponsor__name', 'user__username')
    
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(SponsorManager, SponsorManagerAdmin)
