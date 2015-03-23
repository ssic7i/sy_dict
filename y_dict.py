# -*- coding: utf-8 -*-
__author__ = 'sergy'

from PyQt4 import QtCore, QtGui
import dict_lib
import sys
import codecs

from mainwindow_ui import Ui_MainWindow


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_translate.clicked.connect(self.check)

    def check(self):
        dict_obj = dict_lib.yandex_dict(r'dict.1.1.20150322T002854Z.38fd5bd1400255a5.3fb3a505a42b20fb5b4113643d35d84ba3916d32')
        text_in = str(unicode(self.ui.lineEdit_input.text()).encode('utf-8'))
        words = dict_obj.check_text(text_in, str(self.ui.comboBox_from.currentText()) + '-' + str(self.ui.comboBox_to.currentText()))
        self.ui.textEdit_main.clear()
        result_text = ''
        for word in words:
            result_text = result_text + word + '<br>'
        result_text = result_text + '<br>'
        self.ui.textEdit_main.insertHtml(result_text)

    # http://stackoverflow.com/questions/5506781/pyqt4-application-on-windows-is-crashing-on-exit
    def closeEvent(self, event):
        sys.exit(0)


app = QtGui.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())