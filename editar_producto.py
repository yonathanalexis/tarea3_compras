#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
import controller 
from ui_editar_producto import Ui_Form

class Form(QtGui.QDialog):
	def __init__(self,parent=None,key=None):#,codigo=None
		QtGui.QDialog.__init__(self,parent)
		self.ui=Ui_Form()
		self.ui.setupUi(self)
		self.set_listeners()
		#self.codigo=codigo
	def set_listeners(self):
		self.ui.btn_salir.clicked.connect(self.cancel)
		self.ui.btn_aceptar.clicked.connect(self.agregar_cambios)

	def agregar_cambios(self):
		precio=self.ui.line_precio.text()
		cantidad = self.ui.line_cantidad.text()
		descuento = self.ui.line_descuento.text()


		result = controller.cambiar_precios(self.key,cantidad,precio,descuento)
		if result:
			self.reject() #Cerramos y esto cargara nuevamente la grilla
		#else:
			#self.ui.mensajes.setText("Hubo un problema al intentar crear el alumno")
 		
	def cancel(self):
		self.reject()
