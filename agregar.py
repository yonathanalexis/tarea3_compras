#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
import controller 
import interfaz_compras
from ui_formulario import Ui_Form

class Form(QtGui.QDialog):
	def __init__(self,parent=None):
		QtGui.QDialog.__init__(self,parent)
		self.ui=Ui_Form()
		self.ui.setupUi(self)
		self.ui.cancelar.clicked.connect(self.cancel)
		self.ui.agregar.clicked.connect(self.agregar_prod)
	def agregar_prod(self):
		codigo=self.ui.codigo_prod.text()
		nombre = self.ui.nombre_prod.text()
		descripcion = self.ui.descripcion_prod.text()
		color = self.ui.color_prod.text()
		marca = self.ui.marca_prod.text()


		result = controller.agregar_producto(codigo,nombre,descripcion,marca,color)

		if result:
			self.reject() #Cerramos y esto cargara nuevamente la grilla
		#else:
			#self.ui.mensajes.setText("Hubo un problema al intentar crear el alumno")
	def cancel(self):
		self.reject()
