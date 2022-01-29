# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(671, 496)
        self.help = QAction(MainWindow)
        self.help.setObjectName(u"help")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.log_text = QTextEdit(self.centralwidget)
        self.log_text.setObjectName(u"log_text")
        self.log_text.setGeometry(QRect(0, 190, 671, 291))
        self.labe = QLabel(self.centralwidget)
        self.labe.setObjectName(u"labe")
        self.labe.setGeometry(QRect(30, 20, 54, 12))
        self.ssid = QLineEdit(self.centralwidget)
        self.ssid.setObjectName(u"ssid")
        self.ssid.setGeometry(QRect(70, 20, 131, 20))
        self.time = QLineEdit(self.centralwidget)
        self.time.setObjectName(u"time")
        self.time.setGeometry(QRect(540, 20, 91, 20))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(470, 20, 54, 12))
        self.password = QLineEdit(self.centralwidget)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(310, 20, 131, 20))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(240, 20, 54, 12))
        self.connect = QPushButton(self.centralwidget)
        self.connect.setObjectName(u"connect")
        self.connect.setGeometry(QRect(140, 60, 75, 23))
        self.disconnect = QPushButton(self.centralwidget)
        self.disconnect.setObjectName(u"disconnect")
        self.disconnect.setGeometry(QRect(250, 60, 75, 23))
        self.labe_2 = QLabel(self.centralwidget)
        self.labe_2.setObjectName(u"labe_2")
        self.labe_2.setGeometry(QRect(30, 120, 91, 16))
        self.cur_ssid = QTextEdit(self.centralwidget)
        self.cur_ssid.setObjectName(u"cur_ssid")
        self.cur_ssid.setGeometry(QRect(140, 110, 241, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 160, 101, 16))
        self.interface_name = QTextEdit(self.centralwidget)
        self.interface_name.setObjectName(u"interface_name")
        self.interface_name.setGeometry(QRect(140, 150, 241, 31))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(450, 70, 54, 12))
        self.frequency = QLineEdit(self.centralwidget)
        self.frequency.setObjectName(u"frequency")
        self.frequency.setGeometry(QRect(540, 70, 91, 20))
        self.test = QPushButton(self.centralwidget)
        self.test.setObjectName(u"test")
        self.test.setGeometry(QRect(550, 110, 75, 23))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(470, 70, 61, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 671, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.help)
        self.menuFile.addSeparator()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WIFI-Test", None))
        self.help.setText(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9\u4fe1\u606f", None))
        self.labe.setText(QCoreApplication.translate("MainWindow", u"SSID:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Time(s):", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.disconnect.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.labe_2.setText(QCoreApplication.translate("MainWindow", u"Connected SSID:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Interface Name:", None))
        self.label_4.setText("")
        self.test.setText(QCoreApplication.translate("MainWindow", u"Test", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Frequency:", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"help", None))
    # retranslateUi

