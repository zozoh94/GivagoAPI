# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0015_auto_20151019_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='view',
            name='ad',
            field=models.ForeignKey(to='advertisement.Ad', related_name='views', null=True),
        ),
        migrations.AlterField(
            model_name='view',
            name='type',
            field=models.SmallIntegerField(default=1, choices=[(1, 'Ad'), (2, 'DailyMotion')]),
        ),
    ]
