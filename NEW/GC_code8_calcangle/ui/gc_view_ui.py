# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gc_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(359, 255)
        MainWindow.setMinimumSize(QtCore.QSize(359, 255))
        MainWindow.setMaximumSize(QtCore.QSize(359, 255))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(0, 10, 161, 201))
        self.groupBox.setObjectName("groupBox")
        self.imageLabel = QtWidgets.QLabel(self.groupBox)
        self.imageLabel.setGeometry(QtCore.QRect(10, 20, 141, 171))
        self.imageLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.imageLabel.setAutoFillBackground(True)
        self.imageLabel.setText("")
        self.imageLabel.setObjectName("imageLabel")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(170, 10, 171, 201))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_testimg = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_testimg.setGeometry(QtCore.QRect(90, 20, 75, 23))
        self.pushButton_testimg.setObjectName("pushButton_testimg")
        self.pushButton_roi = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_roi.setGeometry(QtCore.QRect(10, 50, 75, 23))
        self.pushButton_roi.setObjectName("pushButton_roi")
        self.pushButton_showimg = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_showimg.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.pushButton_showimg.setObjectName("pushButton_showimg")
        self.pushButton_run = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_run.setGeometry(QtCore.QRect(90, 50, 71, 41))
        self.pushButton_run.setObjectName("pushButton_run")
        self.lineEdit_num = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_num.setGeometry(QtCore.QRect(40, 80, 41, 20))
        self.lineEdit_num.setObjectName("lineEdit_num")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 80, 31, 16))
        self.label.setObjectName("label")
        self.lineEdit_name = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_name.setEnabled(True)
        self.lineEdit_name.setGeometry(QtCore.QRect(40, 110, 51, 20))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 31, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 140, 31, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_angle = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_angle.setGeometry(QtCore.QRect(40, 140, 111, 20))
        self.lineEdit_angle.setObjectName("lineEdit_angle")
        self.lineEdit_part = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_part.setGeometry(QtCore.QRect(40, 170, 113, 20))
        self.lineEdit_part.setObjectName("lineEdit_part")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 31, 16))
        self.label_4.setObjectName("label_4")
        self.label_res = QtWidgets.QLabel(self.centralwidget)
        self.label_res.setGeometry(QtCore.QRect(0, 200, 241, 31))
        self.label_res.setText("")
        self.label_res.setObjectName("label_res")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GC2000自动计算角度V1.2"))
        self.groupBox.setTitle(_translate("MainWindow", "图像显示"))
        self.groupBox_2.setTitle(_translate("MainWindow", "选择"))
        self.pushButton_testimg.setText(_translate("MainWindow", "测试图像"))
        self.pushButton_roi.setText(_translate("MainWindow", "框取模板"))
        self.pushButton_showimg.setText(_translate("MainWindow", "显示图像"))
        self.pushButton_run.setText(_translate("MainWindow", "计算运行"))
        self.lineEdit_num.setText(_translate("MainWindow", "1"))
        self.label.setText(_translate("MainWindow", "数量："))
        self.label_2.setText(_translate("MainWindow", "位号："))
        self.label_3.setText(_translate("MainWindow", "旋转："))
        self.label_4.setText(_translate("MainWindow", "元件："))
