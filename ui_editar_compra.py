# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_editar_compra.ui'
#
# Created: Sun Jul 14 18:08:18 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 477)
        self.tbl_compra = QtGui.QTableView(Form)
        self.tbl_compra.setGeometry(QtCore.QRect(10, 60, 421, 251))
        self.tbl_compra.setObjectName("tbl_compra")
        self.line_proveedor = QtGui.QLineEdit(Form)
        self.line_proveedor.setGeometry(QtCore.QRect(180, 360, 241, 27))
        self.line_proveedor.setObjectName("line_proveedor")
        self.line_descripcion = QtGui.QLineEdit(Form)
        self.line_descripcion.setGeometry(QtCore.QRect(180, 400, 241, 27))
        self.line_descripcion.setObjectName("line_descripcion")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 370, 81, 20))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(90, 410, 81, 20))
        self.label_2.setObjectName("label_2")
        self.btn_editar_prod = QtGui.QPushButton(Form)
        self.btn_editar_prod.setGeometry(QtCore.QRect(10, 320, 131, 27))
        self.btn_editar_prod.setObjectName("btn_editar_prod")
        self.btn_aceptar = QtGui.QPushButton(Form)
        self.btn_aceptar.setGeometry(QtCore.QRect(320, 440, 98, 27))
        self.btn_aceptar.setObjectName("btn_aceptar")
        self.btn_buscar = QtGui.QPushButton(Form)
        self.btn_buscar.setGeometry(QtCore.QRect(320, 20, 111, 27))
        self.btn_buscar.setObjectName("btn_buscar")
        self.line_buscar = QtGui.QLineEdit(Form)
        self.line_buscar.setGeometry(QtCore.QRect(12, 20, 301, 27))
        self.line_buscar.setObjectName("line_buscar")
        self.btn_eliminar = QtGui.QPushButton(Form)
        self.btn_eliminar.setGeometry(QtCore.QRect(330, 320, 98, 27))
        self.btn_eliminar.setObjectName("btn_eliminar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Editar Compra", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Proveedor:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Descripcion:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_editar_prod.setText(QtGui.QApplication.translate("Form", "Editar productos", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_aceptar.setText(QtGui.QApplication.translate("Form", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_buscar.setText(QtGui.QApplication.translate("Form", "buscar producto", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_eliminar.setText(QtGui.QApplication.translate("Form", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))

