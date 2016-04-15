# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import qtils.models
from django.conf import settings
import quests.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_at', models.DateTimeField(db_index=True, auto_now_add=True)),
                ('updated_at', models.DateTimeField(db_index=True, auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=60)),
                ('number', models.IntegerField(db_index=True, default=quests.models.category_number)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_at', models.DateTimeField(db_index=True, auto_now_add=True)),
                ('updated_at', models.DateTimeField(db_index=True, auto_now=True)),
                ('shortname', models.CharField(db_index=True, unique=True, max_length=60)),
                ('score', models.IntegerField(db_index=True, editable=False)),
                ('provider_type', models.CharField(blank=True, max_length=60)),
                ('provider_file', models.FilePathField(db_index=True, path='C:\\Users\\andgein\\Documents\\Work\\2016\\04. Qoala\\qoala\\data\\tasks', recursive=True)),
                ('provider_state', models.BinaryField(null=True)),
                ('provider_hash', models.CharField(max_length=60, editable=False)),
                ('is_simple', models.BooleanField(db_index=True, default=True, verbose_name='Can be checked at main thread')),
                ('is_manual', models.BooleanField(db_index=True, default=False, verbose_name='Should be checked manually')),
                ('category', models.ForeignKey(editable=False, to='quests.Category')),
                ('open_for', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-score'],
            },
            bases=(qtils.models.ModelDiffMixin, models.Model),
        ),
        migrations.CreateModel(
            name='QuestAnswer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_at', models.DateTimeField(db_index=True, auto_now_add=True)),
                ('updated_at', models.DateTimeField(db_index=True, auto_now=True)),
                ('is_checked', models.BooleanField(db_index=True, default=False)),
                ('is_success', models.BooleanField(db_index=True, default=False)),
                ('result', models.TextField(blank=True)),
                ('score', models.IntegerField(db_index=True, default=0)),
                ('answer', models.TextField()),
                ('answer_file', models.FileField(upload_to='media', editable=False)),
            ],
            bases=(qtils.models.ModelDiffMixin, models.Model),
        ),
        migrations.CreateModel(
            name='QuestVariant',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_at', models.DateTimeField(db_index=True, auto_now_add=True)),
                ('updated_at', models.DateTimeField(db_index=True, auto_now=True)),
                ('timeout', models.DateTimeField(db_index=True)),
                ('try_count', models.IntegerField(db_index=True, default=1)),
                ('is_valid', models.BooleanField(db_index=True, default=True)),
                ('state', models.BinaryField()),
                ('quest', models.ForeignKey(to='quests.Quest')),
                ('team', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='questanswer',
            name='quest_variant',
            field=models.ForeignKey(to='quests.QuestVariant'),
        ),
        migrations.AlterIndexTogether(
            name='questvariant',
            index_together=set([('quest', 'team'), ('quest', 'team', 'is_valid', 'timeout')]),
        ),
        migrations.AlterIndexTogether(
            name='questanswer',
            index_together=set([('quest_variant', 'is_success', 'is_checked'), ('is_success', 'is_checked')]),
        ),
    ]
