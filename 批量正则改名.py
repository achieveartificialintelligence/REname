# -*- coding: utf-8 -*-

import re
import os
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(385, 198)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 54, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 10, 311, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 54, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 50, 311, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 150, 111, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 150, 111, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 100, 281, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 54, 20))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.yulan)

        self.pushButton_2.clicked.connect(self.tihuan)

        self.lineEdit_3.setText(os.getcwd())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "批量文件正则替换"))
        self.label.setText(_translate("MainWindow", "查找"))
        self.label_2.setText(_translate("MainWindow", "替换"))
        self.pushButton.setText(_translate("MainWindow", "预览"))
        self.pushButton_2.setText(_translate("MainWindow", "替换"))
        self.label_3.setText(_translate("MainWindow", "路径名"))

    def yulan(self):
        path = self.lineEdit_3.text()
        print("====START====")
        for file in os.listdir(path):
            res=re.sub(re.compile(self.lineEdit.text()),self.lineEdit_2.text(),file)
            if file!=res :
                print("[OLD]"+path+"\\"+file)
                print("[NEW]"+path+"\\"+res+"\n")
        print("====END====")

    def tihuan(self):
        path = self.lineEdit_3.text()
        print("====START====")
        for file in os.listdir(path):
            res=re.sub(re.compile(self.lineEdit.text()),self.lineEdit_2.text(),file)
            if file!=res :
                os.rename(path+"\\"+file,path+"\\"+res)
                print("[OLD]"+path+"\\"+file)
                print("[NEW]"+path+"\\"+res+"\n")
        print("====END====")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())