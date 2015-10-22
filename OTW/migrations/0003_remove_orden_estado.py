# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OTW', '0002_auto_20151022_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orden',
            name='estado',
        ),
    ]
