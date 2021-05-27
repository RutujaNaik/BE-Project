# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bal_lim.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_wdLim(object):
    def setupUi(self, wdLim):
        wdLim.setObjectName("wdLim")
        wdLim.resize(960, 640)
        wdLim.setStyleSheet("background-color: rgb(33, 170, 229);\n"
"background-color: rgb(173, 127, 168);")
        wdLim.setModal(False)
        self.topLabel = QtWidgets.QTextBrowser(wdLim)
        self.topLabel.setGeometry(QtCore.QRect(0, 0, 961, 111))
        self.topLabel.setStyleSheet("background-color: rgb(225, 255, 253);")
        self.topLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.topLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.topLabel.setLineWidth(3)
        self.topLabel.setObjectName("topLabel")
        self.QRframe = QtWidgets.QLabel(wdLim)
        self.QRframe.setGeometry(QtCore.QRect(20, 130, 921, 491))
        self.QRframe.setFrameShape(QtWidgets.QFrame.Panel)
        self.QRframe.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.QRframe.setLineWidth(3)
        self.QRframe.setText("")
        self.QRframe.setObjectName("QRframe")
        self.textBrowser = QtWidgets.QTextBrowser(wdLim)
        self.textBrowser.setGeometry(QtCore.QRect(170, 340, 631, 51))
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(wdLim)
        QtCore.QMetaObject.connectSlotsByName(wdLim)

    def retranslateUi(self, wdLim):
        _translate = QtCore.QCoreApplication.translate
        wdLim.setWindowTitle(_translate("wdLim", "Dialog"))
        self.topLabel.setHtml(_translate("wdLim", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#000000;\">ENHANCED ATM - For Cardless and Secure Transactions</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("wdLim", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Withdrawal amount exceeded. Transaction failed.</span></p></body></html>"))

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wdLim = QtWidgets.QDialog()
    ui = Ui_wdLim()
    ui.setupUi(wdLim)
    wdLim.show()
    sys.exit(app.exec_())
"""
