# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20170508_1023'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('source', 'can see source'), ('logistic', 'can see logistic'), ('indoor', 'can see indoor'))},
        ),
    ]
