# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('actfund', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='curr_amount',
        ),
        migrations.AddField(
            model_name='survey',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 23, 14, 4, 47, 874414, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
