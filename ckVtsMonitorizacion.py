#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	Modulo encargado de definir las vistas del sistema de monitorizacion

	:author: Michael Castillo Polo y Luis Miguel López Coleto
	:date: 10/06/2015
"""

__docformat__ = "restructuredtext"

import sys
from PyQt4 import QtCore
from PyQt4 import QtGui

from bcMonitorizacion import *
import ckCtrlMonitorizacion as ctrl
import bcMonitorizacionVivero as bcmp
import bcMonitorizacionComputador as bcmc

class MonitorizacionDlg(QtGui.QWidget):
	"""
	Clase donde se codifica la interfaz de la aplicacion

	:author: Michael Castillo Polo y Luis Miguel López Coleto
	:date: 10/06/2015
	"""
	def __init__(self):
		# Llamada al constructor de la clase padre
		super(MonitorizacionDlg, self).__init__()

		# Atributos de proposito general
		self.dominio= 'Vivero'
		self.crearTablasDescripcionDominio()

		# Atributos de Interfaz de Usuario
		self.grid = QtGui.QGridLayout()
		self.grid.setSpacing(10)

		# Descripcion del dominio
		labelTextDescripcionDominio=QtGui.QLabel(u"Descripción del dominio",self)

		self.grid.addWidget(labelTextDescripcionDominio, 0, 1)
		self.grid.addWidget(self.tablaWidgetComputador, 1, 1, 1, 1)
		self.tablaWidgetComputador.hide()
		self.grid.addWidget(self.tablaWidgetVivero, 1, 1, 1, 1)

  		# Dominio de aplicacion
		labelComboBoxDominio=QtGui.QLabel("Dominio", self)
		self.comboBoxDominio= QtGui.QComboBox()
		self.comboBoxDominio.addItem('Vivero')
		self.comboBoxDominio.addItem('Computadoras')
		self.comboBoxDominio.activated[str].connect(self.dominioModificado)

		self.grid.addWidget(labelComboBoxDominio, 2, 1)
		self.grid.addWidget(self.comboBoxDominio, 3, 1)

		# Justificacion de la monitorizacion
		labelTextjustificacionL=QtGui.QLabel(u"Justificación de la monitorización",self)
		self.plainTextEditExplicacion = QtGui.QPlainTextEdit()
		self.plainTextEditExplicacion.setReadOnly(True)

		self.grid.addWidget(labelTextjustificacionL, 0, 0)
		self.grid.addWidget(self.plainTextEditExplicacion, 1, 0, 30, 1)


		# Definicion de los botones
		self.monitorizarButtom=QtGui.QPushButton('Monitorizar')
		self.borrarButtom=QtGui.QPushButton('Borrar')
		self.salirButtom=QtGui.QPushButton('Salir')
		self.buttomsLayout = QtGui.QHBoxLayout()
		self.buttomsLayout.addStretch()
		self.buttomsLayout.addWidget(self.monitorizarButtom)
		self.buttomsLayout.addWidget(self.borrarButtom)
		self.buttomsLayout.addWidget(self.salirButtom)
		self.buttomsLayout.addStretch()

		# Creacion de un contenedor vertical para desarrollar la interfaz
		mainLayout = QtGui.QVBoxLayout()
		mainLayout.addLayout(self.grid)
		mainLayout.addLayout(self.buttomsLayout)
		self.setLayout(mainLayout)

		# Definir las dimensiones de la ventana, titulo y a continuacion, mostrarla
		self.setGeometry(0, 0, 1200, 600)
		self.setWindowTitle("TAREA DE MONITORIZACION")
		self.show()

		#self.plainTextEditExplicacion.appendPlainText("Dominio" + self.dominio)

		# Señales
		self.monitorizarButtom.clicked.connect(self.monitorizar)
		self.borrarButtom.clicked.connect(self.plainTextEditExplicacion.clear)
		self.salirButtom.clicked.connect(self.close)

	def crearTablasDescripcionDominio(self):
		"""
		Metodo encargado de crear un tabla representativa de cada dominio
		a traves de cual se podran indicar la descripción del mismo

		:author: Michael Castillo Polo y Luis Miguel López Coleto
		:date: 10/06/2015
		"""
		self.etiquetasHeader= ['PARAMETRO', 'NORMA', 'UNIDAD']

		#Vivero
		self.cc=bcmp.clases()

		# Crear la tabla relativa al dominio de Vivero
		self.tablaWidgetVivero= QtGui.QTableWidget(len(self.cc), 3)
		self.tablaWidgetVivero.setColumnWidth(0,200)
		self.tablaWidgetVivero.setColumnWidth(1,200)
		self.tablaWidgetVivero.setColumnWidth(2,150)
		self.tablaWidgetVivero.setHorizontalHeaderLabels(self.etiquetasHeader)

		i=0
		for c in self.cc:
			parametro = QtGui.QTableWidgetItem(c.nombre)
			parametro.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

			norma = QtGui.QTableWidgetItem(c.norma.tipo + ' ' + str(c.norma.valor))
			norma.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

			unidad = QtGui.QTableWidgetItem(c.unidad)
			unidad.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

			self.tablaWidgetVivero.setItem(i,0,parametro)
			self.tablaWidgetVivero.setItem(i,1,norma)
			self.tablaWidgetVivero.setItem(i,2,unidad)
			i=i+1

		#COMPUTADORES
		self.cc=bcmc.clases()

		# Crear la tabla relativa al dominio de los computadores
		self.tablaWidgetComputador= QtGui.QTableWidget(len(self.cc), 3)
		self.tablaWidgetComputador.setColumnWidth(0,200)
		self.tablaWidgetComputador.setColumnWidth(1,200)
		self.tablaWidgetComputador.setColumnWidth(2,150)
		self.tablaWidgetComputador.setHorizontalHeaderLabels(self.etiquetasHeader)

		i=0
		for c in self.cc:
			parametro = QtGui.QTableWidgetItem(c.nombre)
			parametro.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

			norma = QtGui.QTableWidgetItem(c.norma.tipo + ' ' + str(c.norma.valor))
			norma.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

			unidad = QtGui.QTableWidgetItem(c.unidad)
			unidad.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

			self.tablaWidgetComputador.setItem(i,0,parametro)
			self.tablaWidgetComputador.setItem(i,1,norma)
			self.tablaWidgetComputador.setItem(i,2,unidad)
			i=i+1


	def dominioModificado(self, text):
		"""
		Metodo encargado modificar y ajustar la interfaz de usuario en
		funcion del dominio seleccionado por el usuario

		:param text: Dominio seleccionado [str]

		:author: Michael Castillo Polo y Luis Miguel López Coleto
		:date: 10/06/2015
		"""

		# Comprobar que el dominio seleccionado sea distinto al actual

		if self.dominio != text:
			# Actualizar de forma interna el dominio seleccionado
			self.dominio = text

			# Actualizar la tabla descriptiva del objeto a clasisficar
			if self.dominio == "Vivero":
				self.tablaWidgetComputador.hide()
				self.tablaWidgetVivero.show()
			else:
				self.tablaWidgetVivero.hide()
				self.tablaWidgetComputador.show()

			# Limpiar justificacion de la respuesta
			self.plainTextEditExplicacion.clear()


	def monitorizar(self):
		"""
		Metodo encargado de iniciar el proceso de monitorizacion
		con el dominio elegido por el usuario

		:author: Michael Castillo Polo y Luis Miguel López Coleto
		:date: 10/06/2015
		"""

		explicacion = ctrl.eventoMonitorizar(self.dominio)

		# Reflejar los resultados por pantalla
		self.plainTextEditExplicacion.clear()
		self.plainTextEditExplicacion.appendPlainText(explicacion)
		self.plainTextEditExplicacion.moveCursor(QtGui.QTextCursor.Start)


if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    form = MonitorizacionDlg()
    sys.exit(app.exec_())
