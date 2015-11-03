from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
from django.contrib.auth import get_user_model

class MyUserDetailsSerializer(TaggitSerializer, serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'date_birth', 'gender', 'income_level', 'avatar', 'interests', 'number_ads_viewed', 'number_different_ads_viewed', 'number_app_installed')
        read_only_fields = ('email', 'interest', 'number_ads_viewed',  'number_different_ads_viewed', 'number_app_installed')

class ContactFormSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.RegexField("^\+(?:[0-9] ?){6,14}[0-9]$")

class CharityContactFormSerializer(ContactFormSerializer):
    charity_name = serializers.CharField()
    position = serializers.CharField()
    comment = serializers.CharField(required=False)

class SponsorContactFormSerializer(ContactFormSerializer):
    company_name = serializers.CharField()
    position = serializers.CharField()
    comment = serializers.CharField(required=False)
    budget = serializers.IntegerField(required=False)

class CommunityContactFormSerializer(ContactFormSerializer):
    comment = serializers.CharField()
