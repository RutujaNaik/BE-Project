# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ops_screen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from wd_scrn import Ui_wdScrn
from bal_scrn import Ui_balScrn

class Ui_ops_Scrn(object):
    def __init__(self, c_no, mydb):
        self.mydb = mydb
        self.c_no = c_no
        #print("printed from ops_Scrn -", c_no)
        
    def setupUi(self, ops_Scrn):
        ops_Scrn.setObjectName("ops_Scrn")
        ops_Scrn.resize(960, 640)
        ops_Scrn.setStyleSheet("background-color: rgb(33, 170, 229);\n"
"background-color: rgb(173, 127, 168);")
        ops_Scrn.setModal(False)
        self.topLabel = QtWidgets.QTextBrowser(ops_Scrn)
        self.topLabel.setGeometry(QtCore.QRect(0, 0, 961, 111))
        self.topLabel.setStyleSheet("background-color: rgb(225, 255, 253);")
        self.topLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.topLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.topLabel.setLineWidth(3)
        self.topLabel.setObjectName("topLabel")
        self.QRframe = QtWidgets.QLabel(ops_Scrn)
        self.QRframe.setGeometry(QtCore.QRect(20, 130, 921, 491))
        self.QRframe.setFrameShape(QtWidgets.QFrame.Panel)
        self.QRframe.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.QRframe.setLineWidth(3)
        self.QRframe.setText("")
        self.QRframe.setObjectName("QRframe")
        self.verticalWidget_2 = QtWidgets.QWidget(ops_Scrn)
        self.verticalWidget_2.setGeometry(QtCore.QRect(500, 250, 431, 241))
        self.verticalWidget_2.setStyleSheet("gridline-color: rgb(255, 255, 255);")
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.wdBtn = QtWidgets.QPushButton(self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wdBtn.sizePolicy().hasHeightForWidth())
        self.wdBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.wdBtn.setFont(font)
        self.wdBtn.setAutoFillBackground(False)
        self.wdBtn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(166, 166, 166);\n"
"selection-color: rgb(170, 255, 255);")
        self.wdBtn.setObjectName("wdBtn")
        self.verticalLayout_2.addWidget(self.wdBtn)
        self.beBtn = QtWidgets.QPushButton(self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.beBtn.sizePolicy().hasHeightForWidth())
        self.beBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.beBtn.setFont(font)
        self.beBtn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(166, 166, 166);\n"
"selection-color: rgb(170, 255, 255);")
        self.beBtn.setObjectName("beBtn")
        self.verticalLayout_2.addWidget(self.beBtn)
        
        self.wdBtn.clicked.connect(self.goto_wdScrn)
        self.beBtn.clicked.connect(self.goto_balScrn)

        self.retranslateUi(ops_Scrn)
        QtCore.QMetaObject.connectSlotsByName(ops_Scrn)
        
    def goto_wdScrn(self):
        wdScrn = QtWidgets.QDialog()
        wdScrn.ui = Ui_wdScrn(self.c_no, self.mydb)
        wdScrn.ui.setupUi(wdScrn)
        wdScrn.show()
        QtCore.QTimer.singleShot(10000, wdScrn.close)
        wdScrn.exec_()
        
    def goto_balScrn(self):
        
        curs = self.mydb.cursor()
        
        bal_sql = f"SELECT bal FROM custs WHERE card_no = {self.c_no}"
        curs.execute(bal_sql)
        res = curs.fetchone()
        init_bal = res[0]
        
        self.mydb.close()
        
        balScrn = QtWidgets.QDialog()
        balScrn.ui = Ui_balScrn(init_bal)
        balScrn.ui.setupUi(balScrn)
        balScrn.show()
        QtCore.QTimer.singleShot(10000, balScrn.close)
        balScrn.exec_()

    def retranslateUi(self, ops_Scrn):
        _translate = QtCore.QCoreApplication.translate
        ops_Scrn.setWindowTitle(_translate("ops_Scrn", "Dialog"))
        self.topLabel.setHtml(_translate("ops_Scrn", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#000000;\">ENHANCED ATM - For Cardless and Secure Transactions</span></p></body></html>"))
        self.wdBtn.setText(_translate("ops_Scrn", "Withdraw"))
        self.beBtn.setText(_translate("ops_Scrn", "Balance enquiry"))


