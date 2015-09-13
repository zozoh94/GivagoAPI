# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_ads_viewed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='interset',
            new_name='interest',
        ),
        migrations.AlterField(
            model_name='user',
            name='ads_viewed',
            field=models.ManyToManyField(to='advertisement.Ad', blank=True),
        ),
    ]
