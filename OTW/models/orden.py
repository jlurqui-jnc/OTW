# -*- coding: utf-8 -*-
'''
Created on 22 de oct. de 2015

@author: jlurqui
'''

from django.db import models
from django.utils import timezone

from .cliente import Cliente
from .estadoOrden import EstadoOrden
from .operario import Operario

class Orden(models.Model):
    '''
    Esta clase incluye los datos de cabecera de una orden de trabajo
    '''

    cliente = models.ForeignKey(Cliente, related_name='ordenes')
    estado = models.ForeignKey(EstadoOrden, related_name='ordenes')
    fechafin = models.DateField(null=True)
    fechainicio = models.DateField(default=timezone.now)
    observaciones = models.TextField(max_length=2048, null=True)
    resolucion = models.TextField(max_length=2048, null=True)
    responsable = models.ForeignKey(Operario, related_name='ordenes')
    solicitud = models.TextField(max_length=2048)
    
    @classmethod
    def create(cls, cliente, estado, fechainicio, responsable, solicitud):
        return Orden(cliente=cliente, estado=estado, fechainicio=fechainicio, 
                     responsable=responsable, solicitud=solicitud)