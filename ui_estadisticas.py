# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_estadisticas.ui'
#
# Created: Sun Jul 14 00:49:49 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(576, 595)
        self.tbl_compras = QtGui.QTableView(Form)
        self.tbl_compras.setGeometry(QtCore.QRect(20, 110, 531, 371))
        self.tbl_compras.setObjectName("tbl_compras")
        self.bus_compra = QtGui.QLineEdit(Form)
        self.bus_compra.setGeometry(QtCore.QRect(150, 30, 241, 27))
        self.bus_compra.setObjectName("bus_compra")
        self.bus_producto = QtGui.QLineEdit(Form)
        self.bus_producto.setGeometry(QtCore.QRect(150, 60, 241, 27))
        self.bus_producto.setObjectName("bus_producto")
        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 90, 551, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btn_buscar = QtGui.QPushButton(Form)
        self.btn_buscar.setGeometry(QtCore.QRect(400, 30, 141, 27))
        self.btn_buscar.setObjectName("btn_buscar")
        self.btn_editar = QtGui.QPushButton(Form)
        self.btn_editar.setGeometry(QtCore.QRect(120, 550, 98, 27))
        self.btn_editar.setObjectName("btn_editar")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 40, 66, 17))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 70, 66, 17))
        self.label_2.setObjectName("label_2")
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(10, 10, 551, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtGui.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(0, 20, 21, 521))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtGui.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(550, 20, 20, 521))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.btn_eliminar = QtGui.QPushButton(Form)
        self.btn_eliminar.setGeometry(QtCore.QRect(10, 550, 98, 27))
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.line_5 = QtGui.QFrame(Form)
        self.line_5.setGeometry(QtCore.QRect(10, 530, 551, 20))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.total_compras = QtGui.QLineEdit(Form)
        self.total_compras.setGeometry(QtCore.QRect(410, 500, 141, 27))
        self.total_compras.setObjectName("total_compras")
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(280, 510, 121, 20))
        self.label_3.setObjectName("label_3")
        self.btn_salir = QtGui.QPushButton(Form)
        self.btn_salir.setGeometry(QtCore.QRect(460, 550, 98, 27))
        self.btn_salir.setObjectName("btn_salir")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "compras registradas", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_buscar.setText(QtGui.QApplication.translate("Form", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_editar.setText(QtGui.QApplication.translate("Form", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Compra:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Producto:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_eliminar.setText(QtGui.QApplication.translate("Form", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "total de compras:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_salir.setText(QtGui.QApplication.translate("Form", "Salir", None, QtGui.QApplication.UnicodeUTF8))

	#------------__ICONO_-------------------------------------#
        self.btn_buscar.setIcon(QtGui.QIcon("buscar_prod.ico"))
        self.btn_editar.setIcon(QtGui.QIcon("editar_prod.ico"))
        self.btn_eliminar.setIcon(QtGui.QIcon("eliminar_prod.ico"))
        self.btn_salir.setIcon(QtGui.QIcon("cancelar.ico"))
