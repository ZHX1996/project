# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0004_test_test1'),
    ]

    operations = [
        migrations.CreateModel(
            name='TEST2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('TIM', models.CharField(max_length=20)),
                ('TEM', models.CharField(max_length=20)),
                ('HUM', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'TEST2',
            },
        ),
        migrations.CreateModel(
            name='TEST3',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('TIM', models.CharField(max_length=20)),
                ('TEM', models.CharField(max_length=20)),
                ('HUM', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'TEST3',
            },
        ),
        migrations.CreateModel(
            name='TEST4',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('TIM', models.CharField(max_length=20)),
                ('TEM', models.CharField(max_length=20)),
                ('HUM', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'TEST4',
            },
        ),
    ]
