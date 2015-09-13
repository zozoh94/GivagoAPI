# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('give', '0002_remove_gift_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='gift',
            name='credits',
            field=models.IntegerField(default=0),
        ),
    ]
