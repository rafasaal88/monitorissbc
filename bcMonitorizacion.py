#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	Modulo encargado de definir las clases fundamentales para la base
	de conocimiento de un sistema de clasificacion

	:author: Michael Castillo Polo y Luis Miguel López Coleto
	:date: 10/06/2015
"""

__docformat__ = "restructuredtext"

import types

		
# CLASE GENÉRICA PARA REPRESENTACION DE PARÁMETROS
class Parametro():
	"""
	Clase Parametro: permite especificar la unidad de medida
	de los parámetros que van a usarse en la base de conocimiento para 
	hacer la comparación.
	"""
    
	def __init__(self, nombre, unidad):
		self.nombre=nombre
		self.unidad=unidad			
					
# CLASE GENÉRICA PARA REPRESENTACION DE HALLAZGOS		
class Hallazgo():
	"""
	Clase Hallazgo: permite almacenar el valor que se recibe.
	"""
    
	def __init__(self, parametro, valor):
		self.parametro=parametro
		self.valor=valor
		
# CLASE GENÉRICA PARA REPRESENTACION DE NORMAS		
class Norma():
	"""
	Clase Norma: permite especificar la norma de un parámetro para su posterior
	comparación.
	"""

	def __init__(self, valor, tipo):
		self.valor=valor
		self.tipo=tipo
