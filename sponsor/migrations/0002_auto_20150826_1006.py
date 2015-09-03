# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='facebook',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='flickr',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='linkedin',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='logo',
            field=models.ImageField(upload_to='sponsor_logo', null=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='twitter',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='youtube',
            field=models.URLField(null=True),
        ),
    ]
