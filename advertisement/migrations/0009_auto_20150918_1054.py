# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0008_auto_20150826_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='sponsor.SponsorManager', null=True, related_name='ads'),
        ),
    ]
