# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_win.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(724, 361)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0.187, y1:0.818455, x2:1, y2:0, stop:0.137931 rgba(44, 134, 145, 206), stop:0.970443 rgba(178, 147, 200, 255));\n"
"font: 700 14pt \"Noto Sans Oriya\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_coordinate = QLabel(self.centralwidget)
        self.label_coordinate.setObjectName(u"label_coordinate")
        self.label_coordinate.setGeometry(QRect(30, 30, 321, 41))
        self.label_coordinate.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid rgba(255, 25, 255, 70);\n"
"border-radius: 7px;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 80, 31, 31))
        font = QFont()
        font.setFamilies([u"Noto Sans Oriya"])
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid rgba(255, 25, 255, 70);\n"
"border-radius: 7px;")
        self.label_coor_cel = QLabel(self.centralwidget)
        self.label_coor_cel.setObjectName(u"label_coor_cel")
        self.label_coor_cel.setGeometry(QRect(370, 30, 321, 41))
        self.label_coor_cel.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid rgba(255, 25, 255, 70);\n"
"border-radius: 7px;")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 130, 211, 41))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid rgba(255, 25, 255, 70);\n"
"border-radius: 7px;")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(250, 130, 31, 41))
        self.label_10.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid rgba(255, 25, 255, 70);\n"
"border-radius: 7px;")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(370, 130, 211, 41))
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid rgba(255, 25, 255, 70);\n"
"border-radius: 7px;")
        self.label_11.setTextFormat(Qt.AutoText)
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(590, 130, 31, 41))
        self.label_12.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid rgba(255, 25, 255, 70);\n"
"border-radius: 7px;")
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(30, 190, 211, 41))
        self.label_13.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid rgba(255, 25, 255, 70);\n"
"border-radius: 7px;")
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(250, 190, 31, 41))
        self.label_14.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid rgba(255, 25, 255, 70);\n"
"border-radius: 7px;")
        self.pushButton_calculate = QPushButton(self.centralwidget)
        self.pushButton_calculate.setObjectName(u"pushButton_calculate")
        self.pushButton_calculate.setGeometry(QRect(360, 180, 331, 51))
        self.pushButton_calculate.setStyleSheet(u"QPushButton {background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid rgba(255, 25, 255, 80);\n"
"border-radius: 10px;}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255, 80);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255, 100);\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_calculate.setAutoDefault(False)
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(30, 290, 211, 41))
        self.label_15.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid rgba(255, 25, 255, 70);\n"
"border-radius: 7px;")
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(370, 290, 211, 41))
        self.label_16.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid rgba(255, 25, 255, 70);\n"
"border-radius: 7px;")
        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(250, 290, 101, 41))
        self.label_17.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid rgba(255, 25, 255, 70);\n"
"border-radius: 7px;")
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(590, 290, 101, 41))
        self.label_18.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid rgba(255, 25, 255, 70);\n"
"border-radius: 7px;")
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(140, 80, 31, 31))
        self.label_19.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid rgba(255, 25, 255, 70);\n"
"border-radius: 7px;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(250, 80, 31, 31))
        self.label_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid rgba(255, 25, 255, 70);\n"
"border-radius: 7px;")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(370, 80, 31, 31))
        self.label_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid rgba(255, 25, 255, 70);\n"
"border-radius: 7px;")
        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(480, 80, 31, 31))
        self.label_20.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid rgba(255, 25, 255, 70);\n"
"border-radius: 7px;")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(590, 80, 31, 31))
        self.label_5.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid rgba(255, 25, 255, 70);\n"
"border-radius: 7px;")
        self.lineEdit_x0 = QLineEdit(self.centralwidget)
        self.lineEdit_x0.setObjectName(u"lineEdit_x0")
        self.lineEdit_x0.setGeometry(QRect(60, 80, 71, 31))
        self.lineEdit_x0.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid rgba(255, 25, 255, 70);\n"
"border-radius: 7px;")
        self.lineEdit_y0 = QLineEdit(self.centralwidget)
        self.lineEdit_y0.setObjectName(u"lineEdit_y0")
        self.lineEdit_y0.setGeometry(QRect(170, 80, 71, 31))
        self.lineEdit_y0.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid rgba(255, 25, 255, 70);\n"
"border-radius: 7px;")
        self.lineEdit_z0 = QLineEdit(self.centralwidget)
        self.lineEdit_z0.setObjectName(u"lineEdit_z0")
        self.lineEdit_z0.setGeometry(QRect(280, 80, 71, 31))
        self.lineEdit_z0.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid rgba(255, 25, 255, 70);\n"
