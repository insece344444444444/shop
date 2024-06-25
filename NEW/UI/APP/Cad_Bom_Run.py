from PySide6.QtWidgets import *
from NEW.UI.UIC.CAD_BOM import Ui_MainWindow as Cad
from NEW.UI.APP.Import_Cad_Run import ImportCadWindow
class CadWindow(QMainWindow,Cad):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

        self.import_CAD.triggered.connect(self.bind_importcad)

    def initUI(self):
        self.table_cadbom.setColumnCount(8)
        headers=['','序号','位号','X坐标','Y坐标','R角度','元件号码','物料描述']
        self.TB_combobox.addItems(['All','Top','Bot'])

        self.table_cadbom.setHorizontalHeaderLabels(headers)
        self.table_cadbom.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table_cadbom.horizontalHeader().setSectionResizeMode(0,QHeaderView.Fixed)
        self.table_cadbom.setColumnWidth(0,20)
        for col in range(1,6):
            self.table_cadbom.horizontalHeader().setSectionResizeMode(col,QHeaderView.Fixed)
            self.table_cadbom.setColumnWidth(col,90)
        for row in range(self.table_cadbom.rowCount()):
            for col in range(self.table_cadbom.columnCount()):
                if col == 0:
                    item=QTableWidgetItem(f"Row {row+1}")
                    print(item)
                else:
                    item=QTableWidgetItem(f"Item {row+1}-{col+1}")
                    print(item)
                self.table_cadbom.setItem(row,col,item)

        self.button_group = QButtonGroup(self)
        self.button_group.setExclusive(True)

        self.buttons = [
            self.Place_Data,
            self.Pcbsize_Data,
            self.Part_Data,
            self.PartTable_Data
        ]
        for button in self.buttons:
            button.setCheckable(True)
            button.setStyleSheet(self.default_style())
            button.clicked.connect(self.update_button_styles)
            button.enterEvent = lambda event,b=button:self.on_hover_enter(b)
            button.leaveEvent = lambda event,b=button:self.on_hover_leave(b)
            self.button_group.addButton(button)
            self.buttons[0].setChecked(True)
        self.update_button_styles()

    def update_button_styles(self):
        for button in self.buttons:
            if button.isChecked():
                button.setStyleSheet(self.checked_style())
            else:
                button.setStyleSheet(self.default_style())
    def on_hover_enter(self,button):
        if not button.isChecked():
            button.setStyleSheet(self.hover_style())
    def on_hover_leave(self,button):
        if not button.isChecked():
            button.setStyleSheet(self.default_style())

    def default_style(self):
        return """
        QPushButton {
            background-color: none;
            border: 1px solid#cccccc;
            }
            """

    def checked_style(self):
        return """
        QPushButton {
            background-color:#FF69B4;
            border: 1px solid#cccccc;
            }
            """

    def hover_style(self):
        return """
        QPushButton {
            background-color:#FFC0CB;
            border: 1px solid#cccccc;
            }
            """

    def bind_importcad(self):
        self.subwindow_importcad=ImportCadWindow()
        self.subwindow_importcad.show()
        self.subwindow_importcad.closeEvent = lambda event:self.show()
        self.closeEvent_i=lambda  event: self.subwindow_importcad.close()
        self.hide()

    def import_cad_data(self):
        print('测试信号')
