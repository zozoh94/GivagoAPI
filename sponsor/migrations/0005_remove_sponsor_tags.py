# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0004_auto_20150826_1011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsor',
            name='tags',
        ),
    ]
