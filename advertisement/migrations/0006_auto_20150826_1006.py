# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0005_ad_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='organization',
            field=models.ForeignKey(to='auth.Group', related_name='ads'),
        ),
    ]
