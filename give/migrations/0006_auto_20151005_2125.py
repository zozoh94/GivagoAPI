# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('give', '0005_gift_fa_icon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gift',
            old_name='fa_icon',
            new_name='icon',
        ),
    ]
