#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
import controller
import compra_prod
from  ui_formulario_compra import Ui_Form

class Form(QtGui.QDialog):
	def __init__(self,parent=None,codigo=None,id_compra=None,cantidad=None,precio=None):
		QtGui.QDialog.__init__(self,parent)
		self.ui=Ui_Form()
		self.ui.setupUi(self)
		self.codigo=codigo
		self.id_compra=id_compra
		self.ui.precio.setText(unicode(precio))
		self.ui.cantidad.setText(unicode(cantidad))
		self.ui.cancelar.clicked.connect(self.cancel)
		self.ui.agregar.clicked.connect(self.editar_prod)
	def editar_prod(self):
		total=0
		desc=0
		precio=self.ui.precio.text()
		cantidad = self.ui.cantidad.text()
		descuento = self.ui.descuento.text()
		try:
        		prec=int(precio)
       			cantidad=int(cantidad)
			
			if (len(descuento)!=0):
				descu=int(descuento) 
				desc=(int(precio)*int(cantidad)*(int(descuento)))/100
			
			
			total=int(precio)*int(cantidad)-desc
			controller.editar_compra(int(precio),int(cantidad),total,self.codigo,self.id_compra)		
			self.reject()
		except ValueError:
			self.errorMessageDialog = QtGui.QErrorMessage(self)
            		self.errorMessageDialog.showMessage("Deben ser solo numeros")
			
		
		

	def cancel(self):
		self.reject()
