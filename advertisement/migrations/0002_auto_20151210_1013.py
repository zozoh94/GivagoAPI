# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('give', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0002_auto_20150616_2121'),
        ('advertisement', '0001_initial'),
        ('sponsor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='view',
            name='viewer',
            field=models.ForeignKey(related_name='ads_viewed', blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='appclick',
            name='app',
            field=models.ForeignKey(related_name='clicks', blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='advertisement.App'),
        ),
        migrations.AddField(
            model_name='appclick',
            name='ong',
            field=models.ForeignKey(to='give.ONG', related_name='app_gift'),
        ),
        migrations.AddField(
            model_name='appclick',
            name='viewer',
            field=models.ForeignKey(related_name='app_clicked', blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ad',
            name='author',
            field=models.ForeignKey(related_name='ads', blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sponsor.SponsorManager'),
        ),
        migrations.AddField(
            model_name='ad',
            name='sponsor',
            field=models.ForeignKey(to='sponsor.Sponsor', related_name='ads'),
        ),
        migrations.AddField(
            model_name='ad',
            name='tags',
            field=taggit.managers.TaggableManager(through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags', to='taggit.Tag'),
        ),
    ]
