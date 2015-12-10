# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.SlugField(max_length=255, unique=True)),
                ('icon', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ONG',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('logo', models.ImageField(upload_to='ong_logo', blank=True, null=True)),
                ('site', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='gift',
            name='ong',
            field=models.ForeignKey(related_name='gifts', blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='give.ONG'),
        ),
    ]
