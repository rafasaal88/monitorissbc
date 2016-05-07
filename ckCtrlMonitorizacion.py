#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	Modulo encargado de definir el subsistema de control del sistema de
	monitorizacion

	:author: Michael Castillo Polo y Luis Miguel López Coleto
	:date: 10/06/2015
"""

__docformat__ = "restructuredtext"

from PyQt4 import QtGui
import ckModMonitorizacion as ma

def eventoMonitorizar(dominio):
	"""
	Metodo encargado de ejecutar el metodo para monitorizar
	indicando el dominio

	:param dominio: Dominio en el que se va a monitorizar

	:author: Michael Castillo Polo y Luis Miguel López Coleto
	:date: 10/06/2015
	"""

	mp= ma.MetodoMonitorizacion(dominio)
	return mp.execute()
        


