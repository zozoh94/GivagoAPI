# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('give', '0007_auto_20151009_1422'),
        ('advertisement', '0013_auto_20151010_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('link', models.URLField()),
                ('os', models.SmallIntegerField(choices=[(1, 'Android'), (2, 'iOS')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='AppClick',
            fields=[
                ('id', models.UUIDField(serialize=False, default=uuid.uuid4, editable=False, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('installed', models.BooleanField(default=False)),
                ('date_installed', models.DateTimeField(null=True, default=None, blank=True)),
                ('ong', models.ForeignKey(to='give.ONG', related_name='app_gift')),
            ],
        ),
        migrations.AlterField(
            model_name='ad',
            name='author',
            field=models.ForeignKey(to='sponsor.SponsorManager', related_name='ads', blank=True, on_delete=django.db.models.deletion.SET_NULL, null=True),
        ),
        migrations.AlterField(
            model_name='view',
            name='type',
            field=models.SmallIntegerField(choices=[(1, 'Ad')], default=1),
        ),
    ]
