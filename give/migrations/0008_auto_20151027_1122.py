# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('give', '0007_auto_20151009_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gift',
            name='name',
            field=models.SlugField(unique=True, max_length=255),
        ),
    ]
