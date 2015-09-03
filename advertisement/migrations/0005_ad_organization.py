# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('advertisement', '0004_auto_20150820_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='organization',
            field=models.ForeignKey(related_name='ads', to='auth.Group', null=True),
        ),
    ]
