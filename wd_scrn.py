# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wd_screen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from end_scrn import Ui_endScrn
from bal_lim import Ui_wdLim

class Ui_wdScrn(object):
    def __init__(self, c_no, mydb):
        self.mydb = mydb
        self.c_no = c_no
        
    def setupUi(self, wdScrn):
        wdScrn.setObjectName("wdScrn")
        wdScrn.resize(960, 640)
        wdScrn.setStyleSheet("background-color: rgb(33, 170, 229);\n"
"background-color: rgb(173, 127, 168);")
        wdScrn.setModal(False)
        self.topLabel = QtWidgets.QTextBrowser(wdScrn)
        self.topLabel.setGeometry(QtCore.QRect(0, 0, 961, 111))
        self.topLabel.setStyleSheet("background-color: rgb(225, 255, 253);")
        self.topLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.topLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.topLabel.setLineWidth(3)
        self.topLabel.setObjectName("topLabel")
        self.QRframe = QtWidgets.QLabel(wdScrn)
        self.QRframe.setGeometry(QtCore.QRect(20, 130, 921, 491))
        self.QRframe.setFrameShape(QtWidgets.QFrame.Panel)
        self.QRframe.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.QRframe.setLineWidth(3)
        self.QRframe.setText("")
        self.QRframe.setObjectName("QRframe")
        self.textBrowser = QtWidgets.QTextBrowser(wdScrn)
        self.textBrowser.setGeometry(QtCore.QRect(170, 230, 631, 41))
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit = QtWidgets.QLineEdit(wdScrn)
        self.lineEdit.setGeometry(QtCore.QRect(320, 330, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.okBtn = QtWidgets.QPushButton(wdScrn)
        self.okBtn.setGeometry(QtCore.QRect(370, 470, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.okBtn.setFont(font)
        self.okBtn.setStyleSheet("background-color: rgb(224, 255, 253);")
        self.okBtn.setObjectName("okBtn")
        
        self.okBtn.clicked.connect(self.data)

        self.retranslateUi(wdScrn)
        QtCore.QMetaObject.connectSlotsByName(wdScrn)
        
    def data(self):
        inp_data = self.lineEdit.text()
        amount = int(inp_data)
        self.transxn(amount)
        
    def transxn(self, amount):
        
        curs = self.mydb.cursor()
        
        bal_sql = f"SELECT bal FROM custs WHERE card_no = {self.c_no}"
        curs.execute(bal_sql)
        res = curs.fetchone()
        init_bal = res[0]
        
        if init_bal < amount:
            print("Withdrawal amount exceeded. Transaction failed.")
            self.close_con()
            self.balLim_screen()
            
        else:
            wd_sql = f"SELECT bal - {amount} FROM custs WHERE card_no = {self.c_no}"
            curs.execute(wd_sql)
            res = curs.fetchone()
            bal = res[0]
            
            set_bal = f"UPDATE custs SET bal = {bal} WHERE card_no = {self.c_no}"
            curs.execute(set_bal)
            self.mydb.commit()
            print(bal)
            self.close_con()
            self.end_screen()
            
    def close_con(self):
        self.mydb.close()
        
    def end_screen(self):
        endScrn = QtWidgets.QDialog()
        endScrn.ui = Ui_endScrn()
        endScrn.ui.setupUi(endScrn)
        endScrn.show()
        QtCore.QTimer.singleShot(7000, endScrn.close)
        endScrn.exec_()
        
    def balLim_screen(self):
        wdLim = QtWidgets.QDialog()
        ui = Ui_wdLim()
        ui.setupUi(wdLim)
        wdLim.show()
        QtCore.QTimer.singleShot(7000, wdLim.close)
        wdLim.exec_()

    def retranslateUi(self, wdScrn):
        _translate = QtCore.QCoreApplication.translate
        wdScrn.setWindowTitle(_translate("wdScrn", "Dialog"))
        self.topLabel.setHtml(_translate("wdScrn", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#000000;\">ENHANCED ATM - For Cardless and Secure Transactions</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("wdScrn", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Please enter the withdrawal amount</span></p></body></html>"))
        self.okBtn.setText(_translate("wdScrn", "OK"))


