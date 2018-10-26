# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        MainWindow.resize(671, 496)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.log_text = QtGui.QTextEdit(self.centralwidget)
        self.log_text.setGeometry(QtCore.QRect(0, 190, 671, 291))
        self.log_text.setObjectName(_fromUtf8("log_text"))
        self.labe = QtGui.QLabel(self.centralwidget)
        self.labe.setGeometry(QtCore.QRect(30, 20, 54, 12))
        self.labe.setObjectName(_fromUtf8("labe"))
        self.ssid = QtGui.QLineEdit(self.centralwidget)
        self.ssid.setGeometry(QtCore.QRect(70, 20, 131, 20))
        self.ssid.setObjectName(_fromUtf8("ssid"))
        self.time = QtGui.QLineEdit(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(540, 20, 91, 20))
        self.time.setObjectName(_fromUtf8("time"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(470, 20, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.password = QtGui.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(310, 20, 131, 20))
        self.password.setObjectName(_fromUtf8("password"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 20, 54, 12))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.connect = QtGui.QPushButton(self.centralwidget)
        self.connect.setGeometry(QtCore.QRect(140, 60, 75, 23))
        self.connect.setObjectName(_fromUtf8("connect"))
        self.disconnect = QtGui.QPushButton(self.centralwidget)
        self.disconnect.setGeometry(QtCore.QRect(250, 60, 75, 23))
        self.disconnect.setObjectName(_fromUtf8("disconnect"))
        self.labe_2 = QtGui.QLabel(self.centralwidget)
        self.labe_2.setGeometry(QtCore.QRect(30, 120, 91, 16))
        self.labe_2.setObjectName(_fromUtf8("labe_2"))
        self.cur_ssid = QtGui.QTextEdit(self.centralwidget)
        self.cur_ssid.setGeometry(QtCore.QRect(140, 110, 241, 31))
        self.cur_ssid.setObjectName(_fromUtf8("cur_ssid"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 160, 101, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.interface_name = QtGui.QTextEdit(self.centralwidget)
        self.interface_name.setGeometry(QtCore.QRect(140, 150, 241, 31))
        self.interface_name.setObjectName(_fromUtf8("interface_name"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(450, 70, 54, 12))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.frequency = QtGui.QLineEdit(self.centralwidget)
        self.frequency.setGeometry(QtCore.QRect(540, 70, 91, 20))
        self.frequency.setObjectName(_fromUtf8("frequency"))
        self.test = QtGui.QPushButton(self.centralwidget)
        self.test.setGeometry(QtCore.QRect(550, 110, 75, 23))
        self.test.setObjectName(_fromUtf8("test"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(470, 70, 61, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 671, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.help = QtGui.QAction(MainWindow)
        self.help.setObjectName(_fromUtf8("help"))
        self.menuFile.addAction(self.help)
        self.menuFile.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "无线客户端工具", None))
        self.labe.setText(_translate("MainWindow", "SSID:", None))
        self.label_2.setText(_translate("MainWindow", "Time(s):", None))
        self.label_3.setText(_translate("MainWindow", "Password:", None))
        self.connect.setText(_translate("MainWindow", "Connect", None))
        self.disconnect.setText(_translate("MainWindow", "Disconnect", None))
        self.labe_2.setText(_translate("MainWindow", "Connected SSID:", None))
        self.label.setText(_translate("MainWindow", "Interface Name:", None))
        self.test.setText(_translate("MainWindow", "Test", None))
        self.label_5.setText(_translate("MainWindow", "Frequency:", None))
        self.menuFile.setTitle(_translate("MainWindow", "help", None))
        self.help.setText(_translate("MainWindow", "帮助信息", None))

