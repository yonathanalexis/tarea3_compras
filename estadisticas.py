#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
import controller 
import editar_compra
import interfaz_compras
from ui_estadisticas import Ui_Form

class Form(QtGui.QDialog):
	def __init__(self,parent=None):
		QtGui.QDialog.__init__(self,parent)
		self.ui=Ui_Form()
		self.ui.setupUi(self)
		self.set_listeners()
		self.cargar_compras()
	
	def set_listeners(self):
		"""
		Funcion para implemetar listeners
		"""
		self.ui.btn_salir.clicked.connect(self.cancel)
		self.ui.btn_buscar.clicked.connect(self.buscar_compra)
		self.ui.btn_eliminar.clicked.connect(self.eliminar_compra)
		self.ui.btn_editar.clicked.connect(self.editar_compra_unitaria)
	
	def buscar_compra(self):
		"""
		Funcion para buscar compra en la base de datos
		"""
		dato1 = self.ui.bus_compra.text()
		dato2 = self.ui.bus_producto.text()
		prod = controller.buscar_compra(dato1,dato2)
		self.cargar_compras(prod)
	
	def eliminar_compra(self):
		"""
		Funcion para eliminar compra seleccionada"
		"""
		model = self.ui.tbl_compras.model()
        	index = self.ui.tbl_compras.currentIndex()
        	if index.row() == -1: 
            		self.errorMessageDialog = QtGui.QErrorMessage(self)
            		self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            		return False
        	else:
            		codigo = model.index(index.row(),0, QtCore.QModelIndex()).data()
            	if (controller.borrar_compra(codigo)):
                	self.cargar_compras()
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
	        Funcion para editar compra seleccionada
	        """
		model = self.ui.tbl_compras.model()
        	index = self.ui.tbl_compras.currentIndex()
        	if index.row() == -1: 
            		self.errorMessageDialog = QtGui.QErrorMessage(self)
            		self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            		return False
        	else:
            		codigo = model.index(index.row(),0, QtCore.QModelIndex()).data()
			print(codigo)
		form=editar_compra.Form(self,codigo)
		form.rejected.connect(self.dato_nuevo)
		form.exec_()
	
	def dato_nuevo(self):
	        """
	        
	        """
	        self.cargar_compras()   
	
	def cargar_compras(self, compra=None):
		"""
		Funcion para cargar las compras en la grilla
		"""
		if compra is None:
		    compra = controller.get_compra()
		self.model = QtGui.QStandardItemModel(len(compra), 4)
		self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"codigo"))
		self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Fecha"))
		self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Proveedor"))
		self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"N° Factura"))
		self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"Descripcion"))
		r = 0
		#total=0
		#suma=0;
		#id_compra=-1
		#id_comparador=-1
		#lista=[]
		#j=-1
		#for i in id_:
		#	id_compra=id_(i['fk_id_compra'])

		#	if(id_comparador==id_compra):
		#		suma=suma+id_(i['total'])
		#		lista[j]=suma
		#	else:
		#		j=j+1
		#		suma=0
		#		suma=id_(i['total'])
		#		lista[j]=suma
		#	id_comparador=id_compra
		for row in compra:
		    index = self.model.index(r, 0, QtCore.QModelIndex());
		     
		    self.model.setData(index, row['id_compra'])
		    index = self.model.index(r, 1, QtCore.QModelIndex()); 
		    self.model.setData(index, row['fecha'])
		    index = self.model.index(r, 2, QtCore.QModelIndex()); 
		    self.model.setData(index, row['proveedor'])
		    index = self.model.index(r, 3, QtCore.QModelIndex()); 
		    self.model.setData(index, row['numero_factura'])
		    index = self.model.index(r, 4, QtCore.QModelIndex()); 
		    self.model.setData(index, row['descripcion']) 
		    r = r+1
		self.ui.tbl_compras.setModel(self.model)
		self.ui.tbl_compras.setColumnWidth(0, 50)
		self.ui.tbl_compras.setColumnWidth(1, 150)
		self.ui.tbl_compras.setColumnWidth(2, 150)
		self.ui.tbl_compras.setColumnWidth(3, 150)
		self.ui.tbl_compras.setColumnWidth(4, 150)

	def cancel(self):
		self.reject()
