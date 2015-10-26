# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_staff_linkedin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='last_name',
        ),
    ]
