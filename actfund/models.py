from django.db import models
from django.conf import settings

class Survey(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='survey_completed', null=True, on_delete=models.SET_NULL, blank=True)
    amount = models.DecimalField(max_digits=4, decimal_places=2)
    date = models.DateTimeField(auto_now_add = True)
