#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	Modulo encargado de definir la base de conocimiento del dominio de los
	pacientes

	:author: Michael Castillo Polo y Luis Miguel López Coleto
	:date: 10/06/2015
"""

__docformat__ = "restructuredtext"

from bcMonitorizacion import *


# DEFINICION DE LA BASE DE CONOCIMIENTO

##	Clase representativa de la constante vital: tensión sistólica
#
#	Define las especificaciones de la tensión sistólica
#
class humedad(Parametro):
    '''
    El parámetro es la tensión sistólica donde la unidad es mmHg y la norma
    esta por debajo de 140
    '''
    def __init__(self):
        Parametro.__init__(self, nombre=u'Humedad absoluta', unidad='g/m3')

        self.norma=Norma(valor=65, tipo='>=')


##	Clase representativa de la constante vital: tensión diastólica
#
#	Define las especificaciones de la tensión diastólica
#
class temperatura(Parametro):
    '''
    El parámetro es la tensión diastólica donde la unidad es mmHg y la norma
    esta por debajo de 90
    '''
    def __init__(self):
        Parametro.__init__(self, nombre=u'Temperatura', unidad=u'°C')

        self.norma=Norma(valor=15, tipo='>=')


##	Clase representativa de la constante vital: frecuencia cardíaca
#
#	Define las especificaciones de la frecuencia cardíaca
#
class riego(Parametro):
    '''
    El parámetro es la frecuencia cardiaca donde la unidad es puls/min y
    la norma esta por debajo de 100
    '''
    def __init__(self):
        Parametro.__init__(self, nombre=u'Riego semanal', unidad='veces/sem')

        self.norma=Norma(valor=3, tipo='<=')

# FUNCIONES AUXILIARES
def clases():
    '''
    Crea una lista de parámetros de la base de conocimiento.
    '''
    return [humedad(), temperatura(), riego()]
