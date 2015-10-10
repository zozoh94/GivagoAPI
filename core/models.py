from django.db import models
from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager

class User(AbstractUser):
    interest = TaggableManager(blank=True)
    def number_ads_viewed(self):
        return self.ads_viewed.count()        
    def number_different_ads_viewed(self):
        return self.ads_viewed.values('ad').distinct().count()
