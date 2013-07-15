#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PySide import QtGui, QtCore
import controller
import editar
import agregar
import datos_compra
import estadisticas
from ui_compras import Ui_MainWindow


class Productos(QtGui.QMainWindow):

	def __init__(self):
		  super(Productos,self).__init__()
		  self.ui =  Ui_MainWindow()        
		  self.ui.setupUi(self)
		  self.cargar_productos()
		  self.set_listeners()
		  self.show()
	
	def set_listeners(self):
		  """
		  Funcion para implementar los listener
		  """
		  self.ui.editar_btn.clicked.connect(self.editar_dato)
		  self.ui.agregar_btn.clicked.connect(self.agregar_dato)
		  self.ui.eliminar_btn.clicked.connect(self.eliminar_dato)
		  self.ui.btn_buscar.clicked.connect(self.cargar_buscar)
		  self.ui.compra_btn.clicked.connect(self.compra)
 		  self.ui.estadisticas_btn.clicked.connect(self.estadisticas)
	
	def estadisticas(self):
		"""
		Funcion para llamar a
		"""
		form=estadisticas.Form(self)
		form.rejected.connect(self.dato_nuevo)
		form.exec_()
	
	def compra(self):
	        """
	        Funcion para inicializar una nueva compra
	        """
		form=datos_compra.Form(self)
		form.rejected.connect(self.dato_nuevo)
		form.exec_()
	
	def agregar_dato(self):
	        """
	        Funcion para tomar un nuevo dato a agregar
	        """
		form=agregar.Form(self)
		form.rejected.connect(self.dato_nuevo)
		form.exec_()
	
	def cargar_buscar(self):
	        """
	        funcion para buscar y filtrar
	        """
		dato = self.ui.line_buscar.text()
		prod = controller.buscar_producto(dato)
		self.cargar_productos(prod)

	def eliminar_dato(self):
	        """
	        Funcion para eliminar un dato selccionado
	        """
        	model = self.ui.tabla.model()
        	index = self.ui.tabla.currentIndex()
        	if index.row() == -1: 
            		self.errorMessageDialog = QtGui.QErrorMessage(self)
            		self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            		return False
        	else:
            		codigo = model.index(index.row(),0, QtCore.QModelIndex()).data()
            	if (controller.delete(codigo)):
                	self.cargar_productos()
                	msgBox = QtGui.QMessageBox()
                	msgBox.setText("EL registro fue eliminado.")
                	msgBox.exec_()
                	return True
            	else:
                	self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
                	self.ui.errorMessageDialog.showMessage("Error al eliminar el registro")
                	return False
            		
	def editar_dato(self):
	        """
	        Funcion para editar un dato seleccionado
	        """
		model = self.ui.tabla.model()
        	index = self.ui.tabla.currentIndex()
        	if index.row() == -1: 
            		self.errorMessageDialog = QtGui.QErrorMessage(self)
            		self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            		return False
        	else:
			
            		codigo = model.index(index.row(),0, QtCore.QModelIndex()).data()
			nombre=model.index(index.row(),1, QtCore.QModelIndex()).data()
        		descripcion=model.index(index.row(),2, QtCore.QModelIndex()).data()
        		marca=model.index(index.row(),3, QtCore.QModelIndex()).data()
        		color=model.index(index.row(),4, QtCore.QModelIndex()).data()
        		
			
			form=editar.Form(self,codigo,nombre,descripcion,marca,color)
			form.rejected.connect(self.dato_nuevo)
			form.exec_()
	
	def dato_nuevo(self):
	        self.cargar_productos()   
        
        def cargar_productos(self, producto=None):
	        """
	        Funcion para cargar datos en la grilla
	        """
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
		self.ui.tabla.setModel(self.model)
		self.ui.tabla.setColumnWidth(0, 90)
		self.ui.tabla.setColumnWidth(1, 150)
		self.ui.tabla.setColumnWidth(2, 150)
		self.ui.tabla.setColumnWidth(3, 150)
		self.ui.tabla.setColumnWidth(4, 150)

"""
Funcion prinicpal para inicializar la aplicacion
"""
def run():
    app = QtGui.QApplication(sys.argv)
    main = Productos()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
