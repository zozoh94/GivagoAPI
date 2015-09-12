# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers
import django.core.validators
import django.utils.timezone
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], max_length=30, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', verbose_name='username', error_messages={'unique': 'A user with that username already exists.'})),
                ('first_name', models.CharField(max_length=30, blank=True, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, blank=True, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, blank=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status', help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(default=True, verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(to='auth.Group', related_name='user_set', blank=True, related_query_name='user', verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.')),
                ('interset', taggit.managers.TaggableManager(through='taggit.TaggedItem', to='taggit.Tag', blank=True, verbose_name='Tags', help_text='A comma-separated list of tags.')),
                ('user_permissions', models.ManyToManyField(to='auth.Permission', related_name='user_set', blank=True, related_query_name='user', verbose_name='user permissions', help_text='Specific permissions for this user.')),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
