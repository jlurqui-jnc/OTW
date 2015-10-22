# -*- coding: utf-8 -*-
'''
Created on 22 de oct. de 2015

@author: jlurqui
'''

from django.db import models

class EstadoOrden(models.Model):
    '''
    Esta clase incluye los datos de los estados posibles de una orden de trabajo
    '''
    descripcion = models.CharField(max_length=50)

    @classmethod
    def create(cls, descripcion):
        return EstadoOrden(descripcion=descripcion)