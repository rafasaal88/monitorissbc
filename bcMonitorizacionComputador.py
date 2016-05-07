#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	Modulo encargado de definir la base de conocimiento del dominio de los computadores

	:author: Michael Castillo Polo y Luis Miguel López Coleto
	:date: 10/06/2015
"""

__docformat__ = "restructuredtext"

from bcMonitorizacion import * 
                
                
# DEFINICION DE LA BASE DE CONOCIMIENTO

##	Clase representativa del componente: CPU
#
#	Define las especificaciones de la CPU
#       
class CPU(Parametro):
    '''
    El parámetro es la CPU donde la unidad es % y la norma 
    esta por debajo de 50
    '''
    def __init__(self):
        Parametro.__init__(self, nombre=u'CPU', unidad='%')
        
        self.norma=Norma(valor=50, tipo='<=')
        

##	Clase representativa del componente: tarjeta gráfica
#
#	Define las especificaciones de la tarjeta gráfica
# 
class tarjetaGrafica(Parametro):
    '''
    El parámetro es la tarjeta gráfica donde la unidad es % y la norma 
    esta por debajo de 65
    '''
    def __init__(self):
        Parametro.__init__(self, nombre=u'Tarjeta Gráfica', unidad='%')
        
        self.norma=Norma(valor=65, tipo='<=')


##	Clase representativa del componente: memoria RAM
#
#	Define las especificaciones de la memoria RAM
# 
class memoriaRAM(Parametro):
    '''
    El parámetro es la memoria RAM donde la unidad es % y la norma 
    esta por debajo de 25
    '''
    def __init__(self):
        Parametro.__init__(self, nombre=u'Memoria RAM', unidad='%')
        
        self.norma=Norma(valor=25, tipo='<=')


##	Clase representativa del componente: temperatura
#
#	Define las especificaciones de la temperatura
# 
class temperatura(Parametro):
    '''
    El parámetro es la temperatura donde la unidad es °C y la norma esta por 
    debajo de 40
    '''
    def __init__(self):
        Parametro.__init__(self, nombre=u'Temperatura', unidad=u'°C')

        self.norma=Norma(valor=40, tipo='<=')


##	Clase representativa del componente: tarjeta de red
#
#	Define las especificaciones de la tarjeta de red
# 
class tarjetaRed(Parametro):
    '''
    El parámetro es la tarjeta de red donde la unidad es % y la norma 
    esta por debajo de 800
    '''
    def __init__(self):
        Parametro.__init__(self, nombre=u'Tarjeta de Red', unidad='bytes/s')
        
        self.norma=Norma(valor=800, tipo='<=')
        

# FUNCIONES AUXILIARES
def clases():
    '''
    Crea una lista de parámetros de la base de conocimiento.
    '''
    return [CPU(), tarjetaGrafica(), memoriaRAM(), temperatura(), tarjetaRed()]
