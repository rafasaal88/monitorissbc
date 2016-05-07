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
class tensionSistolica(Parametro):
    '''
    El parámetro es la tensión sistólica donde la unidad es mmHg y la norma 
    esta por debajo de 140
    '''
    def __init__(self):
        Parametro.__init__(self, nombre=u'Tensión Sistólica', unidad='mmHg')
        
        self.norma=Norma(valor=140, tipo='<=')


##	Clase representativa de la constante vital: tensión diastólica
#
#	Define las especificaciones de la tensión diastólica
#    
class tensionDiastolica(Parametro):
    '''
    El parámetro es la tensión diastólica donde la unidad es mmHg y la norma 
    esta por debajo de 90
    '''
    def __init__(self):
        Parametro.__init__(self, nombre=u'Tensión Diastólica', unidad='mmHg')
        
        self.norma=Norma(valor=90, tipo='<=')


##	Clase representativa de la constante vital: frecuencia cardíaca
#
#	Define las especificaciones de la frecuencia cardíaca
#    
class frecuenciaCardiaca(Parametro):
    '''
    El parámetro es la frecuencia cardiaca donde la unidad es puls/min y 
    la norma esta por debajo de 100
    '''
    def __init__(self):
        Parametro.__init__(self, nombre=u'Frecuencia Cardíaca', unidad='puls/min')
        
        self.norma=Norma(valor=100, tipo='<=')
        

##	Clase representativa de la constante vital: frecuencia respiratoria
#
#	Define las especificaciones de la frecuencia respiratoria
#    
class frecuenciaRespiratoria(Parametro):
    '''
    El parámetro es la frecuencia respiratoria donde la unidad es resp/min y 
    la norma esta por debajo de 20
    '''
    def __init__(self):
        Parametro.__init__(self, nombre=u'Frecuencia Respiratoria', unidad='resp/min')
        
        self.norma=Norma(valor=20, tipo='<=')


##	Clase representativa de la constante vital: nivel de oxígeno
#
#	Define las especificaciones del nivel de oxígeno
#    
class nivelOxigeno(Parametro):
    '''
    El parámetro es el nivel de oxígeno donde la unidad es % y la norma esta 
    por encima de 95
    '''
    def __init__(self):
        Parametro.__init__(self, nombre=u'Nivel de Oxígeno', unidad='%')
        
        self.norma=Norma(valor=95, tipo='>=')


##	Clase representativa de la constante vital: temperatura
#
#	Define las especificaciones de la temperatura
#    
class temperatura(Parametro):
    '''
    El parámetro es la temperatura donde la unidad es °C y la norma esta por 
    debajo de 37
    '''
    def __init__(self):
        Parametro.__init__(self, nombre=u'Temperatura', unidad=u'°C')

        self.norma=Norma(valor=37, tipo='<=')


# FUNCIONES AUXILIARES
def clases():
    '''
    Crea una lista de parámetros de la base de conocimiento.
    '''
    return [tensionSistolica(), tensionDiastolica(), frecuenciaCardiaca(), frecuenciaRespiratoria(), nivelOxigeno(), temperatura()]
