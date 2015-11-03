# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_staff_last_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Staff',
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatar', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='income_level',
            field=models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')], blank=True, null=True),
        ),
    ]
