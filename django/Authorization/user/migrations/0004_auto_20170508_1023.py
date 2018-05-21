# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20170502_2020'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('source', 'can see source'), ('logistic', 'can see logistc'), ('indoor', 'can see indoor'))},
        ),
    ]
