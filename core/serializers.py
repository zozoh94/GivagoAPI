from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
from django.contrib.auth import get_user_model

class MyUserDetailsSerializer(TaggitSerializer, serializers.ModelSerializer):
    interest = TagListSerializerField(required=False)
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'interest', 'number_ads_viewed')
        read_only_fields = ('email', 'interest', 'number_ads_viewed')
