# -*- coding: utf-8 -*-
'''
Created on 22 de oct. de 2015

@author: jlurqui
'''
from .orden import Orden
from django.db import models
from .operario import Operario
from .accionOrden import AccionOrden
from .articulo import Articulo
from .bases import BaseAccion


class MaterialOrden(BaseAccion):
    '''
    Esta clase incluye los datos de un material imputado a una orden de trabajo
    '''

    articulo = models.ForeignKey(Articulo, related_name='acciones')
    operario = models.ForeignKey(Operario, related_name='material_orden')
    orden = models.ForeignKey(Orden, related_name='material')
