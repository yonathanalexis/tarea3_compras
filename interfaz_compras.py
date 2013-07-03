#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PySide import QtGui, QtCore
import controller
from ui_compras import Ui_MainWindow

class Productos(QtGui.QMainWindow):

	def __init__(self):
		  super(Productos,self).__init__()
		  self.ui =  Ui_MainWindow()        
		  self.ui.setupUi(self)
		  self.cargar_productos()
		  self.show()
		  

        def cargar_productos(self, producto=None):
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
	

def run():
    app = QtGui.QApplication(sys.argv)
    main = Productos()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
