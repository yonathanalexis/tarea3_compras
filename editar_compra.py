#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
import controller 
import editar_producto
from ui_editar_compra import Ui_Form

class Form(QtGui.QDialog):
	def __init__(self,parent=None,codigo=None):
		QtGui.QDialog.__init__(self,parent)
		self.ui=Ui_Form()
		self.ui.setupUi(self)
		self.set_listeners()
		self.codigo=codigo
		self.cargar_compra_productos()
	
	def set_listeners(self):
		"""
		Funcion para implementar listeners
		"""
		self.ui.btn_aceptar.clicked.connect(self.cancel)
		self.ui.btn_buscar.clicked.connect(self.buscar_producto)
		self.ui.btn_eliminar.clicked.connect(self.eliminar_compra_producto)
		self.ui.btn_editar_prod.clicked.connect(self.editar_compra_unitaria)
		
	def buscar_producto(self):
		"""
		funcion para buscar producto necesitado
		"""
		dato = self.ui.line_buscar.text()
		prod = controller.buscar_compra_realizada(dato,self.codigo)
		self.cargar_compra_productos(prod)


	def eliminar_compra_producto(self):
	        """
		funcion para eliminar compra seleccionada
		"""
		model = self.ui.tbl_compra.model()
        	index = self.ui.tbl_compra.currentIndex()
        	if index.row() == -1: 
            		self.errorMessageDialog = QtGui.QErrorMessage(self)
            		self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            		return False
        	else:
            		codigo = model.index(index.row(),0, QtCore.QModelIndex()).data()
            	if (controller.borrar_prod_com(codigo)):
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
	        """
		funcion para editar compra seleccionada
		"""
		model = self.ui.tbl_compra.model()
        	index = self.ui.tbl_compra.currentIndex()
        	if index.row() == -1: 
            		self.errorMessageDialog = QtGui.QErrorMessage(self)
            		self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            		return False
        	else:
            		cod = model.index(index.row(),0, QtCore.QModelIndex()).data()
			print(cod)
		form=editar_producto.Form(self,cod,self.codigo)
		form.rejected.connect(self.dato_nuevo)
		form.exec_()
	
	def dato_nuevo(self):
	        """
		funcion para cargar las compras
		"""
	        self.cargar_compra_productos()   
	
	def cargar_compra_productos(self, compra=None):
	        """
		funcion para cargar compras en la grilla de compras que se estan realizando
		"""
		if compra is None:
		    print(self.codigo)
		    compra = controller.get_compra_unitaria(self.codigo)
		self.model = QtGui.QStandardItemModel(len(compra), 6)
		self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Codigo"))
		self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Nombre"))
		self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Marca"))
		self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Precio unitario"))
		self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"Cantidad"))
		self.model.setHorizontalHeaderItem(5, QtGui.QStandardItem(u"Total"))
		r = 0
		for row in compra:
		    index = self.model.index(r, 0, QtCore.QModelIndex()); 
		    self.model.setData(index, row['fk_id_producto'])
		    index = self.model.index(r, 1, QtCore.QModelIndex()); 
		    self.model.setData(index, row['nombre'])
		    index = self.model.index(r, 2, QtCore.QModelIndex()); 
		    self.model.setData(index, row['marca'])
		    index = self.model.index(r, 3, QtCore.QModelIndex()); 
		    self.model.setData(index, row['precio_unitario'])
		    index = self.model.index(r, 4, QtCore.QModelIndex()); 
		    self.model.setData(index, row['cantidad'])
		    index = self.model.index(r, 5, QtCore.QModelIndex()); 
		    self.model.setData(index, row['total'])
		    r = r+1
		self.ui.tbl_compra.setModel(self.model)
		self.ui.tbl_compra.setColumnWidth(0, 50)
		self.ui.tbl_compra.setColumnWidth(1, 150)
		self.ui.tbl_compra.setColumnWidth(2, 150)
		self.ui.tbl_compra.setColumnWidth(3, 150)
		self.ui.tbl_compra.setColumnWidth(4, 150)

		
	def cancel(self):
		proveedor=self.ui.line_proveedor.text()
		descripcion= self.ui.line_descripcion.text()
		controller.editar_prov_des(proveedor,descripcion,self.codigo)
		self.reject()




