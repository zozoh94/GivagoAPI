# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0017_app_rpa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appclick',
            name='viewer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='app_clicked', blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='view',
            name='viewer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ads_viewed', blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
