# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='login',
            field=models.CharField(default='', max_length=100, db_index=True, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(help_text='team name', max_length=10, db_index=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='token',
            field=models.CharField(null=True, max_length=100, db_index=True, unique=True),
        ),
    ]
