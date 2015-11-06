from rest_framework import serializers
from embed_video.backends import detect_backend
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
from django.utils.translation import ugettext_lazy as _

from .models import Ad
from .models import App
from sponsor.models import Sponsor
from sponsor.models import SponsorManager
from sponsor.serializers import SponsorSerializer

class VideoSerializer(serializers.BaseSerializer):
    def to_representation(self, obj):
        video = detect_backend(obj)
        return {
            'url': obj,
            'url_embed': video.get_url(),
            'thumbnail': video.get_thumbnail_url()
        }
    def to_internal_value(self, data):
        try:
            backend = detect_backend(url)
            backend.get_code()
        except UnknownBackendException:
            raise serializers.ValidationError(_(u'URL could not be recognized.'))
        except UnknownIdException:
            raise serializers.ValidationError(_(u'ID of this video could not be '
                                          u'recognized.'))
        return data
    
class AdSerializer(TaggitSerializer, serializers.ModelSerializer):
    video = VideoSerializer(required=True)
    author = serializers.ReadOnlyField(source='author.user.username')
    sponsor_url = serializers.HyperlinkedRelatedField(view_name='sponsor-detail', read_only=True, source='sponsor')
    sponsor = serializers.PrimaryKeyRelatedField(queryset=Sponsor.objects.all(), write_only=True, required=True)
    tags = TagListSerializerField(required=False, read_only=True)
    class Meta:
        model = Ad
        fields = ('id', 'url', 'name', 'video', 'author', 'sponsor', 'sponsor_url', 'tags')
    def validate_sponsor(self, value):
        if value is not None:
            try:
                manager_in_sponsor = value.managers.all()
            except SponsorManager.DoesNotExist:
                raise serializers.ValidationError("Sponsor don't have any manager.")
            try:
                current_manager = self.context['request'].user.sponsormanager
            except SponsorManager.DoesNotExist:
                raise serializers.ValidationError("You're not a manager.")
            if current_manager in manager_in_sponsor or self.context['request'].user.is_superuser:
                return value
            else:
                raise serializers.ValidationError("You can't assign this sponsor to the advertisement. You're not a manager of this sponsor.")
        else:
            return value

class AdDetailSerializer(AdSerializer):
    sponsor_detail = SponsorSerializer(read_only=True, source='sponsor')
    class Meta:
        model = Ad
        fields = ('url', 'name', 'video', 'author', 'sponsor', 'sponsor_detail', 'tags', 'number_views', 'number_views_different_user')

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('id', 'name', 'link', 'thumbnail')
