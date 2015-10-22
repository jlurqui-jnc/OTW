# -*- coding: utf-8 -*-
'''
Created on 22 de oct. de 2015

@author: jlurqui
'''
from django.db import models
from .bases import BaseAccion
from .operario import Operario
from .orden import Orden


class AccionOrden(BaseAccion):
    '''
    Esta clase incluye los datos de una acción de mano de obra sobre una orden de trabajo
    '''
    operario = models.ForeignKey(Operario)
    orden = models.ForeignKey(Orden, related_name='acciones')
