#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
import controller 
#import editar_producto
from ui_editar_compra import Ui_Form

class Form(QtGui.QDialog):
	def __init__(self,parent=None):
		print("asas")
		QtGui.QDialog.__init__(self,parent)
		self.ui=Ui_Form()
		self.ui.setupUi(self)
		self.cargar_compra_productos()
	def set_listeners(self):
		self.ui.btn_aceptar.clicked.connect(self.cancel)
		self.ui.btn_buscar.clicked.connect(self.buscar_producto)
		self.ui.btn_eliminar.clicked.connect(self.eliminar_compra_producto)
		self.ui.btn_editar.clicked.connect(self.editar_compra_unitaria)
		
	def buscar_producto(self):
		dato = self.ui.line_buscar.text()
		prod = controller.buscar_compra_realizada(dato)
		self.cargar_compra_productos(prod)


	def eliminar_compra_producto(self):
		model = self.ui.tbl_compra.model()
        	index = self.ui.tbl_compra.currentIndex()
        	if index.row() == -1: 
            		self.errorMessageDialog = QtGui.QErrorMessage(self)
            		self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            		return False
        	else:
            		codigo = model.index(index.row(),0, QtCore.QModelIndex()).data()
            	if (controller.delete(codigo)):
                	self.cargar_compra_productos()
                	msgBox = QtGui.QMessageBox()
                	msgBox.setText("EL registro fue eliminado.")
                	msgBox.exec_()
                	return True
            	else:
                	self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
                	self.ui.errorMessageDialog.showMessage("Error al eliminar el registro")
                	return False
            		
	def editar_compra_unitaria(self):
		form=editar_producto.Form(self)
		form.rejected.connect(self.dato_nuevo)
		form.exec_()
	def dato_nuevo(self):
	        self.cargar_compras()   
	def cargar_compra_productos(self, compra=None):
		if compra is None:
		    compra = controller.get_compra()
		

		

		self.model = QtGui.QStandardItemModel(len(compra), 4)
		self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Nombre"))
		self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Marca"))
		self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Precio unitario"))
		self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Cantidad"))
		self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"Total"))
		r = 0
		for row in compra:
		    index = self.model.index(r, 0, QtCore.QModelIndex()); 
		    self.model.setData(index, row['nombre'])
		    index = self.model.index(r, 1, QtCore.QModelIndex()); 
		    self.model.setData(index, row['marca'])
		    index = self.model.index(r, 2, QtCore.QModelIndex()); 
		    self.model.setData(index, row['precio_unitario'])
		    index = self.model.index(r, 3, QtCore.QModelIndex()); 
		    self.model.setData(index, row['cantidad'])
		    index = self.model.index(r, 4, QtCore.QModelIndex()); 
		    self.model.setData(index, row['total'])
		    r = r+1

		self.ui.tbl_compra.setModel(self.model)
		self.ui.tbl_compra.setColumnWidth(0, 90)
		self.ui.tbl_compra.setColumnWidth(1, 150)
		self.ui.tbl_compra.setColumnWidth(2, 150)
		self.ui.tbl_compra.setColumnWidth(3, 150)
		self.ui.tbl_compra.setColumnWidth(4, 150)

		
	def cancel(self):
		self.reject()
