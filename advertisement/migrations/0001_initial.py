# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import embed_video.fields
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('give', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('video', embed_video.fields.EmbedVideoField()),
                ('remaining_views', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=2, default='GB', choices=[('GB', 'Great Britain'), ('AU', 'Australia'), ('FR', 'France'), ('US', 'USA'), ('BR', 'Brazil'), ('ES', 'Spain'), ('IT', 'Italia')])),
                ('link', models.URLField()),
                ('os', models.SmallIntegerField(choices=[(1, 'Android'), (2, 'iOS'), (3, 'iPad'), (4, 'iPhone'), (5, 'Free')], default=1)),
                ('rpa', models.DecimalField(decimal_places=2, max_digits=3)),
                ('thumbnail', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AppClick',
            fields=[
                ('id', models.UUIDField(editable=False, default=uuid.uuid4, serialize=False, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('installed', models.BooleanField(default=False)),
                ('date_installed', models.DateTimeField(default=None, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('type', models.SmallIntegerField(choices=[(1, 'Ad'), (2, 'DailyMotion')], default=1)),
                ('ad', models.ForeignKey(related_name='views', blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='advertisement.Ad')),
                ('ong', models.ForeignKey(to='give.ONG', related_name='ads_gift')),
            ],
        ),
    ]
