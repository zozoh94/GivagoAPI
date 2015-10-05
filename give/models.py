from django.db import models

class Gift(models.Model):
    name = models.CharField(max_length=255, unique=True)
    icon = models.CharField(max_length=255, null=True)
    credits = models.IntegerField(default=0)
