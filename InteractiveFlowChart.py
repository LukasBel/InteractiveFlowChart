# -*- coding: utf-8 -*-

# Interactive Flow Chart for CRIMJ 2022, Penn State Abington

# All right reserved to Penn State Abington.

# Date: 10/19/2022

from PyQt5 import QtCore, QtGui, QtWidgets
from SecondWindow import Ui_SecondWindow
import sys

class Ui_MainWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi_2(self.window)
        self.window.show()

    def toggle_window(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()

    def show_new_window(self, checked):
        self.w.show()

    def setupUi(self, MainWindow):
        self.buttonArray = []

        MainWindow.resize(1170, 860)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 10, 931, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setMouseTracking(True)
        self.label.setStyleSheet("color: rgb(132, 171, 243);")
        self.label.setMidLineWidth(1)
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton.setGeometry(QtCore.QRect(20, 140, 121, 91))
        self.pushButton.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(10, 60, 1151, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.splitter.setFont(font)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("border-radius: 7px;\n"
                                   "border: 1px solid black;")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("border-radius: 7px;\n"
                                   "border: 1px solid black;")
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("border-radius: 7px;\n"
                                   "border: 1px solid black;")
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("border-radius: 7px;\n"
                                   "border: 1px solid black;")
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(False)
        self.label_5.setIndent(-2)
        self.label_5.setObjectName("label_5")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_2.setGeometry(QtCore.QRect(20, 240, 121, 91))
        self.pushButton_2.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_3.setGeometry(QtCore.QRect(20, 340, 121, 91))
        self.pushButton_3.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_4.setGeometry(QtCore.QRect(20, 440, 121, 91))
        self.pushButton_4.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_4.setCheckable(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_5.setGeometry(QtCore.QRect(20, 540, 121, 91))
        self.pushButton_5.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_5.setCheckable(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_6.setGeometry(QtCore.QRect(150, 340, 121, 91))
        self.pushButton_6.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_6.setCheckable(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_7.setGeometry(QtCore.QRect(150, 440, 121, 91))
        self.pushButton_7.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_7.setCheckable(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_8.setGeometry(QtCore.QRect(150, 140, 121, 91))
        self.pushButton_8.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_8.setCheckable(False)
        self.pushButton_8.setAutoDefault(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_9.setGeometry(QtCore.QRect(150, 240, 121, 91))
        self.pushButton_9.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_9.setCheckable(False)
        self.pushButton_9.setAutoDefault(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_10.setGeometry(QtCore.QRect(150, 540, 121, 91))
        self.pushButton_10.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_10.setCheckable(False)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_11.setGeometry(QtCore.QRect(450, 140, 121, 91))
        self.pushButton_11.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_11.setCheckable(False)
        self.pushButton_11.setAutoDefault(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_12.setGeometry(QtCore.QRect(450, 540, 121, 91))
        self.pushButton_12.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_12.setCheckable(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_13.setGeometry(QtCore.QRect(320, 340, 121, 91))
        self.pushButton_13.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_13.setCheckable(False)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_14.setGeometry(QtCore.QRect(450, 340, 121, 91))
        self.pushButton_14.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_14.setCheckable(False)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_15.setGeometry(QtCore.QRect(450, 240, 121, 91))
        self.pushButton_15.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_15.setCheckable(False)
        self.pushButton_15.setAutoDefault(True)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_16.setGeometry(QtCore.QRect(320, 440, 121, 91))
        self.pushButton_16.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_16.setCheckable(False)
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_17.setGeometry(QtCore.QRect(320, 140, 121, 91))
        self.pushButton_17.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_17.setCheckable(False)
        self.pushButton_17.setAutoDefault(True)
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_18.setGeometry(QtCore.QRect(450, 440, 121, 91))
        self.pushButton_18.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_18.setCheckable(False)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_19.setGeometry(QtCore.QRect(320, 240, 121, 91))
        self.pushButton_19.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_19.setCheckable(False)
        self.pushButton_19.setAutoDefault(True)
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_20.setGeometry(QtCore.QRect(320, 540, 121, 91))
        self.pushButton_20.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_20.setCheckable(False)
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_21.setGeometry(QtCore.QRect(740, 140, 121, 91))
        self.pushButton_21.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_21.setCheckable(False)
        self.pushButton_21.setAutoDefault(True)
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_22.setGeometry(QtCore.QRect(740, 540, 121, 91))
        self.pushButton_22.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_22.setCheckable(False)
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_23.setGeometry(QtCore.QRect(610, 340, 121, 91))
        self.pushButton_23.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_23.setCheckable(False)
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_24.setGeometry(QtCore.QRect(740, 340, 121, 91))
        self.pushButton_24.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_24.setCheckable(False)
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_25.setGeometry(QtCore.QRect(740, 240, 121, 91))
        self.pushButton_25.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_25.setCheckable(False)
        self.pushButton_25.setAutoDefault(True)
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_26.setGeometry(QtCore.QRect(610, 440, 121, 91))
        self.pushButton_26.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_26.setCheckable(False)
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_27 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_27.setGeometry(QtCore.QRect(610, 140, 121, 91))
        self.pushButton_27.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_27.setCheckable(False)
        self.pushButton_27.setAutoDefault(True)
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_28 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_28.setGeometry(QtCore.QRect(740, 440, 121, 91))
        self.pushButton_28.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_28.setCheckable(False)
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_29 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_29.setGeometry(QtCore.QRect(610, 240, 121, 91))
        self.pushButton_29.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_29.setCheckable(False)
        self.pushButton_29.setAutoDefault(True)
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_30 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_30.setGeometry(QtCore.QRect(610, 540, 121, 91))
        self.pushButton_30.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_30.setCheckable(False)
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_31 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_31.setGeometry(QtCore.QRect(1030, 140, 121, 91))
        self.pushButton_31.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_31.setCheckable(False)
        self.pushButton_31.setAutoDefault(True)
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_32 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_32.setGeometry(QtCore.QRect(1030, 540, 121, 91))
        self.pushButton_32.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_32.setCheckable(False)
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_33 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_33.setGeometry(QtCore.QRect(900, 340, 121, 91))
        self.pushButton_33.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_33.setCheckable(False)
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_34 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_34.setGeometry(QtCore.QRect(1030, 340, 121, 91))
        self.pushButton_34.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_34.setCheckable(False)
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_35 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_35.setGeometry(QtCore.QRect(1030, 240, 121, 91))
        self.pushButton_35.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_35.setCheckable(False)
        self.pushButton_35.setAutoDefault(True)
        self.pushButton_35.setObjectName("pushButton_35")
        self.pushButton_36 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_36.setGeometry(QtCore.QRect(900, 440, 121, 91))
        self.pushButton_36.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_36.setCheckable(False)
        self.pushButton_36.setObjectName("pushButton_36")
        self.pushButton_37 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_37.setGeometry(QtCore.QRect(900, 140, 121, 91))
        self.pushButton_37.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_37.setCheckable(False)
        self.pushButton_37.setAutoDefault(True)
        self.pushButton_37.setObjectName("pushButton_37")
        self.pushButton_38 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_38.setGeometry(QtCore.QRect(1030, 440, 121, 91))
        self.pushButton_38.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_38.setCheckable(False)
        self.pushButton_38.setObjectName("pushButton_38")
        self.pushButton_39 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_39.setGeometry(QtCore.QRect(900, 240, 121, 91))
        self.pushButton_39.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_39.setCheckable(False)
        self.pushButton_39.setAutoDefault(True)
        self.pushButton_39.setObjectName("pushButton_39")
        self.pushButton_40 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openWindow())
        self.pushButton_40.setGeometry(QtCore.QRect(900, 540, 121, 91))
        self.pushButton_40.setStyleSheet("border-radius: 7px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(153, 210, 242);\n"
"border: 1px solid black;")
        self.pushButton_40.setCheckable(False)
        self.pushButton_40.setObjectName("pushButton_40")

        self.pushButton_41 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_41.setGeometry(QtCore.QRect(160, 700, 70, 70))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_41.setFont(font)
        self.pushButton_41.setStyleSheet("border-radius: 10px;\n"
                                         "font: 75 8pt \"MS Shell Dlg 2\";\n"
                                         "background-color: rgb(153, 210, 242);\n"
                                         "border: 1px solid black;")
        self.pushButton_41.setAutoRepeatDelay(300)
        self.pushButton_41.setAutoRepeatInterval(100)
        self.pushButton_41.setFlat(False)
        self.pushButton_41.setObjectName("pushButton_41")

        self.pushButton_42 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_42.setGeometry(QtCore.QRect(250, 700, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_42.setFont(font)
        self.pushButton_42.setStyleSheet("border-radius: 10px;\n"
                                         "background-color: rgb(249, 210, 222);\n"
                                         "border: 1px solid black;")
        self.pushButton_42.setAutoRepeatDelay(300)
        self.pushButton_42.setAutoRepeatInterval(100)
        self.pushButton_42.setFlat(False)
        self.pushButton_42.setObjectName("pushButton_42")

        self.pushButton_43 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_43.setGeometry(QtCore.QRect(610, 700, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_43.setFont(font)
        self.pushButton_43.setStyleSheet("border-radius: 10px;\n"
                                         "background-color: rgb(164, 164, 164);\n"
                                         "border: 1px solid black;")
        self.pushButton_43.setAutoRepeatDelay(300)
        self.pushButton_43.setAutoRepeatInterval(100)
        self.pushButton_43.setFlat(False)
        self.pushButton_43.setObjectName("pushButton_43")

        self.pushButton_44 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_44.setGeometry(QtCore.QRect(430, 700, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_44.setFont(font)
        self.pushButton_44.setStyleSheet("border-radius: 10px;\n"
                                         "background-color: rgb(179, 145, 181);\n"
                                         "border: 1px solid black;")
        self.pushButton_44.setAutoRepeatDelay(300)
        self.pushButton_44.setAutoRepeatInterval(100)
        self.pushButton_44.setFlat(False)
        self.pushButton_44.setObjectName("pushButton_44")

        self.pushButton_45 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_45.setGeometry(QtCore.QRect(340, 700, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_45.setFont(font)
        self.pushButton_45.setStyleSheet("border-radius: 10px;\n"
                                         "background-color: rgb(255, 219, 169);\n"
                                         "border: 1px solid black;")
        self.pushButton_45.setAutoRepeatDelay(300)
        self.pushButton_45.setAutoRepeatInterval(100)
        self.pushButton_45.setFlat(False)
        self.pushButton_45.setObjectName("pushButton_45")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(90, 720, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(740, 700, 311, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(710, 730, 341, 20))
        self.label_12.setObjectName("label_12")
        self.pushButton_46 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_46.setGeometry(QtCore.QRect(520, 700, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_46.setFont(font)
        self.pushButton_46.setStyleSheet("border-radius: 10px;\n"
                                       "border: 3px solid blue;")
        self.pushButton_46.setAutoRepeatDelay(300)
        self.pushButton_46.setAutoRepeatInterval(100)
        self.pushButton_46.setFlat(False)
        self.pushButton_46.setObjectName("pushButton_46")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1199, 26)) #1199, 26 #1200, 26
        self.menubar.setObjectName("menubar")
        self.menuTBd = QtWidgets.QMenu(self.menubar)
        self.menuTBd.setObjectName("menuTBd")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuTBd.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Criminal Justice - Bachelor of Science Suggested Academic Plan"))
        self.pushButton.setText(_translate("MainWindow", "CRIMJ 100 (3 cr)"))
        self.label_2.setText(_translate("MainWindow", "Year 1"))
        self.label_3.setText(_translate("MainWindow", "Year 2"))
        self.label_4.setText(_translate("MainWindow", "Year 3"))
        self.label_5.setText(_translate("MainWindow", "Year 4"))

        self.buttonArray = [self.pushButton, self.pushButton_2, self.pushButton_3, self.pushButton_4, self.pushButton_5,
                            self.pushButton_6, self.pushButton_7,
                            self.pushButton_8, self.pushButton_9, self.pushButton_10, self.pushButton_11,
                            self.pushButton_12, self.pushButton_13,
                            self.pushButton_14, self.pushButton_15, self.pushButton_16, self.pushButton_17,
                            self.pushButton_18, self.pushButton_19, self.pushButton_20,
                            self.pushButton_21, self.pushButton_22, self.pushButton_23, self.pushButton_24,
                            self.pushButton_25, self.pushButton_26, self.pushButton_27,
                            self.pushButton_28, self.pushButton_29, self.pushButton_30, self.pushButton_31,
                            self.pushButton_32, self.pushButton_33, self.pushButton_34,
                            self.pushButton_35, self.pushButton_36, self.pushButton_37, self.pushButton_38,
                            self.pushButton_39, self.pushButton_40]

        Ui_MainWindow.populate(self, arrayButton=self.buttonArray, translator=_translate)

        self.pushButton_41.setText(_translate("MainWindow", "Core\n"
                                                            "(In\n"
                                                            " Major)"))
        self.pushButton_42.setText(_translate("MainWindow", "Gen.\n"
                                                            "Ed."))
        self.pushButton_43.setText(_translate("MainWindow", "Taken"))
        self.pushButton_44.setText(_translate("MainWindow", "Major &\n"
                                                            "Gen.\n"
                                                            " Ed."))
        self.pushButton_45.setText(_translate("MainWindow", "Elective"))
        self.label_10.setText(_translate("MainWindow", "Legend"))
        self.label_11.setText(_translate("MainWindow", "*** PSU starting Fall 2019 - must earn a C or higher"))
        self.label_12.setText(
            _translate("MainWindow", "General Education: Complete 6 Inter-Domain (\"N\") or 6 Linked units"))
        self.pushButton_46.setText(_translate("MainWindow", "C or \n"
                                                            "Better\n"
                                                            "Required"))

        #self.menuTBd.setTitle(_translate("MainWindow", "TBd"))

    def processFile(self, fileName):
        name = []
        courseID = []
        credit = []
        color = []
        data = []

        myFile = open(fileName, "r")  # Note: Is the StudentInfo unsorted file in the project

        for line in myFile:
            #line.write()
            text = line.strip()
            x = ''.join(text)
            x = text.split()
            x = ''.join(x)
            y = x.split(',')
            #print(y)  # This line is for debuging
            name.append(y[0])
            courseID.append(y[1])
            credit.append(y[2])
            color.append(y[3])
            data.append(y[:])
            print(data, end = "\n")
        return data
        myFile.close()

    def populate(self, arrayButton, translator):
        data = Ui_MainWindow.processFile(self, "CourseInfo.txt")  # open('CourseInfo.txt', 'r')
        # print(data)
        d = 0
        linecounter = 0
        for i in data:
            """if linecounter == 40:
                break"""
            line = i[0] + "\n" + i[1] + "\n" + i[2] + " credits"
            linecounter += 1
            # print(line)
            arrayButton[d].setText(translator("MainWindow", line))
            d = d + 1
        # CRIMJ 220 3 pink => ['CRIMJ', '220', '3', 'pink']


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())