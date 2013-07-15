# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_compras.ui'
#
# Created: Sun Jul 14 16:03:56 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(764, 578)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabla = QtGui.QTableView(self.centralwidget)
        self.tabla.setGeometry(QtCore.QRect(20, 110, 721, 361))
        self.tabla.setObjectName("tabla")
        self.line_buscar = QtGui.QLineEdit(self.centralwidget)
        self.line_buscar.setGeometry(QtCore.QRect(20, 70, 611, 27))
        self.line_buscar.setObjectName("line_buscar")
        self.btn_buscar = QtGui.QPushButton(self.centralwidget)
        self.btn_buscar.setGeometry(QtCore.QRect(640, 70, 98, 27))
        self.btn_buscar.setObjectName("btn_buscar")
        self.eliminar_btn = QtGui.QPushButton(self.centralwidget)
        self.eliminar_btn.setGeometry(QtCore.QRect(20, 500, 98, 27))
        self.eliminar_btn.setObjectName("eliminar_btn")
        self.editar_btn = QtGui.QPushButton(self.centralwidget)
        self.editar_btn.setGeometry(QtCore.QRect(130, 500, 98, 27))
        self.editar_btn.setObjectName("editar_btn")
        self.agregar_btn = QtGui.QPushButton(self.centralwidget)
        self.agregar_btn.setGeometry(QtCore.QRect(240, 500, 98, 27))
        self.agregar_btn.setObjectName("agregar_btn")
        self.compra_btn = QtGui.QPushButton(self.centralwidget)
        self.compra_btn.setGeometry(QtCore.QRect(540, 490, 201, 51))
        self.compra_btn.setObjectName("compra_btn")
        self.estadisticas_btn = QtGui.QPushButton(self.centralwidget)
        self.estadisticas_btn.setGeometry(QtCore.QRect(380, 490, 151, 51))
        self.estadisticas_btn.setObjectName("estadisticas_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Compras", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_buscar.setText(QtGui.QApplication.translate("MainWindow", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.eliminar_btn.setText(QtGui.QApplication.translate("MainWindow", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.editar_btn.setText(QtGui.QApplication.translate("MainWindow", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.agregar_btn.setText(QtGui.QApplication.translate("MainWindow", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.compra_btn.setText(QtGui.QApplication.translate("MainWindow", "Nueva Compra", None, QtGui.QApplication.UnicodeUTF8))
        self.estadisticas_btn.setText(QtGui.QApplication.translate("MainWindow", "Compras", None, QtGui.QApplication.UnicodeUTF8))
        
        self.btn_buscar.setIcon(QtGui.QIcon("buscar_prod.ico"))
        self.eliminar_btn.setIcon(QtGui.QIcon("eliminar_prod.ico"))
        self.editar_btn.setIcon(QtGui.QIcon("editar_prod.ico"))
        self.agregar_btn.setIcon(QtGui.QIcon("agregar_prod.ico"))
        self.compra_btn.setIcon(QtGui.QIcon("nueva_compra.ico"))
        self.compra_btn.setIconSize(QtCore.QSize(45,45))
        self.estadisticas_btn.setIcon(QtGui.QIcon("compras.ico"))
	self.estadisticas_btn.setIconSize(QtCore.QSize(45,45))

