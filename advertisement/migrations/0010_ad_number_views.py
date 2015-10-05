# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0009_auto_20150918_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='number_views',
            field=models.IntegerField(default=0),
        ),
    ]
