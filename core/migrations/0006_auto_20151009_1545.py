# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_user_number_ads_viewed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='ads_viewed',
        ),
        migrations.RemoveField(
            model_name='user',
            name='number_ads_viewed',
        ),
    ]
