from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
from django.contrib.auth import get_user_model

class MyUserDetailsSerializer(TaggitSerializer, serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'number_ads_viewed', 'number_different_ads_viewed')
        read_only_fields = ('number_ads_viewed',  'number_different_ads_viewed')
