#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
import controller 
from ui_formulario import Ui_Form

class Form(QtGui.QDialog):
	def __init__(self,parent=None,codigo=None,nombre=None,descripcion=None,marca=None,color=None):
		QtGui.QDialog.__init__(self,parent)
		self.ui=Ui_Form()
		self.ui.setupUi(self)
		self.codigo=codigo
		self.nombre=nombre
		self.descripcion=descripcion
		self.color=color
		self.marca=marca
		self.ui.codigo_prod.setText(codigo)
		self.ui.nombre_prod.setText(nombre)
		self.ui.descripcion_prod.setText(descripcion)
		self.ui.marca_prod.setText(marca)
		self.ui.color_prod.setText(color)
		self.ui.cancelar.clicked.connect(self.cancel)
		self.ui.agregar.clicked.connect(self.editar_prod)

		
	
	#envia lo ingresado a editar_prducto de controller.py
	def editar_prod(self):
			codigo=self.ui.codigo_prod.text()
			nombre=self.ui.nombre_prod.text()
			descripcion=self.ui.descripcion_prod.text()
			marca=self.ui.marca_prod.text()
			color=self.ui.color_prod.text()
			resultado=controller.editar_producto(codigo,nombre,descripcion,marca,color)

			if resultado:
				self.reject()
		
			
	def cancel(self):
				self.reject()
