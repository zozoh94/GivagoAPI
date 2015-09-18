from django.db import models
from embed_video.fields import EmbedVideoField
from taggit.managers import TaggableManager
from django_random_queryset import RandomManager

from sponsor.models import Sponsor
from sponsor.models import SponsorManager

# Create your models here.
class Ad(models.Model):
    objects = RandomManager()
    author = models.ForeignKey(SponsorManager, related_name='ads', null=True,
                               on_delete=models.SET_NULL)
    sponsor = models.ForeignKey(Sponsor, related_name='ads', null=False)
    name = models.CharField(max_length=255)
    video = EmbedVideoField(null=False)
    tags = TaggableManager(blank=True)
