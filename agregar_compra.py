# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_compras_prod.ui'
#
# Created: Sat Jul 13 23:16:06 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        self.buscar_prod_2 = QtGui.QPushButton(Form)
        self.buscar_prod_2.setGeometry(QtCore.QRect(10, 10, 98, 27))
        self.buscar_prod_2.setObjectName("buscar_prod_2")
        self.buscar_prod = QtGui.QLineEdit(Form)
        self.buscar_prod.setGeometry(QtCore.QRect(140, 10, 641, 27))
        self.buscar_prod.setObjectName("buscar_prod")
        self.tabla_prod = QtGui.QTableView(Form)
        self.tabla_prod.setGeometry(QtCore.QRect(10, 51, 771, 201))
        self.tabla_prod.setObjectName("tabla_prod")
        self.agregar_prod = QtGui.QPushButton(Form)
        self.agregar_prod.setGeometry(QtCore.QRect(10, 260, 121, 41))
        self.agregar_prod.setObjectName("agregar_prod")
        self.tabla_compra = QtGui.QTableView(Form)
        self.tabla_compra.setGeometry(QtCore.QRect(10, 320, 771, 192))
        self.tabla_compra.setObjectName("tabla_compra")
        self.eliminar_prod = QtGui.QPushButton(Form)
        self.eliminar_prod.setGeometry(QtCore.QRect(20, 540, 98, 27))
        self.eliminar_prod.setObjectName("eliminar_prod")
        self.editar_prod = QtGui.QPushButton(Form)
        self.editar_prod.setGeometry(QtCore.QRect(130, 540, 98, 27))
        self.editar_prod.setObjectName("editar_prod")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(490, 540, 101, 17))
        self.label.setObjectName("label")
        self.total_compra = QtGui.QPlainTextEdit(Form)
        self.total_compra.setGeometry(QtCore.QRect(590, 520, 191, 51))
        self.total_compra.setObjectName("total_compra")

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

