# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('give', '0004_auto_20150913_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='gift',
            name='fa_icon',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