"border-radius: 7px;")
        self.lineEdit_v0 = QLineEdit(self.centralwidget)
        self.lineEdit_v0.setObjectName(u"lineEdit_v0")
        self.lineEdit_v0.setGeometry(QRect(280, 130, 71, 41))
        self.lineEdit_v0.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid rgba(255, 25, 255, 70);\n"
"border-radius: 7px;")
        self.lineEdit_R = QLineEdit(self.centralwidget)
        self.lineEdit_R.setObjectName(u"lineEdit_R")
        self.lineEdit_R.setGeometry(QRect(280, 190, 71, 41))
        self.lineEdit_R.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid rgba(255, 25, 255, 70);\n"
"border-radius: 7px;")
        self.lineEdit_x = QLineEdit(self.centralwidget)
        self.lineEdit_x.setObjectName(u"lineEdit_x")
        self.lineEdit_x.setGeometry(QRect(400, 80, 71, 31))
        self.lineEdit_x.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid rgba(255, 25, 255, 70);\n"
"border-radius: 7px;")
        self.lineEdit_y = QLineEdit(self.centralwidget)
        self.lineEdit_y.setObjectName(u"lineEdit_y")
        self.lineEdit_y.setGeometry(QRect(510, 80, 71, 31))
        self.lineEdit_y.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid rgba(255, 25, 255, 70);\n"
"border-radius: 7px;")
        self.lineEdit_z = QLineEdit(self.centralwidget)
        self.lineEdit_z.setObjectName(u"lineEdit_z")
        self.lineEdit_z.setGeometry(QRect(620, 80, 71, 31))
        self.lineEdit_z.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid rgba(255, 25, 255, 70);\n"
"border-radius: 7px;")
        self.lineEdit_g = QLineEdit(self.centralwidget)
        self.lineEdit_g.setObjectName(u"lineEdit_g")
        self.lineEdit_g.setGeometry(QRect(620, 130, 71, 41))
        self.lineEdit_g.setStyleSheet(u"background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid rgba(255, 25, 255, 70);\n"
"border-radius: 7px;")
        self.pushButton_send = QPushButton(self.centralwidget)
        self.pushButton_send.setObjectName(u"pushButton_send")
        self.pushButton_send.setGeometry(QRect(360, 240, 331, 41))
        self.pushButton_send.setStyleSheet(u"QPushButton {background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid rgba(255, 25, 255, 80);\n"
"border-radius: 10px;}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255, 80);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_get = QPushButton(self.centralwidget)
        self.pushButton_get.setObjectName(u"pushButton_get")
        self.pushButton_get.setGeometry(QRect(30, 240, 321, 41))
        self.pushButton_get.setStyleSheet(u"QPushButton {background-color: rgba(255, 255, 255, 60);\n"
"border: 1px solid rgba(255, 25, 255, 80);\n"
"border-radius: 10px;}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255, 80);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255, 100);\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_coordinate.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b \u043a\u0430\u0442\u0430\u043f\u0443\u043b\u044c\u0442\u044b", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">X0:</span></p></body></html>", None))
        self.label_coor_cel.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b \u0446\u0435\u043b\u0438", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u0430\u044f \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">V0:</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">\u0423\u0441\u043a\u043e\u0440\u0435\u043d\u0438\u0435 \u0441\u0432/\u043f\u0430\u0434\u0435\u043d\u0438\u044f</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">g:</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u0420\u0430\u0434\u0438\u0443\u0441 \u0441\u0444\u0435\u0440\u044b \u043f\u043e\u0440\u0430\u0436\u0435\u043d\u0438\u044f</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">R:</span></p></body></html>", None))
        self.pushButton_calculate.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u0423\u0433\u043e\u043b \u0430\u0437\u0438\u043c\u0443\u0442\u0430\u043b\u044c\u043d\u044b\u0439</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u0423\u0433\u043e\u043b \u043f\u043e\u043b\u044f\u0440\u043d\u044b\u0439</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">R:</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">R:</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Y0:</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Z0:</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">X:</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Y:</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Z:</span></p></body></html>", None))
        self.pushButton_send.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u043e\u0442\u0432\u0435\u0442", None))
        self.pushButton_get.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u043e\u0442\u0432\u0435\u0442", None))
    # retranslateUi

