# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_compras_prod.ui'
#
# Created: Mon Jul 15 21:30:01 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 619)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        self.buscar_prod_2 = QtGui.QPushButton(Form)
        self.buscar_prod_2.setGeometry(QtCore.QRect(10, 10, 98, 27))
        self.buscar_prod_2.setObjectName("buscar_prod_2")
        self.buscar_prod = QtGui.QLineEdit(Form)
        self.buscar_prod.setGeometry(QtCore.QRect(140, 10, 641, 27))
        self.buscar_prod.setObjectName("buscar_prod")
        self.tabla_prod = QtGui.QTableView(Form)
        self.tabla_prod.setGeometry(QtCore.QRect(10, 51, 771, 171))
        self.tabla_prod.setObjectName("tabla_prod")
        self.agregar_prod = QtGui.QPushButton(Form)
        self.agregar_prod.setGeometry(QtCore.QRect(10, 230, 121, 41))
        self.agregar_prod.setObjectName("agregar_prod")
        self.tabla_compra = QtGui.QTableView(Form)
        self.tabla_compra.setGeometry(QtCore.QRect(10, 281, 771, 231))
        self.tabla_compra.setObjectName("tabla_compra")
        self.eliminar_prod = QtGui.QPushButton(Form)
        self.eliminar_prod.setGeometry(QtCore.QRect(567, 236, 101, 31))
        self.eliminar_prod.setObjectName("eliminar_prod")
        self.editar_prod = QtGui.QPushButton(Form)
        self.editar_prod.setGeometry(QtCore.QRect(680, 236, 98, 31))
        self.editar_prod.setObjectName("editar_prod")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(480, 560, 101, 17))
        self.label.setObjectName("label")
        self.fin = QtGui.QPushButton(Form)
        self.fin.setGeometry(QtCore.QRect(20, 570, 131, 41))
        self.fin.setObjectName("fin")
        self.line_total = QtGui.QLineEdit(Form)
        self.line_total.setEnabled(False)
        self.line_total.setGeometry(QtCore.QRect(590, 550, 171, 41))
        self.line_total.setObjectName("line_total")
        self.cancelar_compra = QtGui.QPushButton(Form)
        self.cancelar_compra.setGeometry(QtCore.QRect(160, 570, 141, 41))
        self.cancelar_compra.setObjectName("cancelar_compra")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "compra_prod", None, QtGui.QApplication.UnicodeUTF8))
        self.buscar_prod_2.setText(QtGui.QApplication.translate("Form", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.buscar_prod.setPlaceholderText(QtGui.QApplication.translate("Form", "Ingrese producto a buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.agregar_prod.setText(QtGui.QApplication.translate("Form", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.eliminar_prod.setText(QtGui.QApplication.translate("Form", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.editar_prod.setText(QtGui.QApplication.translate("Form", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Total Compra:", None, QtGui.QApplication.UnicodeUTF8))
        self.fin.setText(QtGui.QApplication.translate("Form", "Guardar Compra", None, QtGui.QApplication.UnicodeUTF8))
        self.line_total.setPlaceholderText(QtGui.QApplication.translate("Form", "Total de la compra", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelar_compra.setText(QtGui.QApplication.translate("Form", "Cancelar Compra", None, QtGui.QApplication.UnicodeUTF8))

	#------------__ICONO_-------------------------------------#	
	self.buscar_prod_2.setIcon(QtGui.QIcon("buscar_compra.ico"))
	self.agregar_prod.setIcon(QtGui.QIcon("agregar_compra.ico"))
	self.agregar_prod.setIconSize(QtCore.QSize(45,45))
	self.eliminar_prod.setIcon(QtGui.QIcon("eliminar_compra.ico"))
	self.eliminar_prod.setIconSize(QtCore.QSize(25,25))
	self.editar_prod.setIcon(QtGui.QIcon("editar_compra.ico"))
	self.editar_prod.setIconSize(QtCore.QSize(25,25))
	self.fin.setIcon(QtGui.QIcon("finalizar_compra.ico"))
	self.fin.setIconSize(QtCore.QSize(25,25))
	self.cancelar_compra.setIcon(QtGui.QIcon("eliminar_prod.ico"))
	self.cancelar_compra.setIconSize(QtCore.QSize(25,25))