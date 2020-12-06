# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1200, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 600))
        MainWindow.setMouseTracking(False)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_input = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_input.setGeometry(QtCore.QRect(550, 130, 101, 31))
        self.pushButton_input.setStyleSheet("background-image:url(:/png/img/import.png);")
        self.pushButton_input.setText("")
        self.pushButton_input.setObjectName("pushButton_input")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(550, 190, 101, 91))
        self.textEdit.setStyleSheet("color:rgb(255, 0, 0);\n"
"placeholderText:请输入字符！;")
        self.textEdit.setObjectName("textEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(550, 310, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.pushButton_conversion = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_conversion.setGeometry(QtCore.QRect(550, 360, 101, 101))
        self.pushButton_conversion.setStyleSheet("background-image:url(:/png/img/conversion.png);")
        self.pushButton_conversion.setText("")
        self.pushButton_conversion.setObjectName("pushButton_conversion")
        self.input_img = QtWidgets.QLabel(self.centralwidget)
        self.input_img.setGeometry(QtCore.QRect(30, 80, 501, 501))
        self.input_img.setScaledContents(True)
        self.input_img.setObjectName("input_img")
        self.export_img = QtWidgets.QLabel(self.centralwidget)
        self.export_img.setGeometry(QtCore.QRect(670, 80, 501, 501))
        self.export_img.setScaledContents(True)
        self.export_img.setObjectName("export_img")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.loding = QtWidgets.QLabel(self.centralwidget)
        self.loding.setGeometry(QtCore.QRect(550, 250, 100, 100))
        self.loding.setText("")
        self.loding.setObjectName("loding")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">请输入字符！</p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "清晰"))
        self.input_img.setText(_translate("MainWindow", "TextLabel"))
        self.export_img.setText(_translate("MainWindow", "TextLabel"))
import img_qc_rc