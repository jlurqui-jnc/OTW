# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OTW', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estadoorden',
            name='id',
        ),
        migrations.AddField(
            model_name='estadoorden',
            name='codigo',
            field=models.CharField(default=None, max_length=10, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
