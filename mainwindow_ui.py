# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_ui.ui'
#
# Created: Sun Mar 22 13:58:56 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 441)
        MainWindow.setMinimumSize(QtCore.QSize(800, 441))
        MainWindow.setMaximumSize(QtCore.QSize(800, 441))
        MainWindow.setBaseSize(QtCore.QSize(800, 441))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lineEdit_input = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_input.setGeometry(QtCore.QRect(10, 5, 291, 27))
        self.lineEdit_input.setObjectName(_fromUtf8("lineEdit_input"))
        self.pushButton_translate = QtGui.QPushButton(self.centralwidget)
        self.pushButton_translate.setGeometry(QtCore.QRect(310, 5, 98, 27))
        self.pushButton_translate.setObjectName(_fromUtf8("pushButton_translate"))
        self.comboBox_from = QtGui.QComboBox(self.centralwidget)
        self.comboBox_from.setGeometry(QtCore.QRect(500, 5, 78, 27))
        self.comboBox_from.setObjectName(_fromUtf8("comboBox_from"))
        self.comboBox_from.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 10, 71, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(610, 10, 81, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.comboBox_to = QtGui.QComboBox(self.centralwidget)
        self.comboBox_to.setGeometry(QtCore.QRect(700, 5, 78, 27))
        self.comboBox_to.setObjectName(_fromUtf8("comboBox_to"))
        self.comboBox_to.addItem(_fromUtf8(""))
        self.comboBox_to.addItem(_fromUtf8(""))
        self.textEdit_main = QtGui.QTextBrowser(self.centralwidget)
        self.textEdit_main.setGeometry(QtCore.QRect(10, 70, 781, 361))
        self.textEdit_main.setReadOnly(True)
        self.textEdit_main.setObjectName(_fromUtf8("textEdit_main"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 45, 631, 17))
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Dict", None))
        self.pushButton_translate.setText(_translate("MainWindow", "Translate", None))
        self.comboBox_from.setItemText(0, _translate("MainWindow", "en", None))
        self.label.setText(_translate("MainWindow", "Lang from", None))
        self.label_2.setText(_translate("MainWindow", "Lang to", None))
        self.comboBox_to.setItemText(0, _translate("MainWindow", "en", None))
        self.comboBox_to.setItemText(1, _translate("MainWindow", "ru", None))
        self.label_3.setText(_translate("MainWindow", "«Реализовано с помощью сервиса «Яндекс.Словарь» <a href=\"http://tech.yandex.ru/dictionary/\">http://tech.yandex.ru/dictionary/</a>", None))

