# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Import_Cad.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Cad_Data(object):
    def setupUi(self, Cad_Data):
        if not Cad_Data.objectName():
            Cad_Data.setObjectName(u"Cad_Data")
        Cad_Data.resize(865, 630)
        self.gridLayout = QGridLayout(Cad_Data)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.OpenFile_BTN = QPushButton(Cad_Data)
        self.OpenFile_BTN.setObjectName(u"OpenFile_BTN")

        self.horizontalLayout.addWidget(self.OpenFile_BTN)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.SetHeader_BTN = QPushButton(Cad_Data)
        self.SetHeader_BTN.setObjectName(u"SetHeader_BTN")

        self.horizontalLayout.addWidget(self.SetHeader_BTN)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.Check_repetition_BTN = QPushButton(Cad_Data)
        self.Check_repetition_BTN.setObjectName(u"Check_repetition_BTN")

        self.horizontalLayout.addWidget(self.Check_repetition_BTN)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.Import_BTN = QPushButton(Cad_Data)
        self.Import_BTN.setObjectName(u"Import_BTN")

        self.horizontalLayout.addWidget(self.Import_BTN)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.repetition_label = QLabel(Cad_Data)
        self.repetition_label.setObjectName(u"repetition_label")

        self.horizontalLayout_2.addWidget(self.repetition_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.table_importcad = QTableWidget(Cad_Data)
        self.table_importcad.setObjectName(u"table_importcad")

        self.gridLayout.addWidget(self.table_importcad, 1, 0, 1, 1)


        self.retranslateUi(Cad_Data)

        QMetaObject.connectSlotsByName(Cad_Data)
    # setupUi

    def retranslateUi(self, Cad_Data):
        Cad_Data.setWindowTitle(QCoreApplication.translate("Cad_Data", u"\u5750\u6807\u6570\u636e", None))
        self.OpenFile_BTN.setText(QCoreApplication.translate("Cad_Data", u"\u6253\u5f00\u6587\u4ef6", None))
        self.SetHeader_BTN.setText(QCoreApplication.translate("Cad_Data", u"\u8bbe\u7f6e\u8868\u5934", None))
        self.Check_repetition_BTN.setText(QCoreApplication.translate("Cad_Data", u"\u68c0\u67e5\u91cd\u590d", None))
        self.Import_BTN.setText(QCoreApplication.translate("Cad_Data", u"\u786e\u5b9a\u5bfc\u5165", None))
        self.repetition_label.setText("")
    # retranslateUi

