from django.db import models
from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager

from advertisement.models import Ad

class User(AbstractUser):
    interest = TaggableManager(blank=True)
    ads_viewed = models.ManyToManyField(Ad, blank=True, related_name="viewers", related_query_name="viewer")
    def number_ads_viewed(self):
        return self.ads_viewed.count()
