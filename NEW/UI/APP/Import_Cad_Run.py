from NEW.UI.UIC.Import_Cad import Ui_Cad_Data as Sub_Ui
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from NEW.UI.APP.Table_logic import Table_Logic as tb
class ImportCadWindow(Sub_Ui,tb):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.selected_column = None

        self.resetHeaders()
        self.OpenFile_BTN.clicked.connect(self.open)
        self.table_importcad.horizontalHeader().setContextMenuPolicy(Qt.CustomContextMenu)
        self.table_importcad.horizontalHeader().customContextMenuRequested.connect(self.showContextMenu)
        self.SetHeader_BTN.clicked.connect(self.ImportCad_SetHeader_Run)
        self.Check_repetition_BTN.clicked.connect(self.Check_repetition_Run)
    def open(self):
        data=self.openfile()
        self.addTableData(data,self.table_importcad)
        self.resetHeaders()

    def showContextMenu(self,pos):
        if not hasattr(self, 'context_menu'):
            self.context()
        header = self.table_importcad.horizontalHeader()
        index = header.logicalIndexAt(pos)
        if index != self.selected_column:
            self.clearColumnHighlight(self.table_importcad, self.selected_column)
            self.selected_column = index
            self.highlightColumn(index, self.table_importcad)
        self.context_menu.exec(self.table_importcad.mapToGlobal(pos))

    def context(self):
        self.context_menu = QMenu(self)
        self.action_Ref = self.context_menu.addAction('位号')
        self.action_X = self.context_menu.addAction('X坐标')
        self.action_Y = self.context_menu.addAction('Y坐标')
        self.action_R = self.context_menu.addAction('R角度')
        self.action_TB = self.context_menu.addAction('T/B')
        self.action_Reset = self.context_menu.addAction('Reset')
        self.action_Ref.triggered.connect(lambda: self.action_Trigger(self.action_Ref,self.table_importcad,self.selected_column,self.context_menu))
        self.action_X.triggered.connect(lambda: self.action_Trigger(self.action_X,self.table_importcad,self.selected_column,self.context_menu))
        self.action_Y.triggered.connect(lambda: self.action_Trigger(self.action_Y,self.table_importcad,self.selected_column,self.context_menu))
        self.action_R.triggered.connect(lambda: self.action_Trigger(self.action_R,self.table_importcad,self.selected_column,self.context_menu))
        self.action_TB.triggered.connect(lambda: self.action_Trigger(self.action_TB,self.table_importcad,self.selected_column,self.context_menu))
        self.action_Reset.triggered.connect(self.resetHeaders)

    def resetHeaders(self):
        self.resetHeader(self.table_importcad)
        self.context()

    def ImportCad_SetHeader_Run(self):
        self.ImportCad_header_order=['位号', 'X坐标', 'Y坐标', 'R角度','T/B']
        self.SetHeader(self.table_importcad, self.ImportCad_header_order)

    def Check_repetition_Run(self):
        datalist = self.exportTableData(self.table_importcad)
        test=self.Check_repetition(datalist)
        for i in test:
            result=self.table_importcad.findItems(i,Qt.MatchContains)
            for item in result:
                row=item.row()
                self.highlight_row(row,self.table_importcad)
