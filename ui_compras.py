# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_compras.ui'
#
# Created: Thu Jun 27 12:17:49 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabla = QtGui.QTableView(self.centralwidget)
        self.tabla.setGeometry(QtCore.QRect(60, 130, 511, 271))
        self.tabla.setObjectName("tabla")
        self.line_buscar = QtGui.QLineEdit(self.centralwidget)
        self.line_buscar.setGeometry(QtCore.QRect(60, 70, 331, 27))
        self.line_buscar.setObjectName("line_buscar")
        self.btn_buscar = QtGui.QPushButton(self.centralwidget)
        self.btn_buscar.setGeometry(QtCore.QRect(450, 70, 98, 27))
        self.btn_buscar.setObjectName("btn_buscar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Compras", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_buscar.setText(QtGui.QApplication.translate("MainWindow", "boton", None, QtGui.QApplication.UnicodeUTF8))

