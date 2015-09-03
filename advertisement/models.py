from django.db import models
from embed_video.fields import EmbedVideoField
from taggit.managers import TaggableManager

from sponsor.models import Sponsor
from sponsor.models import SponsorManager

# Create your models here.
class Ad(models.Model):
    author = models.ForeignKey(SponsorManager, related_name='ads')
    sponsor = models.ForeignKey(Sponsor, related_name='ads', null=False)
    name = models.CharField(max_length=255)
    video = EmbedVideoField(null=False)
    tags = TaggableManager(blank=True)
