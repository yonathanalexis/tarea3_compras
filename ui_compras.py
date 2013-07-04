# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_compras.ui'
#
# Created: Thu Jul  4 12:11:35 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(764, 600)
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
        self.editar_btn.setGeometry(QtCore.QRect(140, 500, 98, 27))
        self.editar_btn.setObjectName("editar_btn")
        self.agregar_btn = QtGui.QPushButton(self.centralwidget)
        self.agregar_btn.setGeometry(QtCore.QRect(270, 500, 98, 27))
        self.agregar_btn.setObjectName("agregar_btn")
        self.compra_btn = QtGui.QPushButton(self.centralwidget)
        self.compra_btn.setGeometry(QtCore.QRect(540, 490, 201, 51))
        self.compra_btn.setObjectName("compra_btn")
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

