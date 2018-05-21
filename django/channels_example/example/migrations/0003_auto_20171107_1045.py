# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0002_delete_indoordepotinfo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TEST',
        ),
        migrations.DeleteModel(
            name='TEST1',
        ),
    ]
