# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_auto_20160415_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status')),
                ('name', models.CharField(db_index=True, help_text='team name', unique=True, max_length=60)),
                ('is_staff', models.BooleanField(db_index=True, help_text='статус персонала', default=False)),
                ('is_active', models.BooleanField(db_index=True, help_text='User can log in', default=True)),
                ('token', models.CharField(db_index=True, null=True, unique=True, max_length=64)),
                ('in_scoreboard', models.BooleanField(db_index=True, help_text='team is visible in scoreboard', default=True)),
                ('group', models.IntegerField(db_index=True, help_text='group identificator', blank=1, default=1)),
                ('groups', models.ManyToManyField(to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', blank=True, verbose_name='groups', related_name='user_set', related_query_name='user')),
                ('user_permissions', models.ManyToManyField(to='auth.Permission', help_text='Specific permissions for this user.', blank=True, verbose_name='user permissions', related_name='user_set', related_query_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
