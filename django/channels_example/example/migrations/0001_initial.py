# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='INDOORDEPOTINFO',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('ID', models.IntegerField()),
                ('TAGEPC', models.CharField(max_length=32)),
                ('DEPOTLOC', models.CharField(max_length=50)),
                ('DEPOTTEM', models.CharField(max_length=20)),
                ('DEPOTHUM', models.CharField(max_length=20)),
                ('MANAGERNAME', models.CharField(max_length=20)),
                ('MANAGERPHONE', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'INDOORDEPOTINFO',
            },
        ),
        migrations.CreateModel(
            name='TEST',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('TIM', models.CharField(max_length=20)),
                ('TEM', models.CharField(max_length=20)),
                ('HUM', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'TEST1',
            },
        ),
    ]
