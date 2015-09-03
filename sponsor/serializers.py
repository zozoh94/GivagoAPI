from rest_framework import serializers

from .models import Sponsor
from .models import SponsorManager

class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('name', 'description', 'logo', 'youtube', 'facebook', 'twitter', 'flickr', 'linkedin')

    
