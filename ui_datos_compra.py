# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_datos_compra.ui'
#
# Created: Mon Jul 15 03:59:39 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(309, 166)
        self.aceptar = QtGui.QPushButton(Form)
        self.aceptar.setGeometry(QtCore.QRect(20, 120, 98, 27))
        self.aceptar.setObjectName("aceptar")
        self.cancelar = QtGui.QPushButton(Form)
        self.cancelar.setGeometry(QtCore.QRect(190, 120, 98, 27))
        self.cancelar.setObjectName("cancelar")
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.label_2.setObjectName("label_2")
        self.proveedor = QtGui.QLineEdit(Form)
        self.proveedor.setGeometry(QtCore.QRect(120, 20, 171, 27))
        self.proveedor.setObjectName("proveedor")
        self.descripcion = QtGui.QLineEdit(Form)
        self.descripcion.setGeometry(QtCore.QRect(120, 70, 171, 27))
        self.descripcion.setObjectName("descripcion")
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 91, 17))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.aceptar.setText(QtGui.QApplication.translate("Form", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelar.setText(QtGui.QApplication.translate("Form", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Proveedor:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Descripcion:", None, QtGui.QApplication.UnicodeUTF8))

	#------------__ICONO_-------------------------------------#
	self.aceptar.setIcon(QtGui.QIcon("aceptar_accion.ico"))
	self.cancelar.setIcon(QtGui.QIcon("cancelar_accion.ico"))