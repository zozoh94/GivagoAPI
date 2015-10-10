# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('give', '0007_auto_20151009_1422'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advertisement', '0010_ad_number_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='ad',
            name='number_views',
        ),
        migrations.AddField(
            model_name='view',
            name='ad',
            field=models.ForeignKey(related_name='views', to='advertisement.Ad'),
        ),
        migrations.AddField(
            model_name='view',
            name='ong',
            field=models.ForeignKey(related_name='ads_gift', to='give.ONG'),
        ),
        migrations.AddField(
            model_name='view',
            name='viewer',
            field=models.ForeignKey(related_name='ads_viewed', to=settings.AUTH_USER_MODEL),
        ),
    ]
