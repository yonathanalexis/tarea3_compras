#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
import controller 
import interfaz_compras
from ui_estadisticas import Ui_Form

class Form(QtGui.QDialog):
	def __init__(self,parent=None):
		QtGui.QDialog.__init__(self,parent)
		self.ui=Ui_Form()
		self.ui.setupUi(self)
		self.cargar_compras()
	def set_listeners(self):
		self.ui.btn_salir.clicked.connect(self.cancel)
		self.ui.btn_buscar.clicked.connect(self.buscar_compra)
		self.ui.btn_eliminar.clicked.connect(self.eliminar_compra)
		self.ui.btn_editar.clicked.connect(self.editar_compra)
	def buscar_compra(self):
		print("asa")
	def eliminar_compra(self):
		print("asa")
	def editar_compra(self):
		print("asa")
	def cargar_compras(self, producto=None):
		if producto is None:
		    producto = controller.get_productos()
		

		
		self.model = QtGui.QStandardItemModel(len(producto), 4)
		self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Codigo"))
		self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Nombre"))
		self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Descripcion"))
		self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Marca"))
		self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"Color"))

		r = 0
		for row in producto:
		    index = self.model.index(r, 0, QtCore.QModelIndex()); 
		    self.model.setData(index, row['codigo'])
		    index = self.model.index(r, 1, QtCore.QModelIndex()); 
		    self.model.setData(index, row['nombre'])
		    index = self.model.index(r, 2, QtCore.QModelIndex()); 
		    self.model.setData(index, row['descripcion'])
		    index = self.model.index(r, 3, QtCore.QModelIndex()); 
		    self.model.setData(index, row['marca'])
		    index = self.model.index(r, 4, QtCore.QModelIndex()); 
		    self.model.setData(index, row['color'])
		    r = r+1

		self.ui.tbl_compras.setModel(self.model)
		self.ui.tbl_compras.setColumnWidth(0, 90)
		self.ui.tbl_compras.setColumnWidth(1, 150)
		self.ui.tbl_compras.setColumnWidth(2, 150)
		self.ui.tbl_compras.setColumnWidth(3, 150)
		self.ui.tbl_compras.setColumnWidth(4, 150)

		
	def cancel(self):
		self.reject()
