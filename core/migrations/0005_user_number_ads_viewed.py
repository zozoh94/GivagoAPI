# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150918_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='number_ads_viewed',
            field=models.IntegerField(default=0),
        ),
    ]
