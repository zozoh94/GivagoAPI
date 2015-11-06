# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0018_auto_20151104_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='os',
            field=models.SmallIntegerField(choices=[(1, 'Android'), (2, 'iOS'), (3, 'iPad'), (4, 'iPhone'), (5, 'Free')], default=1),
        ),
        migrations.AlterField(
            model_name='appclick',
            name='app',
            field=models.ForeignKey(blank=True, related_name='clicks', null=True, on_delete=django.db.models.deletion.SET_NULL, to='advertisement.App'),
        ),
        migrations.AlterField(
            model_name='view',
            name='ad',
            field=models.ForeignKey(blank=True, related_name='views', null=True, on_delete=django.db.models.deletion.SET_NULL, to='advertisement.Ad'),
        ),
    ]
