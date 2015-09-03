# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0003_auto_20150826_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
