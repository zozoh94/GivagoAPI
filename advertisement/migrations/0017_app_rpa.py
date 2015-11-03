# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0016_auto_20151024_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='rpa',
            field=models.DecimalField(max_digits=3, decimal_places=2, default=1.0),
            preserve_default=False,
        ),
    ]
