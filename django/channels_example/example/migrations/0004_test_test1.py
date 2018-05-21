# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0003_auto_20171107_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='TEST',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('TIM', models.CharField(max_length=20)),
                ('TEM', models.CharField(max_length=20)),
                ('HUM', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'TEST',
            },
        ),
        migrations.CreateModel(
            name='TEST1',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('TIM', models.CharField(max_length=20)),
                ('TEM', models.CharField(max_length=20)),
                ('HUM', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'TEST1',
            },
        ),
    ]
