# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('give', '0003_gift_credits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gift',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
