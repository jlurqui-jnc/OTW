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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('descripcion', models.CharField(max_length=128)),
                ('fechafin', models.DateTimeField(null=True)),
                ('fechainicio', models.DateTimeField(default=django.utils.timezone.now)),
                ('precio', models.DecimalField(default=0, max_digits=8, decimal_places=2)),
                ('unidades', models.DecimalField(default=0, max_digits=8, decimal_places=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('descripcion', models.CharField(max_length=128)),
                ('fechaalta', models.DateField(default=django.utils.timezone.now)),
                ('precio', models.DecimalField(default=0, max_digits=8, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialOrden',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('descripcion', models.CharField(max_length=128)),
                ('fechafin', models.DateTimeField(null=True)),
                ('fechainicio', models.DateTimeField(default=django.utils.timezone.now)),
                ('precio', models.DecimalField(default=0, max_digits=8, decimal_places=2)),
                ('unidades', models.DecimalField(default=0, max_digits=8, decimal_places=2)),
                ('articulo', models.ForeignKey(related_name='acciones', to='OTW.Articulo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Operario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nombre', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('fechafin', models.DateField(null=True)),
                ('fechainicio', models.DateField(default=django.utils.timezone.now)),
                ('observaciones', models.TextField(max_length=2048, null=True)),
                ('resolucion', models.TextField(max_length=2048, null=True)),
                ('solicitud', models.TextField(max_length=2048)),
                ('cliente', models.ForeignKey(related_name='ordenes', to='OTW.Cliente')),
                ('estado', models.ForeignKey(related_name='ordenes', to='OTW.EstadoOrden')),
                ('responsable', models.ForeignKey(related_name='ordenes', to='OTW.Operario')),
            ],
        ),
        migrations.AddField(
            model_name='materialorden',
            name='operario',
            field=models.ForeignKey(related_name='material_orden', to='OTW.Operario'),
        ),
        migrations.AddField(
            model_name='materialorden',
            name='orden',
            field=models.ForeignKey(related_name='material', to='OTW.Orden'),
        ),
        migrations.AddField(
            model_name='accionorden',
            name='operario',
            field=models.ForeignKey(to='OTW.Operario'),
        ),
        migrations.AddField(
            model_name='accionorden',
            name='orden',
            field=models.ForeignKey(related_name='acciones', to='OTW.Orden'),
        ),
    ]
