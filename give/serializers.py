from rest_framework import serializers

from .models import Gift

class GiftSerializer(serializers.ModelSerializer):
    credits = serializers.IntegerField(write_only=True)
    class Meta:
        model = Gift
        fields = ('id', 'name', 'credits')
