# -*- coding: utf-8 -*-
'''
Created on 22 de oct. de 2015

@author: jlurqui
'''

from django.db import models
from django.utils import timezone

from .orden import Orden

class AccionOrden(models.Model):
    '''
    Esta clase incluye los datos de una acción de mano de obra sobre una orden de trabajo
    '''

    descripcion = models.CharField(max_length=128)
    fechafin = models.DateTimeField(null=True)
    fechainicio = models.DateTimeField(default=timezone.now)
    orden = models.ForeignKey(Orden, related_name='acciones')
    precio = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    unidades = models.DecimalField(default=0, max_digits=8, decimal_places=2)    