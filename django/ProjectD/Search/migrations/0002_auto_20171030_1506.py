# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Search', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='INDOORDEPOTINFO',
        ),
        migrations.DeleteModel(
            name='INDOORMILKPRODUCTINFO',
        ),
        migrations.DeleteModel(
            name='LOGISTICCARINFO',
        ),
        migrations.DeleteModel(
            name='LOGISTICDRIVERSINFO',
        ),
        migrations.DeleteModel(
            name='LOGISTICMILKPRODUCTINFO',
        ),
        migrations.DeleteModel(
            name='LOGISTICTERMINALINFO',
        ),
        migrations.DeleteModel(
            name='SOURCEBOTTLEINFO',
        ),
        migrations.DeleteModel(
            name='SOURCECOWSENVIRONMENT1',
        ),
        migrations.DeleteModel(
            name='SOURCECOWSFARM',
        ),
        migrations.DeleteModel(
            name='SOURCECOWSINFO',
        ),
        migrations.DeleteModel(
            name='SOURCEMILKPROCESSINFO',
        ),
        migrations.DeleteModel(
            name='SOURCESALE',
        ),
    ]
