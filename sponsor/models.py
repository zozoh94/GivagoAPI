from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from django.conf import settings

class Sponsor(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to='sponsor_logo', null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    flickr = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    def __str__(self):
        return self.name

class SponsorManager(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sponsor = models.ForeignKey('Sponsor', related_name='managers')
    def save(self, *args, **kwargs):
        add_ad = Permission.objects.get(codename='add_ad')
        change_ad = Permission.objects.get(codename='change_ad')
        delete_ad = Permission.objects.get(codename='delete_ad')        
        change_sponsor = Permission.objects.get(codename='change_sponsor')
        delete_sponsor = Permission.objects.get(codename='delete_sponsor')
        self.user.user_permissions.add(add_ad, change_ad, delete_ad,
                                       change_sponsor, delete_sponsor)
        super(SponsorManager, self).save(*args, **kwargs)
    def __str__(self):
        return self.user.__str__()
@receiver(pre_delete, sender=SponsorManager)
def delete_permissions_manager(sender, instance, using, **kwargs):
    add_ad = Permission.objects.get(codename='add_ad')
    change_ad = Permission.objects.get(codename='change_ad')
    delete_ad = Permission.objects.get(codename='delete_ad')
    change_sponsor = Permission.objects.get(codename='change_sponsor')
    delete_sponsor = Permission.objects.get(codename='delete_sponsor')
    instance.user.user_permissions.remove(add_ad, change_ad, delete_ad,
                                          change_sponsor, delete_sponsor)

