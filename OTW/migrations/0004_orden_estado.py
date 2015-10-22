# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OTW', '0003_remove_orden_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='estado',
            field=models.ForeignKey(default=1, related_name='ordenes', to='OTW.EstadoOrden'),
            preserve_default=False,
        ),
    ]
