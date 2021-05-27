# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bal_scrn.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from end_scrn import Ui_endScrn

class Ui_balScrn(object):
    def __init__(self, bal):
        self.bal = str(bal)
        
    
    def setupUi(self, balScrn):
        balScrn.setObjectName("balScrn")
        balScrn.resize(960, 640)
        balScrn.setStyleSheet("background-color: rgb(33, 170, 229);\n"
"background-color: rgb(173, 127, 168);")
        balScrn.setModal(False)
        self.topLabel = QtWidgets.QTextBrowser(balScrn)
        self.topLabel.setGeometry(QtCore.QRect(0, 0, 961, 111))
        self.topLabel.setStyleSheet("background-color: rgb(225, 255, 253);")
        self.topLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.topLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.topLabel.setLineWidth(3)
        self.topLabel.setObjectName("topLabel")
        self.QRframe = QtWidgets.QLabel(balScrn)
        self.QRframe.setGeometry(QtCore.QRect(20, 130, 921, 491))
        self.QRframe.setFrameShape(QtWidgets.QFrame.Panel)
        self.QRframe.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.QRframe.setLineWidth(3)
        self.QRframe.setText("")
        self.QRframe.setObjectName("QRframe")
        self.textBrowser = QtWidgets.QTextBrowser(balScrn)
        self.textBrowser.setGeometry(QtCore.QRect(170, 230, 631, 41))
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.okBtn = QtWidgets.QPushButton(balScrn)
        self.okBtn.setGeometry(QtCore.QRect(370, 470, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.okBtn.setFont(font)
        self.okBtn.setStyleSheet("background-color: rgb(224, 255, 253);")
        self.okBtn.setObjectName("okBtn")
        self.balDisp = QtWidgets.QLabel(balScrn)
        self.balDisp.setGeometry(QtCore.QRect(320, 330, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.balDisp.setFont(font)
        self.balDisp.setStyleSheet("")
        self.balDisp.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.balDisp.setFrameShadow(QtWidgets.QFrame.Plain)
        self.balDisp.setText(self.bal)
        self.balDisp.setObjectName("balDisp")
        
        self.okBtn.clicked.connect(self.end_screen)

        self.retranslateUi(balScrn)
        QtCore.QMetaObject.connectSlotsByName(balScrn)
        
    def end_screen(self):
        endScrn = QtWidgets.QDialog()
        endScrn.ui = Ui_endScrn()
        endScrn.ui.setupUi(endScrn)
        endScrn.show()
        QtCore.QTimer.singleShot(7000, endScrn.close)
        endScrn.exec_()

    def retranslateUi(self, balScrn):
        _translate = QtCore.QCoreApplication.translate
        balScrn.setWindowTitle(_translate("balScrn", "Dialog"))
        self.topLabel.setHtml(_translate("balScrn", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#000000;\">ENHANCED ATM - For Cardless and Secure Transactions</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("balScrn", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Your available balance is:</span></p></body></html>"))
        self.okBtn.setText(_translate("balScrn", "OK"))

