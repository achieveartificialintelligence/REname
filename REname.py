# -*- coding: utf-8 -*-

import re
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QStringListModel
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListView, QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(779, 343)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 0, 54, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 361, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 0, 54, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(400, 30, 361, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 280, 141, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 280, 151, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 290, 281, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 290, 54, 20))
        self.label_3.setObjectName("label_3")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(20, 60, 361, 211))
        self.listView.setObjectName("listView")
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(400, 60, 361, 211))
        self.listView_2.setObjectName("listView_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.yulan)

        self.pushButton_2.clicked.connect(self.tihuan)

        self.lineEdit_3.setText(os.getcwd())

        self.listView.clicked.connect(self.CZ)

        self.listView_2.clicked.connect(self.TH)

        self.qList1 = []  # 添加的数组数据
        self.qList2 = []  # 添加的数组数据

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "正则文件名替换"))
        self.label.setText(_translate("MainWindow", "查找"))
        self.label_2.setText(_translate("MainWindow", "替换"))
        self.pushButton.setText(_translate("MainWindow", "预览"))
        self.pushButton_2.setText(_translate("MainWindow", "替换"))
        self.label_3.setText(_translate("MainWindow", "路径名"))

    def jilu(self):
        slm1 = QStringListModel()  # 创建model
        if self.qList1.count(self.lineEdit.text())<=0:
            self.qList1.append(self.lineEdit.text())
        slm1.setStringList(self.qList1)  # 将数据设置到model
        self.listView.setModel(slm1)  # 绑定 listView 和 model

        slm2 = QStringListModel()  # 创建model
        if self.qList2.count(self.lineEdit_2.text())<=0:
            self.qList2.append(self.lineEdit_2.text())
        slm2.setStringList(self.qList2)  # 将数据设置到model
        self.listView_2.setModel(slm2)  # 绑定 listView_2 和 model

    def CZ(self, index):
        self.lineEdit.setText(self.qList1[index.row()])

    def TH(self, index):
        self.lineEdit_2.setText(self.qList2[index.row()])

    def zhixing(self, bo):
        os.system("cls")
        path = self.lineEdit_3.text()

        for root, dir, file in os.walk(path):
            for name in file:
                #print("FILE"+os.path.join(root,name))
                res=re.sub(re.compile(self.lineEdit.text()),self.lineEdit_2.text(),name)
                if name!=res :
                    print(os.path.join(root,name))
                    print(os.path.join(root,res+"\n"))
                    if bo :
                        os.rename(os.path.join(root,name),os.path.join(root,res))
            # for name in dir:
            #     print("DIR"+os.path.join(root,name))
        self.jilu()

    def yulan(self):
        self.zhixing(False)

    def tihuan(self):
        self.zhixing(True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())