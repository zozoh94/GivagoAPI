# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0011_auto_20151009_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='view',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
