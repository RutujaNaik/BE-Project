# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bnk_options.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ops_screen import Ui_ops_Scrn


class Ui_bnkScrn(object):
    def __init__(self, c_no, mydb):
        self.mydb = mydb
        self.c_no = c_no
        #self.bnkScrn = bnkScrn
        #print("printed from bnk_options -", c_no)
        
    def setupUi(self, bnkScrn):
        bnkScrn.setObjectName("bnkScrn")
        bnkScrn.resize(960, 640)
        bnkScrn.setStyleSheet("background-color: rgb(33, 170, 229);\n"
"background-color: rgb(173, 127, 168);")
        bnkScrn.setModal(False)
        self.topLabel = QtWidgets.QTextBrowser(bnkScrn)
        self.topLabel.setGeometry(QtCore.QRect(0, 0, 961, 111))
        self.topLabel.setStyleSheet("background-color: rgb(225, 255, 253);")
        self.topLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.topLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.topLabel.setLineWidth(3)
        self.topLabel.setObjectName("topLabel")
        self.QRframe = QtWidgets.QLabel(bnkScrn)
        self.QRframe.setGeometry(QtCore.QRect(20, 130, 921, 491))
        self.QRframe.setFrameShape(QtWidgets.QFrame.Panel)
        self.QRframe.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.QRframe.setLineWidth(3)
        self.QRframe.setText("")
        self.QRframe.setObjectName("QRframe")
        self.verticalWidget = QtWidgets.QWidget(bnkScrn)
        self.verticalWidget.setGeometry(QtCore.QRect(500, 250, 431, 241))
        self.verticalWidget.setAutoFillBackground(False)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.savBtn = QtWidgets.QPushButton(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.savBtn.sizePolicy().hasHeightForWidth())
        self.savBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.savBtn.setFont(font)
        self.savBtn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(166, 166, 166);\n"
"selection-color: rgb(170, 255, 255);")
        self.savBtn.setObjectName("savBtn")
        self.verticalLayout.addWidget(self.savBtn)
        self.curBtn = QtWidgets.QPushButton(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.curBtn.sizePolicy().hasHeightForWidth())
        self.curBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.curBtn.setFont(font)
        self.curBtn.setAutoFillBackground(False)
        self.curBtn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(166, 166, 166);\n"
"selection-color: rgb(170, 255, 255);")
        self.curBtn.setObjectName("curBtn")
        self.verticalLayout.addWidget(self.curBtn)

        self.savBtn.clicked.connect(self.ops_screenWindow)
        self.curBtn.clicked.connect(self.ops_screenWindow)

        self.retranslateUi(bnkScrn)
        QtCore.QMetaObject.connectSlotsByName(bnkScrn) 
        
        #QtCore.QTimer.singleShot(1000, self.win_close)
        
        #self.savBtn.clicked.connect(self.win_close)
        #self.curBtn.clicked.connect(self.win_close)
        
    def ops_screenWindow(self):
        ops_Scrn = QtWidgets.QDialog()
        ops_Scrn.ui = Ui_ops_Scrn(self.c_no, self.mydb)
        ops_Scrn.ui.setupUi(ops_Scrn)
        ops_Scrn.show()
        QtCore.QTimer.singleShot(9000, ops_Scrn.close)
        ops_Scrn.exec_() 
        
        
    def retranslateUi(self, bnkScrn):
        _translate = QtCore.QCoreApplication.translate
        bnkScrn.setWindowTitle(_translate("bnkScrn", "Dialog"))
        self.topLabel.setHtml(_translate("bnkScrn", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#000000;\">ENHANCED ATM - For Cardless and Secure Transactions</span></p></body></html>"))
        self.savBtn.setText(_translate("bnkScrn", "Savings Account"))
        self.curBtn.setText(_translate("bnkScrn", "Current Account"))


