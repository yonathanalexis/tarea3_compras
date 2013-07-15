#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
import controller
import compra_prod
from  ui_formulario_compra import Ui_Form

class Form(QtGui.QDialog):
	def __init__(self,parent=None,codigo=None):
		QtGui.QDialog.__init__(self,parent)
		self.ui=Ui_Form()
		self.ui.setupUi(self)
		self.codigo=codigo
		self.total_compra=0
		self.ui.cancelar.clicked.connect(self.cancel)
		self.ui.agregar.clicked.connect(self.agregar_prod)
	def agregar_prod(self):
		total=0
		precio=self.ui.precio.text()
		cantidad = self.ui.cantidad.text()
		descuento = self.ui.descuento.text()
		desc=int(precio)-(int(descuento)/100)
		total=desc*int(cantidad)
		self.total_compra=self.total_compra+total
		controller.agr_compra(precio,cantidad,total,self.codigo)		
		self.reject()
		

	def cancel(self):
		self.reject()
