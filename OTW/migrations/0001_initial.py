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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=128)),
                ('fechafin', models.DateTimeField(null=True)),
                ('fechainicio', models.DateTimeField(default=django.utils.timezone.now)),
                ('precio', models.DecimalField(max_digits=8, decimal_places=2, default=0)),
                ('unidades', models.DecimalField(max_digits=8, decimal_places=2, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=128)),
                ('fechaalta', models.DateField(default=django.utils.timezone.now)),
                ('precio', models.DecimalField(max_digits=8, decimal_places=2, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Operario',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
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
        migrations.CreateModel(
            name='MaterialOrden',
            fields=[
                ('accionorden_ptr', models.OneToOneField(serialize=False, auto_created=True, parent_link=True, to='OTW.AccionOrden', primary_key=True)),
                ('articulo', models.ForeignKey(related_name='acciones', to='OTW.Articulo')),
            ],
            bases=('OTW.accionorden',),
        ),
        migrations.AddField(
            model_name='accionorden',
            name='orden',
            field=models.ForeignKey(related_name='acciones', to='OTW.Orden'),
        ),
    ]
