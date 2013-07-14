# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_editar_producto.ui'
#
# Created: Sun Jul 14 17:56:34 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 201)
        self.btn_salir = QtGui.QPushButton(Form)
        self.btn_salir.setGeometry(QtCore.QRect(297, 150, 81, 27))
        self.btn_salir.setObjectName("btn_salir")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(5, 40, 111, 20))
        self.label.setObjectName("label")
        self.line_precio = QtGui.QLineEdit(Form)
        self.line_precio.setGeometry(QtCore.QRect(120, 30, 261, 27))
        self.line_precio.setObjectName("line_precio")
        self.line_cantidad = QtGui.QLineEdit(Form)
        self.line_cantidad.setGeometry(QtCore.QRect(120, 70, 261, 27))
        self.line_cantidad.setObjectName("line_cantidad")
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 66, 17))
        self.label_2.setObjectName("label_2")
        self.line_descuento = QtGui.QLineEdit(Form)
        self.line_descuento.setGeometry(QtCore.QRect(120, 110, 261, 27))
        self.line_descuento.setObjectName("line_descuento")
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(25, 110, 81, 20))
        self.label_3.setObjectName("label_3")
        self.btn_aceptar = QtGui.QPushButton(Form)
        self.btn_aceptar.setGeometry(QtCore.QRect(200, 150, 81, 27))
        self.btn_aceptar.setObjectName("btn_aceptar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Especificaciones del producto", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_salir.setText(QtGui.QApplication.translate("Form", "Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Precio unitario:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Cantidad:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Descuento:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_aceptar.setText(QtGui.QApplication.translate("Form", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))

