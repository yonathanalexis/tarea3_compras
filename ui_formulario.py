# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_formulario.ui'
#
# Created: Thu Jul  4 12:01:08 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(385, 325)
        Form.setToolTip("")
        Form.setWhatsThis("")
        Form.setAccessibleName("")
        self.agregar = QtGui.QPushButton(Form)
        self.agregar.setGeometry(QtCore.QRect(80, 260, 98, 27))
        self.agregar.setObjectName("agregar")
        self.cancelar = QtGui.QPushButton(Form)
        self.cancelar.setGeometry(QtCore.QRect(220, 260, 98, 27))
        self.cancelar.setObjectName("cancelar")
        self.codigo_prod = QtGui.QLineEdit(Form)
        self.codigo_prod.setGeometry(QtCore.QRect(210, 30, 151, 27))
        self.codigo_prod.setStatusTip("")
        self.codigo_prod.setWhatsThis("")
        self.codigo_prod.setAccessibleName("")
        self.codigo_prod.setInputMask("")
        self.codigo_prod.setText("")
        self.codigo_prod.setObjectName("codigo_prod")
        self.nombre_prod = QtGui.QLineEdit(Form)
        self.nombre_prod.setGeometry(QtCore.QRect(210, 70, 151, 27))
        self.nombre_prod.setObjectName("nombre_prod")
        self.descripcion_prod = QtGui.QLineEdit(Form)
        self.descripcion_prod.setGeometry(QtCore.QRect(210, 110, 151, 27))
        self.descripcion_prod.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.descripcion_prod.setObjectName("descripcion_prod")
        self.marca_prod = QtGui.QLineEdit(Form)
        self.marca_prod.setGeometry(QtCore.QRect(210, 150, 151, 27))
        self.marca_prod.setObjectName("marca_prod")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 30, 66, 17))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(90, 70, 81, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(90, 110, 101, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(90, 150, 66, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 81, 17))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(90, 200, 66, 17))
        self.label_7.setObjectName("label_7")
        self.color_prod = QtGui.QLineEdit(Form)
        self.color_prod.setGeometry(QtCore.QRect(210, 200, 151, 27))
        self.color_prod.setObjectName("color_prod")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Producto", None, QtGui.QApplication.UnicodeUTF8))
        self.agregar.setText(QtGui.QApplication.translate("Form", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelar.setText(QtGui.QApplication.translate("Form", "cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.codigo_prod.setPlaceholderText(QtGui.QApplication.translate("Form", "Ingresar Codigo", None, QtGui.QApplication.UnicodeUTF8))
        self.nombre_prod.setPlaceholderText(QtGui.QApplication.translate("Form", "Ingresar Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.descripcion_prod.setPlaceholderText(QtGui.QApplication.translate("Form", "Ingresar Descripción", None, QtGui.QApplication.UnicodeUTF8))
        self.marca_prod.setPlaceholderText(QtGui.QApplication.translate("Form", "Ingresar Marca", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Codigo:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Descripción:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Marca:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Producto", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "Color:", None, QtGui.QApplication.UnicodeUTF8))
        self.color_prod.setPlaceholderText(QtGui.QApplication.translate("Form", "Ingresar Color", None, QtGui.QApplication.UnicodeUTF8))

        #------------__ICONO_-------------------------------------#
	self.agregar.setIcon(QtGui.QIcon("agregar.ico"))
	self.cancelar.setIcon(QtGui.QIcon("cancelar.ico"))
