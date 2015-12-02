# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0020_app_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='country',
            field=models.CharField(max_length=2, choices=[('GB', 'Great Britain')], default='GB'),
        ),
    ]
