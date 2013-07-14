# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_formulario_compra.ui'
#
# Created: Sun Jul 14 00:03:50 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(362, 168)
        self.agregar = QtGui.QPushButton(Form)
        self.agregar.setGeometry(QtCore.QRect(110, 130, 98, 27))
        self.agregar.setObjectName("agregar")
        self.cancelar = QtGui.QPushButton(Form)
        self.cancelar.setGeometry(QtCore.QRect(240, 130, 98, 27))
        self.cancelar.setObjectName("cancelar")
        self.precio = QtGui.QLineEdit(Form)
        self.precio.setGeometry(QtCore.QRect(190, 50, 151, 27))
        self.precio.setObjectName("precio")
        self.cantidad = QtGui.QLineEdit(Form)
        self.cantidad.setGeometry(QtCore.QRect(190, 90, 151, 27))
        self.cantidad.setObjectName("cantidad")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 66, 17))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 50, 111, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(110, 90, 66, 17))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.agregar.setText(QtGui.QApplication.translate("Form", "agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelar.setText(QtGui.QApplication.translate("Form", "cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.precio.setPlaceholderText(QtGui.QApplication.translate("Form", "Ingresar Precio", None, QtGui.QApplication.UnicodeUTF8))
        self.cantidad.setPlaceholderText(QtGui.QApplication.translate("Form", "Ingresar Cantidad", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Producto", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Precio unitario:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Cantidad:", None, QtGui.QApplication.UnicodeUTF8))

