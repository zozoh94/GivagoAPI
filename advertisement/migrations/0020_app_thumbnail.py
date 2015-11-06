# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0019_auto_20151106_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='thumbnail',
            field=models.URLField(null=True),
        ),
    ]
