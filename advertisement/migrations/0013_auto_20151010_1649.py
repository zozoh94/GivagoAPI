# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0012_auto_20151010_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='remaining_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='view',
            name='type',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
