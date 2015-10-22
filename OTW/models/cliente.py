# -*- coding: utf-8 -*-
'''
Created on 22 de oct. de 2015

@author: jlurqui
'''

from django.db import models
from django.utils import timezone


class Cliente(models.Model):
    '''
    Esta clase incluye los datos de un cliente
    '''
    domicilio = models.CharField(max_length=128)
    email = models.CharField(max_length=50)
    fechaalta = models.DateField(default=timezone.now)
    nombre = models.CharField(max_length=128)
    poblacion = models.CharField(max_length=128)
    telefono = models.CharField(max_length=15)

    @classmethod
    def create(cls, nombre, domicilio, poblacion, telefono, email):
        return Cliente(nombre=nombre, domicilio=domicilio, poblacion=poblacion,
                       telefono=telefono, email=email)

    def __str__(self,):
        return self.nombre
