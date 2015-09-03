# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0005_remove_sponsor_tags'),
        ('advertisement', '0007_ad_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='organization',
        ),
        migrations.AddField(
            model_name='ad',
            name='sponsor',
            field=models.ForeignKey(default=1, related_name='ads', to='sponsor.Sponsor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ad',
            name='author',
            field=models.ForeignKey(related_name='ads', to='sponsor.SponsorManager'),
        ),
    ]
