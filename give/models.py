from django.db import models

class Gift(models.Model):
    name = models.SlugField(max_length=255, unique=True)
    icon = models.CharField(max_length=255, null=True)
    ong = models.ForeignKey('ONG', related_name='gifts', on_delete=models.SET_NULL, null=True, blank=True)
    def number_gifts(self):
        return self.ong.ads_gift.count() + self.ong.app_gift.filter(installed=True).count()

class ONG(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to='ong_logo', null=True, blank=True)
    site = models.URLField(null=True, blank=True)
    def __str__(self):
        return self.name
