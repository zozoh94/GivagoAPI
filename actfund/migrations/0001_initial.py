# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('amount', models.DecimalField(max_digits=4, decimal_places=2)),
                ('curr_amount', models.DecimalField(max_digits=4, decimal_places=2)),
                ('user', models.ForeignKey(related_name='survey_completed', to=settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL)),
            ],
        ),
    ]
