# -*- coding: utf-8 -*-
'''
Created on 22 de oct. de 2015

@author: jlurqui
'''

from django.db import models

class Operario(models.Model):
    '''
    Esta clase incluye los datos de un operario
    '''

    nombre = models.CharField(max_length=50, default='')
 
    @classmethod
    def create(cls, nombre):
        return Operario(nombre=nombre)