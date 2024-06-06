# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CAD_BOM.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(870, 682)
        self.Open = QAction(MainWindow)
        self.Open.setObjectName(u"Open")
        self.Save = QAction(MainWindow)
        self.Save.setObjectName(u"Save")
        self.Save_As = QAction(MainWindow)
        self.Save_As.setObjectName(u"Save_As")
        self.Exit = QAction(MainWindow)
        self.Exit.setObjectName(u"Exit")
        self.import_CAD = QAction(MainWindow)
        self.import_CAD.setObjectName(u"import_CAD")
        self.import_BOM = QAction(MainWindow)
        self.import_BOM.setObjectName(u"import_BOM")
        self.action3 = QAction(MainWindow)
        self.action3.setObjectName(u"action3")
        self.action4 = QAction(MainWindow)
        self.action4.setObjectName(u"action4")
        self.import_CAD_BOM = QAction(MainWindow)
        self.import_CAD_BOM.setObjectName(u"import_CAD_BOM")
        self.import_GC_CSV = QAction(MainWindow)
        self.import_GC_CSV.setObjectName(u"import_GC_CSV")
        self.FUJI_R = QAction(MainWindow)
        self.FUJI_R.setObjectName(u"FUJI_R")
        self.Yamaha_R = QAction(MainWindow)
        self.Yamaha_R.setObjectName(u"Yamaha_R")
        self.JUKI_R = QAction(MainWindow)
        self.JUKI_R.setObjectName(u"JUKI_R")
        self.GXH_R = QAction(MainWindow)
        self.GXH_R.setObjectName(u"GXH_R")
        self.Samsung_R = QAction(MainWindow)
        self.Samsung_R.setObjectName(u"Samsung_R")
        self.Panasonic_R = QAction(MainWindow)
        self.Panasonic_R.setObjectName(u"Panasonic_R")
        self.NCMaater_R = QAction(MainWindow)
        self.NCMaater_R.setObjectName(u"NCMaater_R")
        self.Fuji_Flexa_E = QAction(MainWindow)
        self.Fuji_Flexa_E.setObjectName(u"Fuji_Flexa_E")
        self.YAMAHA_E = QAction(MainWindow)
        self.YAMAHA_E.setObjectName(u"YAMAHA_E")
        self.Samsung_E = QAction(MainWindow)
        self.Samsung_E.setObjectName(u"Samsung_E")
        self.JUKI_E = QAction(MainWindow)
        self.JUKI_E.setObjectName(u"JUKI_E")
        self.Panasonnic_E = QAction(MainWindow)
        self.Panasonnic_E.setObjectName(u"Panasonnic_E")
        self.GXH_E = QAction(MainWindow)
        self.GXH_E.setObjectName(u"GXH_E")
        self.SONY_E = QAction(MainWindow)
        self.SONY_E.setObjectName(u"SONY_E")
        self.RongDe_E = QAction(MainWindow)
        self.RongDe_E.setObjectName(u"RongDe_E")
        self.HanChengTong_E = QAction(MainWindow)
        self.HanChengTong_E.setObjectName(u"HanChengTong_E")
        self.COORD10_E = QAction(MainWindow)
        self.COORD10_E.setObjectName(u"COORD10_E")
        self.export_CAD = QAction(MainWindow)
        self.export_CAD.setObjectName(u"export_CAD")
        self.export_CADBOM = QAction(MainWindow)
        self.export_CADBOM.setObjectName(u"export_CADBOM")
        self.export_place_part_data = QAction(MainWindow)
        self.export_place_part_data.setObjectName(u"export_place_part_data")
        self.Send_GC = QAction(MainWindow)
        self.Send_GC.setObjectName(u"Send_GC")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.TB_show = QLabel(self.centralwidget)
        self.TB_show.setObjectName(u"TB_show")

        self.horizontalLayout.addWidget(self.TB_show)

        self.TB_combobox = QComboBox(self.centralwidget)
        self.TB_combobox.setObjectName(u"TB_combobox")

        self.horizontalLayout.addWidget(self.TB_combobox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.table_cadbom = QTableWidget(self.centralwidget)
        self.table_cadbom.setObjectName(u"table_cadbom")

        self.gridLayout.addWidget(self.table_cadbom, 2, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Place_Data = QPushButton(self.centralwidget)
        self.Place_Data.setObjectName(u"Place_Data")

        self.horizontalLayout_2.addWidget(self.Place_Data)

        self.Pcbsize_Data = QPushButton(self.centralwidget)
        self.Pcbsize_Data.setObjectName(u"Pcbsize_Data")

        self.horizontalLayout_2.addWidget(self.Pcbsize_Data)

        self.Part_Data = QPushButton(self.centralwidget)
        self.Part_Data.setObjectName(u"Part_Data")

        self.horizontalLayout_2.addWidget(self.Part_Data)

        self.PartTable_Data = QPushButton(self.centralwidget)
        self.PartTable_Data.setObjectName(u"PartTable_Data")

        self.horizontalLayout_2.addWidget(self.PartTable_Data)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 870, 22))
        self.File = QMenu(self.menubar)
        self.File.setObjectName(u"File")
        self.Data_Import = QMenu(self.menubar)
        self.Data_Import.setObjectName(u"Data_Import")
        self.reading_program = QMenu(self.menubar)
        self.reading_program.setObjectName(u"reading_program")
        self.export_Fle = QMenu(self.menubar)
        self.export_Fle.setObjectName(u"export_Fle")
        self.Transmit_Coordinate = QMenu(self.menubar)
        self.Transmit_Coordinate.setObjectName(u"Transmit_Coordinate")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.File.menuAction())
        self.menubar.addAction(self.Data_Import.menuAction())
        self.menubar.addAction(self.reading_program.menuAction())
        self.menubar.addAction(self.export_Fle.menuAction())
        self.menubar.addAction(self.Transmit_Coordinate.menuAction())
        self.File.addAction(self.Open)
        self.File.addAction(self.Save)
        self.File.addAction(self.Save_As)
        self.File.addAction(self.Exit)
        self.Data_Import.addAction(self.import_CAD)
        self.Data_Import.addAction(self.import_BOM)
        self.Data_Import.addSeparator()
        self.Data_Import.addAction(self.import_CAD_BOM)
        self.Data_Import.addAction(self.import_GC_CSV)
        self.reading_program.addAction(self.FUJI_R)
        self.reading_program.addSeparator()
        self.reading_program.addAction(self.Yamaha_R)
        self.reading_program.addSeparator()
        self.reading_program.addAction(self.JUKI_R)
        self.reading_program.addSeparator()
        self.reading_program.addAction(self.GXH_R)
        self.reading_program.addSeparator()
        self.reading_program.addAction(self.Samsung_R)
        self.reading_program.addSeparator()
        self.reading_program.addAction(self.Panasonic_R)
        self.reading_program.addSeparator()
        self.reading_program.addAction(self.NCMaater_R)
        self.export_Fle.addAction(self.Fuji_Flexa_E)
        self.export_Fle.addSeparator()
        self.export_Fle.addAction(self.YAMAHA_E)
        self.export_Fle.addSeparator()
        self.export_Fle.addAction(self.Samsung_E)
        self.export_Fle.addSeparator()
        self.export_Fle.addAction(self.JUKI_E)
        self.export_Fle.addSeparator()
        self.export_Fle.addAction(self.Panasonnic_E)
        self.export_Fle.addSeparator()
        self.export_Fle.addAction(self.GXH_E)
        self.export_Fle.addSeparator()
        self.export_Fle.addAction(self.SONY_E)
        self.export_Fle.addSeparator()
        self.export_Fle.addAction(self.RongDe_E)
        self.export_Fle.addSeparator()
        self.export_Fle.addAction(self.HanChengTong_E)
        self.export_Fle.addSeparator()
        self.export_Fle.addAction(self.COORD10_E)
        self.export_Fle.addSeparator()
        self.export_Fle.addAction(self.export_CAD)
        self.export_Fle.addAction(self.export_CADBOM)
        self.export_Fle.addAction(self.export_place_part_data)
        self.Transmit_Coordinate.addAction(self.Send_GC)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SMT\u7a0b\u5e8f\u683c\u5f0f\u8f6c\u6362", None))
        self.Open.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.Save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.Save_As.setText(QCoreApplication.translate("MainWindow", u"\u53e6\u5b58\u4e3a", None))
        self.Exit.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.import_CAD.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165_CAD\u5750\u6807", None))
        self.import_BOM.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165_BOM_\u6574\u7406_\u6bd4\u5bf9", None))
        self.action3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.action4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.import_CAD_BOM.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165_\u6587\u4ef6_CAD+BOM", None))
        self.import_GC_CSV.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165GC-PowerStation\u751f\u6210\u7684_CSV", None))
        self.FUJI_R.setText(QCoreApplication.translate("MainWindow", u"FUJI", None))
        self.Yamaha_R.setText(QCoreApplication.translate("MainWindow", u"Yamaha", None))
        self.JUKI_R.setText(QCoreApplication.translate("MainWindow", u"JUKI", None))
        self.GXH_R.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u7acb", None))
        self.Samsung_R.setText(QCoreApplication.translate("MainWindow", u"\u97e9\u534e\u4e09\u661f", None))
        self.Panasonic_R.setText(QCoreApplication.translate("MainWindow", u"Panasonic", None))
        self.NCMaater_R.setText(QCoreApplication.translate("MainWindow", u"NCMaater\u6587\u4ef6", None))
        self.Fuji_Flexa_E.setText(QCoreApplication.translate("MainWindow", u"Fuji Flexa\u6587\u4ef6\u683c\u5f0f", None))
        self.YAMAHA_E.setText(QCoreApplication.translate("MainWindow", u"YAMAHA\u6587\u4ef6\u683c\u5f0f", None))
        self.Samsung_E.setText(QCoreApplication.translate("MainWindow", u"\u97e9\u534e\u4e09\u661f\u6587\u4ef6\u683c\u5f0f", None))
        self.JUKI_E.setText(QCoreApplication.translate("MainWindow", u"JUKI\u6587\u4ef6\u683c\u5f0f", None))
        self.Panasonnic_E.setText(QCoreApplication.translate("MainWindow", u"Panasonnic\u6587\u4ef6\u683c\u5f0f", None))
        self.GXH_E.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u7acb\u6587\u4ef6\u683c\u5f0f", None))
        self.SONY_E.setText(QCoreApplication.translate("MainWindow", u"SONY\u6587\u4ef6\u683c\u5f0f", None))
        self.RongDe_E.setText(QCoreApplication.translate("MainWindow", u"\u8363\u5fb7\u6587\u4ef6\u683c\u5f0f", None))
        self.HanChengTong_E.setText(QCoreApplication.translate("MainWindow", u"\u6c49\u8bda\u901a\u6587\u4ef6\u683c\u5f0f", None))
        self.COORD10_E.setText(QCoreApplication.translate("MainWindow", u"COORD10", None))
        self.export_CAD.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u5750\u6807_txt", None))
        self.export_CADBOM.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u5750\u6807BOM\u7ed3\u679c_CSV", None))
        self.export_place_part_data.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u8d34\u88c5\u62fc\u677f\u5750\u6807\u5143\u4ef6\u6570\u636e_xls", None))
        self.Send_GC.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u5230GC2000\u8f85\u52a9\u5de5\u5177", None))
        self.TB_show.setText(QCoreApplication.translate("MainWindow", u"T/B\u663e\u793a", None))
        self.TB_combobox.setCurrentText("")
        self.Place_Data.setText(QCoreApplication.translate("MainWindow", u"\u8d34\u88c5\u6570\u636e", None))
        self.Pcbsize_Data.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u677f\u6570\u636e", None))
        self.Part_Data.setText(QCoreApplication.translate("MainWindow", u"\u5143\u4ef6\u6570\u636e", None))
        self.PartTable_Data.setText(QCoreApplication.translate("MainWindow", u"\u6599\u7ad9\u6570\u636e", None))
        self.File.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.Data_Import.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5bfc\u5165", None))
        self.reading_program.setTitle(QCoreApplication.translate("MainWindow", u"\u8bfb\u53d6\u7a0b\u5e8f", None))
        self.export_Fle.setTitle(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u6587\u4ef6", None))
        self.Transmit_Coordinate.setTitle(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u5750\u6807", None))
    # retranslateUi

