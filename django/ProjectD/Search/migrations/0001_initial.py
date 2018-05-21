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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
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
            name='INDOORMILKPRODUCTINFO',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('TAGEPC', models.CharField(max_length=32)),
                ('PRONAME', models.CharField(max_length=20)),
                ('PROINOREX', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'INDOORMILKPRODUCTINFO',
            },
        ),
        migrations.CreateModel(
            name='LOGISTICCARINFO',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('TAGEPC', models.CharField(max_length=32)),
                ('CARID', models.CharField(max_length=32)),
                ('COMPANY', models.CharField(max_length=32)),
                ('REGISTERTIME', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'LOGISTICCARINFO',
            },
        ),
        migrations.CreateModel(
            name='LOGISTICDRIVERSINFO',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('TAGEPC', models.CharField(max_length=32)),
                ('DRIVERID', models.CharField(max_length=32)),
                ('DRIVERNAME', models.CharField(max_length=32)),
                ('DRIVERPHONE', models.CharField(max_length=32)),
                ('DRILICENSE', models.CharField(max_length=32)),
                ('SEX', models.CharField(max_length=20)),
                ('NATION', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'LOGISTICDRIVERSINFO',
            },
        ),
        migrations.CreateModel(
            name='LOGISTICMILKPRODUCTINFO',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('TAGEPC', models.CharField(max_length=32)),
                ('PRONAME', models.CharField(max_length=20)),
                ('PROSELLER', models.CharField(max_length=20)),
                ('PROSHOPNAME', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'LOGISTICMILKPRODUCTINFO',
            },
        ),
        migrations.CreateModel(
            name='LOGISTICTERMINALINFO',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('TERMINALDEVICEID', models.CharField(max_length=32)),
                ('SIMNO', models.CharField(max_length=32)),
                ('TEMPERATURE', models.CharField(max_length=32)),
                ('HUMIDITY', models.CharField(max_length=32)),
                ('TAGEPC', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'LOGISTICTERMINALINFO',
            },
        ),
        migrations.CreateModel(
            name='SOURCEBOTTLEINFO',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('PRODUCTIONTYPE', models.CharField(max_length=20)),
                ('HSCODE', models.CharField(max_length=30)),
                ('STORE', models.CharField(max_length=20)),
                ('PRODUCTIONDATE', models.CharField(max_length=20)),
                ('EXPIRATIONDATE', models.CharField(max_length=20)),
                ('MANUFACTURER', models.CharField(max_length=50)),
                ('MANUFACTURERLOC', models.CharField(max_length=50)),
                ('NETCONTENT', models.CharField(max_length=20)),
                ('COWSRFID', models.CharField(max_length=100)),
                ('OFFICIALWEBSITE', models.CharField(max_length=50)),
                ('TAGEPC', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'SOURCEBOTTLEINFO',
            },
        ),
        migrations.CreateModel(
            name='SOURCECOWSENVIRONMENT1',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('GATHERTIME', models.CharField(max_length=20)),
                ('SENSOR', models.CharField(max_length=20)),
                ('ENVIRONMENTTEM', models.CharField(max_length=20)),
                ('ENVIRONMENTHUM', models.CharField(max_length=20)),
                ('ENVIRONMENTPH', models.CharField(max_length=20)),
                ('ENVIRONMENTPHOTO', models.BinaryField()),
                ('COWSFARMID', models.CharField(max_length=20)),
                ('TAGEPC', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'SOURCECOWSENVIRONMENT1',
            },
        ),
        migrations.CreateModel(
            name='SOURCECOWSFARM',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('COWSFARMID', models.CharField(max_length=20)),
                ('COWSFARMNAME', models.CharField(max_length=50)),
                ('COWSFARMLOC', models.CharField(max_length=50)),
                ('COWSFARMSIZE', models.CharField(max_length=20)),
                ('COWSFARMPHONE', models.CharField(max_length=20)),
                ('TAGEPC', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'SOURCECOWSFARM',
            },
        ),
        migrations.CreateModel(
            name='SOURCECOWSINFO',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('COWSRFID', models.CharField(max_length=100)),
                ('COWSFARMID', models.CharField(max_length=20)),
                ('PRODUCTTIME', models.CharField(max_length=20)),
                ('MILKAMOUNT', models.CharField(max_length=20)),
                ('COWSPHOTO', models.BinaryField()),
                ('TAGEPC', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'SOURCECOWSINFO',
            },
        ),
        migrations.CreateModel(
            name='SOURCEMILKPROCESSINFO',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('FACTORYID', models.CharField(max_length=20)),
                ('FACTORYNAME', models.CharField(max_length=50)),
                ('PROCESSTIME', models.CharField(max_length=20)),
                ('PACKMATERIAL', models.CharField(max_length=20)),
                ('SUPPLEMENTNAME', models.CharField(max_length=100)),
                ('PROCESSPHOTO', models.BinaryField()),
                ('TAGEPC', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'SOURCEMILKPROCESSINFO',
            },
        ),
        migrations.CreateModel(
            name='SOURCESALE',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('MARKETNAME', models.CharField(max_length=20)),
                ('MARKETLOC', models.CharField(max_length=60)),
                ('MARKETTEL', models.CharField(max_length=20)),
                ('SALEDORNOT', models.CharField(max_length=50)),
                ('TAGEPC', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'SOURCESALE',
            },
        ),
    ]
