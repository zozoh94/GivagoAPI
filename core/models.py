from django.db import models
from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager

class User(AbstractUser):
    interest = TaggableManager(blank=True)
    def number_ads_viewed(self):
        return self.ads_viewed.count()        
    def number_different_ads_viewed(self):
        return self.ads_viewed.values('ad').distinct().count()
    def number_app_installed(self):
        return self.app_clicked.filter(installed=True).count()

class Staff(models.Model):
    first_name = models.CharField(max_length=255)
    bio = models.TextField()
    picture = models.ImageField(upload_to='staff_picture')
    position = models.CharField(max_length=255)
    linkedin = models.URLField(null=True, blank=True)
