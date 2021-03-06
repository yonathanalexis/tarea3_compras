#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
import controller
import editar_prod_compra
import formulario_compra
from ui_compras_prod import Ui_Form

class Form(QtGui.QDialog):
	def __init__(self,parent=None,codigo=None):
		QtGui.QDialog.__init__(self,parent)
		self.ui=Ui_Form()
		self.ui.setupUi(self)
		self.id_compra=codigo
		self.compra()
		self.productos()
		self.set_listeners()
	def set_listeners(self):
		self.ui.buscar_prod_2.clicked.connect(self.cargar_buscar)
		self.ui.agregar_prod.clicked.connect(self.agregar)
		self.ui.fin.clicked.connect(self.terminar)
		self.ui.cancelar_compra.clicked.connect(self.cancelar)
		self.ui.eliminar_prod.clicked.connect(self.eliminar_compra)
		self.ui.editar_prod.clicked.connect(self.editar_compra)
	def editar_compra(self):
		model = self.ui.tabla_compra.model()
        	index = self.ui.tabla_compra.currentIndex()
        	if index.row() == -1: 
            		self.errorMessageDialog = QtGui.QErrorMessage(self)
            		self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            		return False
        	else:
			
            		cantidad = model.index(index.row(),3, QtCore.QModelIndex()).data()
			precio=model.index(index.row(),4, QtCore.QModelIndex()).data()
        		codigo=model.index(index.row(),0, QtCore.QModelIndex()).data()
			form=editar_prod_compra.Form(self,codigo,self.id_compra,cantidad,precio)
			form.rejected.connect(self.compra)
			form.exec_()
	def eliminar_compra(self):
		model = self.ui.tabla_compra.model()
        	index = self.ui.tabla_compra.currentIndex()
        	if index.row() == -1: 
            		self.errorMessageDialog = QtGui.QErrorMessage(self)
            		self.errorMessageDialog.showMessage("Debe seleccionar una fila de la tabla de las compras	")
       
        	else:
            		codigo = model.index(index.row(),0, QtCore.QModelIndex()).data()
            	if (controller.delete(codigo)):
                	self.compra()
                	msgBox = QtGui.QMessageBox()
                	msgBox.setText("EL registro fue eliminado.")
                	msgBox.exec_()
                	return True
            	else:
                	self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
                	self.ui.errorMessageDialog.showMessage("Error al eliminar el registro")
                	return False	
	def cancelar(self):
		controller.cancelar_compra(self.id_compra)
		self.reject()
	def terminar(self):
		self.reject()
	def agregar(self):
		model = self.ui.tabla_prod.model()
        	index = self.ui.tabla_prod.currentIndex()
        	if index.row() == -1: 
            		self.errorMessageDialog = QtGui.QErrorMessage(self)
            		self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            		return False
        	else:
            		codigo = model.index(index.row(),0, QtCore.QModelIndex()).data()
			id_producto=controller.tomar_id(codigo)
		form=formulario_compra.Form(self,codigo,self.id_compra)
		form.exec_()
		self.compra(None,id_producto)
	def cargar_buscar(self):
		dato = self.ui.buscar_prod.text()
		prod = controller.buscar_producto(dato)
		self.productos(prod)
	def compra(self,producto=None,id_producto=None):
		if producto is None:
		    producto = controller.get_prod_compra(self.id_compra,id_producto)
		
		self.model = QtGui.QStandardItemModel(len(producto), 6)
		self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Codigo"))
		self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Nombre"))
		self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Marca"))
		self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"cantidad"))
		self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"Precio unitario"))
		self.model.setHorizontalHeaderItem(5, QtGui.QStandardItem(u"Total"))
		r=0
		total_compra=0
		for row in producto:
			index = self.model.index(r, 0, QtCore.QModelIndex()); 
			self.model.setData(index,row['codigo'])
			index = self.model.index(r, 1, QtCore.QModelIndex()); 
			self.model.setData(index,row['nombre'])
			index = self.model.index(r, 2, QtCore.QModelIndex()); 
			self.model.setData(index,row['marca'])
			index = self.model.index(r, 3, QtCore.QModelIndex());
			self.model.setData(index, row['precio_unitario'])
			index = self.model.index(r, 4, QtCore.QModelIndex()); 
			self.model.setData(index, row['cantidad'])
			index = self.model.index(r, 5, QtCore.QModelIndex()); 
			self.model.setData(index, row['total'])
			total_compra=total_compra+row['total']
			self.ui.line_total.setText(unicode(total_compra))
			r =r+1
		
		self.ui.tabla_compra.setModel(self.model)
		self.ui.tabla_compra.setColumnWidth(0, 100)
		self.ui.tabla_compra.setColumnWidth(1, 150)
		self.ui.tabla_compra.setColumnWidth(2, 150)
		self.ui.tabla_compra.setColumnWidth(3, 150)
		self.ui.tabla_compra.setColumnWidth(4, 150)
		self.ui.tabla_compra.setColumnWidth(5, 150)

		
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
		self.ui.tabla_prod.setColumnWidth(0, 100)
		self.ui.tabla_prod.setColumnWidth(1, 150)
		self.ui.tabla_prod.setColumnWidth(2, 150)
		self.ui.tabla_prod.setColumnWidth(3, 150)
		self.ui.tabla_prod.setColumnWidth(4, 150)
	
