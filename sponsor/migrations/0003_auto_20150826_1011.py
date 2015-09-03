# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0002_auto_20150826_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='flickr',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='logo',
            field=models.ImageField(upload_to='sponsor_logo', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', blank=True, verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='youtube',
            field=models.URLField(blank=True, null=True),
        ),
    ]
