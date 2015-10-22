# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OTW', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accionorden',
            name='operario',
            field=models.ForeignKey(to='OTW.Operario', default=None, related_name='acciones_orden'),
            preserve_default=False,
        ),
    ]
