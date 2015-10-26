# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='linkedin',
            field=models.URLField(null=True, blank=True),
        ),
    ]
