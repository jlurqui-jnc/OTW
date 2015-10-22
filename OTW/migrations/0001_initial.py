# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccionOrden',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=128)),
                ('fechafin', models.DateTimeField(null=True)),
                ('fechainicio', models.DateTimeField(default=django.utils.timezone.now)),
                ('precio', models.DecimalField(default=0, max_digits=8, decimal_places=2)),
                ('unidades', models.DecimalField(default=0, max_digits=8, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=128)),
                ('fechaalta', models.DateField(default=django.utils.timezone.now)),
                ('precio', models.DecimalField(default=0, max_digits=8, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('domicilio', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=50)),
                ('fechaalta', models.DateField(default=django.utils.timezone.now)),
                ('nombre', models.CharField(max_length=128)),
                ('poblacion', models.CharField(max_length=128)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='EstadoOrden',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Operario',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('fechafin', models.DateField(null=True)),
                ('fechainicio', models.DateField(default=django.utils.timezone.now)),
                ('observaciones', models.TextField(max_length=2048, null=True)),
                ('resolucion', models.TextField(max_length=2048, null=True)),
                ('solicitud', models.TextField(max_length=2048)),
                ('cliente', models.ForeignKey(to='OTW.Cliente', related_name='ordenes')),
                ('estado', models.ForeignKey(to='OTW.EstadoOrden', related_name='ordenes')),
                ('responsable', models.ForeignKey(to='OTW.Operario', related_name='ordenes')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialOrden',
            fields=[
                ('accionorden_ptr', models.OneToOneField(auto_created=True, parent_link=True, serialize=False, primary_key=True, to='OTW.AccionOrden')),
                ('articulo', models.ForeignKey(to='OTW.Articulo', related_name='acciones')),
            ],
            bases=('OTW.accionorden',),
        ),
        migrations.AddField(
            model_name='accionorden',
            name='orden',
            field=models.ForeignKey(to='OTW.Orden', related_name='acciones'),
        ),
    ]
