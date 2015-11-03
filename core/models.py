from django.db import models
from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager

from advertisement.models import View

class User(AbstractUser):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    INCOME_LEVEL_CHOICES = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High')
    )
    interest = TaggableManager(blank=True)
    date_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, null=True, blank=True, choices=GENDER_CHOICES)
    income_level = models.IntegerField(null=True, blank=True, choices=INCOME_LEVEL_CHOICES)
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True)
    def number_ads_viewed(self):
        return self.ads_viewed.count()        
    def number_different_ads_viewed(self):
        return self.ads_viewed.filter(type=View.AD_TYPE).values('ad').distinct().count() + self.ads_viewed.filter(type=View.DAILYMOTION_TYPE).count()
    def number_app_installed(self):
        return self.app_clicked.filter(installed=True).count()
    def interests(self):
        return self.interest.names()
