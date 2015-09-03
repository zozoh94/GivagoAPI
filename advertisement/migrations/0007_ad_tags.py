# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('advertisement', '0006_auto_20150826_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='tags',
            field=taggit.managers.TaggableManager(verbose_name='Tags', to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', blank=True),
        ),
    ]
