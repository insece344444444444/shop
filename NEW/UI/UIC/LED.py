# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LED.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(990, 725)
        self.import_file = QAction(MainWindow)
        self.import_file.setObjectName(u"import_file")
        self.export_file = QAction(MainWindow)
        self.export_file.setObjectName(u"export_file")
        self.actionPass = QAction(MainWindow)
        self.actionPass.setObjectName(u"actionPass")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.SetHeader_btn = QPushButton(self.centralwidget)
        self.SetHeader_btn.setObjectName(u"SetHeader_btn")

        self.horizontalLayout.addWidget(self.SetHeader_btn)

        self.split_Part = QPushButton(self.centralwidget)
        self.split_Part.setObjectName(u"split_Part")

        self.horizontalLayout.addWidget(self.split_Part)

        self.horizontalSpacer = QSpacerItem(1000, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.table = QTableWidget(self.centralwidget)
        self.table.setObjectName(u"table")

        self.gridLayout.addWidget(self.table, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 990, 22))
        self.file = QMenu(self.menubar)
        self.file.setObjectName(u"file")
        self.print = QMenu(self.menubar)
        self.print.setObjectName(u"print")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.file.menuAction())
        self.menubar.addAction(self.print.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.file.addAction(self.import_file)
        self.print.addAction(self.export_file)
        self.menu.addAction(self.actionPass)

        self.retranslateUi(MainWindow)
        self.import_file.triggered.connect(MainWindow.import_csv)
        self.export_file.triggered.connect(MainWindow.export_csv)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"LED", None))
        self.import_file.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165CAD\u5750\u6807", None))
        self.export_file.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51faCAD", None))
        self.actionPass.setText(QCoreApplication.translate("MainWindow", u"Pass", None))
        self.SetHeader_btn.setText(QCoreApplication.translate("MainWindow", u"\u5b9a\u4e49\u8868\u5934", None))
        self.split_Part.setText(QCoreApplication.translate("MainWindow", u"\u7ad9\u4f4d\u6253\u6563", None))
        self.file.setTitle(QCoreApplication.translate("MainWindow", u"\u8f93\u5165", None))
        self.print.setTitle(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u5750\u6807", None))
    # retranslateUi

