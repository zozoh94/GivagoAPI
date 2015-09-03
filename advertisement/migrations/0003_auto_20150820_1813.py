# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0002_auto_20150820_1716'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ad',
            options={'permissions': (('add_ad', 'Can add an advertisement'), ('change_ad', 'Can change an advertisement'), ('delete_ad', 'Can delete an advertisement'))},
        ),
    ]
