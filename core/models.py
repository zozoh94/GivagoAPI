from django.db import models
from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager

from advertisement.models import Ad

class User(AbstractUser):
    interset = TaggableManager(blank=True)
    ads_viewed = models.ManyToManyField(Ad)
