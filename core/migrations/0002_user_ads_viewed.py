# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0008_auto_20150826_1753'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ads_viewed',
            field=models.ManyToManyField(to='advertisement.Ad'),
        ),
    ]
