# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0005_remove_sponsor_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsormanager',
            name='sponsor',
            field=models.ForeignKey(to='sponsor.Sponsor', related_name='managers'),
        ),
    ]
