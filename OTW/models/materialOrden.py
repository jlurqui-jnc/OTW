# -*- coding: utf-8 -*-
'''
Created on 22 de oct. de 2015

@author: jlurqui
'''

from django.db import models

from .accionOrden import AccionOrden
from .articulo import Articulo

class MaterialOrden(AccionOrden):
    '''
    Esta clase incluye los datos de un material imputado a una orden de trabajo
    '''

    articulo = models.ForeignKey(Articulo, related_name='acciones')