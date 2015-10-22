# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advertisement', '0014_auto_20151019_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='appclick',
            name='app',
            field=models.ForeignKey(default=3, to='advertisement.App', related_name='clicks'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appclick',
            name='viewer',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL, related_name='app_clicked'),
            preserve_default=False,
        ),
    ]
