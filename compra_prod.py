#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
import controller
import agr_prod_compra
from ui_compras_prod import Ui_Form

class Form(QtGui.QDialog):
	def __init__(self,parent=None):
		QtGui.QDialog.__init__(self,parent)
		self.ui=Ui_Form()
		self.ui.setupUi(self)
		
		self.compra()		
		self.productos()
		
		self.set_listeners()
	def set_listeners(self):
		self.ui.buscar_prod_2.clicked.connect(self.cargar_buscar)
		self.ui.agregar_prod.clicked.connect(self.agregar_compra)
	def agregar(self,codigo):
		form=agr_prod_compra.Form(self,codigo)
		
		form.exec_()
	def agregar_compra(self,precio=None,cantidad=None):
		
		model = self.ui.tabla_prod.model()
        	index = self.ui.tabla_prod.currentIndex()
        	if index.row() == -1: 
            		self.errorMessageDialog = QtGui.QErrorMessage(self)
            		self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            		return False
        	else:
            		codigo = model.index(index.row(),0, QtCore.QModelIndex()).data()
			self.agregar(codigo)
			
			
			self.compra(codigo)
		
	def cargar_buscar(self):
		dato = self.ui.buscar_prod.text()
		prod = controller.buscar_producto(dato)
		self.productos(prod)
	def compra(self,codigo=None,producto=None):
		if producto is None:
		    producto = controller.get_prod_compra()
		
		self.model = QtGui.QStandardItemModel(len(producto), 6)
		self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Codigo"))
		self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Nombre"))
		self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Descripcion"))
		self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Marca"))
		self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"Color"))
		self.model.setHorizontalHeaderItem(5, QtGui.QStandardItem(u"Precio unitario"))
		self.model.setHorizontalHeaderItem(6, QtGui.QStandardItem(u"Cantidad"))
		r=0
		total_compra=0
		for row in producto:
			index = self.model.index(r, 0, QtCore.QModelIndex()); 
			self.model.setData(index,row['codigo'])
			index = self.model.index(r, 1, QtCore.QModelIndex()); 
			self.model.setData(index,row['nombre'])
			index = self.model.index(r, 2, QtCore.QModelIndex()); 
			self.model.setData(index, row['descripcion'])
			index = self.model.index(r, 3, QtCore.QModelIndex()); 
			self.model.setData(index,row['marca'])
			index = self.model.index(r, 4, QtCore.QModelIndex()); 
			self.model.setData(index, row['color'])
			index = self.model.index(r, 5, QtCore.QModelIndex()); 
			self.model.setData(index, row['cantidad'])
			index = self.model.index(r, 6, QtCore.QModelIndex()); 
			self.model.setData(index, row['precio_unitario'])
			total_compra=total_compra+row['total']
			self.ui.total_compra.setPlainText(unicode(total_compra))
			r =r+1
		
		self.ui.tabla_compra.setModel(self.model)
		self.ui.tabla_compra.setColumnWidth(0, 150)
		self.ui.tabla_compra.setColumnWidth(1, 150)
		self.ui.tabla_compra.setColumnWidth(2, 150)
		self.ui.tabla_compra.setColumnWidth(3, 150)
		self.ui.tabla_compra.setColumnWidth(4, 150)
		self.ui.tabla_compra.setColumnWidth(5, 200)
		self.ui.tabla_compra.setColumnWidth(6, 150)
		
	def productos(self, producto=None):
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

		self.ui.tabla_prod.setModel(self.model)
		self.ui.tabla_prod.setColumnWidth(0, 150)
		self.ui.tabla_prod.setColumnWidth(1, 150)
		self.ui.tabla_prod.setColumnWidth(2, 150)
		self.ui.tabla_prod.setColumnWidth(3, 150)
		self.ui.tabla_prod.setColumnWidth(4, 150)
	
