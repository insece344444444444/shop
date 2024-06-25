import random
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from NEW.UI.UIC.LED import Ui_MainWindow as LED
from NEW.UI.APP.Table_logic import Table_Logic as tb

class LedWindow(QMainWindow,LED,tb):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet('''
                QPushButton{
                    background-color:rgb(255, 255, 255);
                    border-radius:10px;
                }
                QPushButton:hover{
                    background-color:rgb(255, 192, 203);
                    color:rgb(255, 255, 255);
                }
                ''')

        self.selected_column = None

        self.resetHeaders()
        self.table_led.horizontalHeader().setContextMenuPolicy(Qt.CustomContextMenu)
        self.table_led.horizontalHeader().setContextMenuPolicy(Qt.DefaultContextMenu)
        self.table_led.horizontalHeader().sectionClicked.connect(self.showContextMenu)

        self.split_Part.clicked.connect(self.PartRandom)
        self.split_Part.setEnabled(False)
        self.SetHeader_btn.clicked.connect(self.Led_SetHeader_Run)

        self.input_dialog = QInputDialog(self)
        self.input_dialog.setInputMode(QInputDialog.InputMode.IntInput)
        self.input_dialog.setIntRange(2, 65)
        self.input_dialog.setIntValue(2)
        self.input_dialog.setLabelText('请输入需要打散的站位数量')
        self.input_dialog.setWindowTitle('LED插花')
        self.input_dialog.setOkButtonText('确定')
        self.input_dialog.setCancelButtonText('取消')
        self.input_dialog.setWindowModality(Qt.WindowModality.ApplicationModal)

    def context(self):
        self.context_menu = QMenu(self)
        self.action_Ref = self.context_menu.addAction('位号')
        self.action_X = self.context_menu.addAction('X坐标')
        self.action_Y = self.context_menu.addAction('Y坐标')
        self.action_R = self.context_menu.addAction('R角度')
        self.action_Reset = self.context_menu.addAction('Reset')
        self.action_Ref.triggered.connect(lambda: self.action_Trigger(self.action_Ref,self.table_led,self.selected_column,self.context_menu))
        self.action_X.triggered.connect(lambda: self.action_Trigger(self.action_X,self.table_led,self.selected_column,self.context_menu))
        self.action_Y.triggered.connect(lambda: self.action_Trigger(self.action_Y,self.table_led,self.selected_column,self.context_menu))
        self.action_R.triggered.connect(lambda: self.action_Trigger(self.action_R,self.table_led,self.selected_column,self.context_menu))
        self.action_Reset.triggered.connect(self.resetHeaders)


    def showContextMenu(self,index):
        if not hasattr(self,'context_menu'):
            self.context()
        if index != self.selected_column:
            self.clearColumnHighlight(self.table_led, self.selected_column)
            self.selected_column = index
            self.highlightColumn(index, self.table_led)
        cursor_position = QCursor.pos()  # 获取当前鼠标的位置
        self.context_menu.exec(cursor_position)


    def resetHeaders(self):
        self.resetHeader(self.table_led)
        self.context()
    def import_csv(self):
        data = self.openfile()
        self.addTableData(data,self.table_led)
        self.resetHeaders()
    def export_csv(self):
        datalist=self.exportTableData(self.table_led)
        self.exportfile(datalist)
    def PartRandom(self):
        if hasattr(self,'context_menu'):
            self.input_dialog.show()
            if self.input_dialog.exec()==QInputDialog.DialogCode.Accepted:
                input_value=self.input_dialog.intValue()
            sorted_lst_x = sorted(self.RandomData(), key=lambda x: x[1])  # 根据X坐标进行排序
            sorted_lst_y = sorted(sorted_lst_x, key=lambda x: x[2])  # 根据Y坐标进行排序
            lst = self.order_list(input_value, 0)
            min_list = min(sorted_lst_y, key=lambda x: x[2])
            min_value = min_list[2]  # 获取子列表中的Y坐标的最小值
            index_one=0
            index_two=0
            index_three=0
            index_four=0
            while index_two != len(sorted_lst_y):
                if sorted_lst_y[index_two][2] == min_value:
                    sorted_lst_y[index_two].append(lst[index_three])
                    index_two += 1
                    index_three = (index_three + 1) % len(lst)
                elif sorted_lst_y[index_two][2] > sorted_lst_y[index_two - 1][2]:
                    if index_one < len(lst) - 1:
                        index_one += 1
                    else:
                        index_one = 0
                    lst = self.order_list(input_value,index_one)
                    index_four=0
                    sorted_lst_y[index_two].append(lst[index_four])
                    index_two += 1
                    index_four= (index_four + 1) % len(lst)
                elif sorted_lst_y[index_two][2] == sorted_lst_y[index_two-1][2]:
                    sorted_lst_y[index_two].append(lst[index_four])
                    index_two += 1
                    index_four = (index_four + 1) % len(lst)
                else:
                    continue
            new_column_count=self.table_led.columnCount()
            self.table_led.setColumnCount(new_column_count + 1)
            headers = [self.table_led.horizontalHeaderItem(i).text() for i in range(new_column_count)]
            headers.append('插花序列')
            self.table_led.setHorizontalHeaderLabels(headers)
            for rowIndex, row in enumerate(sorted_lst_y):  # 遍历数据
                for columnIndex, item in enumerate(row):  # 遍历数据
                    self.table_led.setItem(rowIndex, columnIndex, QTableWidgetItem(str(item)))
            self.split_Part.setEnabled(False)

    def order_list(self,input_value,sort_index=0):
        if input_value == 2:
            int_list = []
            order_list=[1,2]
            for ZW1 in range(order_list[sort_index],3):
                int_list.append(ZW1)
            for ZW2 in range(1,order_list[sort_index]):
                int_list.append(ZW2)
            return int_list
        elif input_value == 48:
            int_list = []
            order_list=[1, 37, 6, 44, 15, 27, 22, 32, 12, 41, 5, 48, 11, 26, 19, 31, 23, 38, 4, 33, 16, 45, 10, 42,
                        25, 13,30,20,39, 3, 46, 8, 36, 17, 29, 24, 35, 2, 43, 7, 47, 14, 28, 9, 40, 21, 34, 18]
            for ZW1 in range(order_list[sort_index],49):
                int_list.append(ZW1)
            for ZW2 in range(1,order_list[sort_index]):
                int_list.append(ZW2)
            return int_list
        else:
            int_list = []
            order_list=[1] + random.sample(range(2, input_value + 1),input_value - 1)
            for ZW1 in range(order_list[sort_index],input_value + 1):
                int_list.append(ZW1)
            for ZW2 in range(1,order_list[sort_index]):
                int_list.append(ZW2)
            return int_list
    def RandomData(self):
        data_list = []
        for row in range(self.table_led.rowCount()):
            row_data = []
            for col in range(self.table_led.columnCount()):
                item = self.table_led.item(row, col)
                if item is not None:
                    if col == 1 or col == 2:
                        row_data.append(float(item.text()))
                    else:
                        row_data.append(item.text())
            data_list.append(row_data)
        return data_list

    def Led_SetHeader_Run(self):
        self.led_header_order = ['位号', 'X坐标', 'Y坐标', 'R角度']
        self.SetHeader(self.table_led,self.led_header_order,self.split_Part)




