# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('give', '0006_auto_20151005_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='ONG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('logo', models.ImageField(upload_to='ong_logo', blank=True, null=True)),
                ('site', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='gift',
            name='credits',
        ),
        migrations.AddField(
            model_name='gift',
            name='ong',
            field=models.ForeignKey(blank=True, null=True, related_name='gifts', on_delete=django.db.models.deletion.SET_NULL, to='give.ONG'),
        ),
    ]
