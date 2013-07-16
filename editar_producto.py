#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
import controller 
from ui_editar_producto import Ui_Form

class Form(QtGui.QDialog):
	def __init__(self,parent=None,key=None,codigo=None):#producto,compra
		QtGui.QDialog.__init__(self,parent)
		self.ui=Ui_Form()
		self.ui.setupUi(self)
		self.key=key
		self.codigo=codigo
		self.set_listeners()
	def set_listeners(self):
	        """
		funcion para implementar listeners
		"""
		self.ui.btn_salir.clicked.connect(self.cancel)
		self.ui.btn_aceptar.clicked.connect(self.agregar_cambios)

	def agregar_cambios(self):
	        """
		funcion para agregar cambios a datos
		"""
		precio=self.ui.line_precio.text()
		cantidad = self.ui.line_cantidad.text()
		descuento = self.ui.line_descuento.text()
		desc=(int(precio)-((int(descuento))/100))
		total=desc*(int(cantidad))
		result = controller.cambiar_precios(self.codigo,self.key,cantidad,precio,total)
		if result:
			self.reject()
 		
	def cancel(self):
		self.reject()
