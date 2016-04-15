# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_auto_20160415_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logged_at', models.DateField(auto_now_add=True)),
                ('ip_address', models.CharField(max_length=100)),
                ('team', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
