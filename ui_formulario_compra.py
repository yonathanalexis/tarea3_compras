# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_formulario_compra.ui'
#
# Created: Mon Jul 15 02:18:48 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(362, 211)
        self.agregar = QtGui.QPushButton(Form)
        self.agregar.setGeometry(QtCore.QRect(110, 170, 98, 27))
        self.agregar.setObjectName("agregar")
        self.cancelar = QtGui.QPushButton(Form)
        self.cancelar.setGeometry(QtCore.QRect(250, 170, 98, 27))
        self.cancelar.setObjectName("cancelar")
        self.precio = QtGui.QLineEdit(Form)
        self.precio.setGeometry(QtCore.QRect(140, 30, 211, 27))
        self.precio.setObjectName("precio")
        self.cantidad = QtGui.QLineEdit(Form)
        self.cantidad.setGeometry(QtCore.QRect(140, 130, 211, 27))
        self.cantidad.setObjectName("cantidad")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 66, 17))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 111, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(70, 130, 71, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(60, 80, 91, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(295, 70, 71, 41))
        self.label_5.setObjectName("label_5")
        self.descuento = QtGui.QLineEdit(Form)
        self.descuento.setGeometry(QtCore.QRect(140, 80, 141, 27))
        self.descuento.setObjectName("descuento")

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
        self.label_4.setText(QtGui.QApplication.translate("Form", "Descuento:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.descuento.setPlaceholderText(QtGui.QApplication.translate("Form", "Ingresar Descuento", None, QtGui.QApplication.UnicodeUTF8))

	#------------__ICONO_-------------------------------------#
	self.agregar.setIcon(QtGui.QIcon("agregar.ico"))
	self.cancelar.setIcon(QtGui.QIcon("cancelar.ico"))
