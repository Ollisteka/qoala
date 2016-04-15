# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_teamlogin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamlogin',
            name='logged_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
