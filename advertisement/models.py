from django.db import models
from embed_video.fields import EmbedVideoField
from taggit.managers import TaggableManager
from django_random_queryset import RandomManager
from django.conf import settings

from sponsor.models import Sponsor
from sponsor.models import SponsorManager
from give.models import ONG

class Ad(models.Model):
    objects = RandomManager()
    author = models.ForeignKey(SponsorManager, related_name='ads', null=True,
                               on_delete=models.SET_NULL)
    sponsor = models.ForeignKey(Sponsor, related_name='ads', null=False)
    name = models.CharField(max_length=255)
    video = EmbedVideoField(null=False)
    tags = TaggableManager(blank=True)
    remaining_views = models.IntegerField(default=0, null=False)
    def number_views(self):
        return self.views.count()
    def number_views_different_user(self):
        return self.views.values('viewer').distinct().count()    
    def __str__(self):
        return self.name

class View(models.Model):
    AD_TYPE = 1
    ad = models.ForeignKey(Ad, related_name='views')
    viewer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='ads_viewed')
    ong = models.ForeignKey(ONG, related_name='ads_gift')
    date = models.DateTimeField(auto_now_add = True)
    type = models.SmallIntegerField(null=False)
