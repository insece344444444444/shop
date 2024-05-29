from PySide6.QtWidgets import *
from NEW.UI.UIC.Cad_Bom import Ui_MainWindow as Cad
class CadWindow(QMainWindow,Cad):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.table.setColumnCount(8)
        headers=['','序号','位号','X坐标','Y坐标','R角度','元件号码','物料描述']
        self.TB_combobox.addItems(['All','Top','Bot'])

        self.table.setHorizontalHeaderLabels(headers)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(0,QHeaderView.Fixed)
        self.table.setColumnWidth(0,20)
        for col in range(1,6):
            self.table.horizontalHeader().setSectionResizeMode(col,QHeaderView.Fixed)
            self.table.setColumnWidth(col,90)
        for row in range(self.table.rowCount()):
            for col in range(self.table.columnCount()):
                if col == 0:
                    item=QTableWidgetItem(f"Row {row+1}")
                    print(item)
                else:
                    item=QTableWidgetItem(f"Item {row+1}-{col+1}")
                    print(item)
                self.table.setItem(row,col,item)

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