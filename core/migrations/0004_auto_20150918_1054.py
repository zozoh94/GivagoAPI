# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150913_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ads_viewed',
            field=models.ManyToManyField(related_query_name='viewer', to='advertisement.Ad', blank=True, related_name='viewers'),
        ),
    ]
