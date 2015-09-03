# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('logo', models.ImageField(upload_to='sponsor_logo')),
                ('youtube', models.URLField()),
                ('facebook', models.URLField()),
                ('twitter', models.URLField()),
                ('flickr', models.URLField()),
                ('linkedin', models.URLField()),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', verbose_name='Tags', to='taggit.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='SponsorManager',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('sponsor', models.ForeignKey(related_name='manager', to='sponsor.Sponsor')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
