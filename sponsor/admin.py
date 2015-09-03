from django.contrib import admin

from .models import Sponsor
from .models import SponsorManager

class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Define a new User admin
class SponsorManagerAdmin(admin.ModelAdmin):
    list_display = ('user', 'sponsor')
    search_fields = ('sponsor__name', 'user')
    
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(SponsorManager, SponsorManagerAdmin)
