#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
import controller
from datetime import *
import compra_prod
from  ui_datos_compra import Ui_Form

class Form(QtGui.QDialog):
	def __init__(self,parent=None):
		QtGui.QDialog.__init__(self,parent)
		self.ui=Ui_Form()
		self.ui.setupUi(self)
		self.ui.cancelar.clicked.connect(self.cancel)
		self.ui.aceptar.clicked.connect(self.agregar_prod_compra)
	
	def agregar_prod_compra(self):
	        """
	        
	        """
		p=datetime.today()
		date=p.strftime("%d/%m/%Y")
		proveedor=self.ui.proveedor.text()
		descripcion= self.ui.descripcion.text()
		codigo=controller.agr_dato(date,proveedor,descripcion)
		form=compra_prod.Form(self,codigo)
		form.exec_()	
		self.reject()
	
	def cancel(self):
		self.reject()
