# -*- coding: utf-8 -*-
'''
Created on 22 de oct. de 2015

@author: jlurqui
'''

from django.db import models
from django.utils import timezone


class Articulo(models.Model):
    '''
    Esta clase incluye los datos de un artículo
    '''

    descripcion = models.CharField(max_length=128)
    fechaalta = models.DateField(default=timezone.now)
    precio = models.DecimalField(default=0, max_digits=8, decimal_places=2)

    @classmethod
    def create(cls, descripcion):
        return Articulo(descripcion=descripcion)

    def __str__(self,):
        return self.nombre
