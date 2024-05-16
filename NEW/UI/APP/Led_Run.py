import pandas as pd
import random
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import sys
from qt_material import apply_stylesheet
from NEW.UI.UIC.LED import Ui_MainWindow as LED

class LedWindow(QMainWindow,LED):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.resetHeaders()
        self.selected_column = None
        self.table.horizontalHeader().setContextMenuPolicy(Qt.CustomContextMenu)
        self.table.horizontalHeader().customContextMenuRequested.connect(self.showContextMenu)
        self.split_Part.clicked.connect(self.PartRandom)
        self.SetHeader_btn.clicked.connect(self.SetHeader)
        self.header_order = ['位号', 'X坐标', 'Y坐标', 'R角度', '站位']
        self.input_dialog = QInputDialog(self)
        self.input_dialog.setInputMode(QInputDialog.InputMode.IntInput)
        self.input_dialog.setIntRange(2, 65)
        self.input_dialog.setIntValue(2)
        self.input_dialog.setLabelText('请输入需要插花的数量')
        self.input_dialog.setWindowTitle('LED插花')
        self.input_dialog.setOkButtonText('确定')
        self.input_dialog.setCancelButtonText('取消')
        self.input_dialog.setWindowModality(Qt.WindowModality.ApplicationModal)
    def addTableData(self,table_data):
        self.table.clearContents()
        num_rows = table_data.shape[0]
        num_cols = table_data.shape[1]
        self.table.setRowCount(num_rows)
        self.table.setColumnCount(num_cols)
        self.data_list = table_data.values.tolist()
        for rowIndex, row in enumerate(self.data_list):
            for columnIndex, item in enumerate(row):
                self.table.setItem(rowIndex, columnIndex, QTableWidgetItem(str(item)))
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    def showContextMenu(self,pos):
        header=self.table.horizontalHeader()
        index=header.logicalIndexAt(pos)
        if self.selected_column is not None and self.selected_column != index:
            for row in range(self.table.rowCount()):
                item=self.table.item(row,self.selected_column)
                if item:
                    item.setSelected(False)
        self.selected_column=index
        for row in range(self.table.rowCount()):
            item=self.table.item(row,index)
            if item:
                item.setSelected(True)
        self.context_menu.exec(self.table.mapToGlobal(pos))
    def action_Triggered(self,tiggered):
        if self.selected_column is not None:
            new_header_item=QTableWidgetItem(tiggered.text())
            self.table.setHorizontalHeaderItem(self.selected_column,new_header_item)
        if tiggered:
            tiggered.triggered.disconnect()
            self.context_menu.removeAction(tiggered)
    def resetHeaders(self):
        for i in range(self.table.columnCount()):
            item=QTableWidgetItem(f"{i+1}")
            self.table.setHorizontalHeaderItem(i,item)
        self.context_menu = QMenu(self)
        action_Ref = self.context_menu.addAction('位号')
        action_X = self.context_menu.addAction('X坐标')
        action_Y = self.context_menu.addAction('Y坐标')
        action_R = self.context_menu.addAction('R角度')
        action_Part = self.context_menu.addAction('站位')
        action_Reset = self.context_menu.addAction('Reset')
        action_Ref.triggered.connect(lambda: self.action_Triggered(action_Ref))
        action_X.triggered.connect(lambda: self.action_Triggered(action_X))
        action_Y.triggered.connect(lambda: self.action_Triggered(action_Y))
        action_R.triggered.connect(lambda: self.action_Triggered(action_R))
        action_Part.triggered.connect(lambda: self.action_Triggered(action_Part))
        action_Reset.triggered.connect(self.resetHeaders)
    def exportTableData(self):
        data_list = []
        for row in range(self.table.rowCount()):#遍历表格的行
            row_data = []#创建一个空列表
            for col in range(self.table.columnCount()):#遍历表格的列
                item = self.table.item(row, col)#获取表格的单元格
                if item is not None:#判断单元格是否为空
                    row_data.append(item.text())#将单元格的数据添加到列表中
            data_list.append(row_data)#将列表添加到列表中
        return data_list
    def import_csv(self):
        file = QFileDialog.getOpenFileName(self, '导入CSV坐标', '..', '文件(*.csv);;所有文件(*.*)')
        if file[0] == '':
            return
        data = pd.read_csv(file[0], header=None)
        data.fillna('',inplace=True)
        self.addTableData(data)
    def export_csv(self):
        file = QFileDialog.getSaveFileName(self, '导出CAD坐标', '..', '文件(*.csv);;所有文件(*.*)')
        if file[0] == '':
            return
        df = pd.DataFrame(self.exportTableData())  # 将列表转换成DataFrame类型
        df.to_csv(file[0], index=False, header=False)  # 将数据保存到文件中
        QMessageBox.information(self, '提示', '导出成功')
        self.close()
    def PartRandom(self):
        self.input_dialog.show()
        if self.input_dialog.exec()==QInputDialog.DialogCode.Accepted:
            input_value=self.input_dialog.intValue()
        sorted_lst_x = sorted(self.RandomData(), key=lambda x: x[1])  # 根据X坐标进行排序
        sorted_lst_y = sorted(sorted_lst_x, key=lambda x: x[2])  # 根据Y坐标进行排序
        min_list = min(sorted_lst_y, key=lambda x: x[2])
        lst=self.order_list(input_value)
        min_value = min_list[2]  # 获取子列表中的Y坐标的最小值
        index_one=0
        index_two=0
        index_three=0
        index_four=0
        while index_one != len(sorted_lst_y):
            if sorted_lst_y[index_one][2] == min_value:
                sorted_lst_y[index_one].append(lst[index_two])
                index_one += 1
                index_two = (index_two + 1) % len(lst)
            elif sorted_lst_y[index_one][2] > sorted_lst_y[index_one - 1][2]:
                if index_three < len(lst) - 1:
                    index_three += 1
                else:
                    index_three = 0
                lst = self.order_list(input_value,index_three)
                sorted_lst_y[index_one].append(lst[index_four])
                index_one += 1
                index_four= (index_four + 1) % len(lst)
            else:
                continue
        print(sorted_lst_y)
    def order_list(self,input_value,sort_index=0):
        int_list=[]
        if input_value == 2:
            order_list=[1,2]
            for item in range(order_list[sort_index],3):
                int_list.append(item)
            for item_ in range(1,order_list[sort_index]):
                int_list.append(item_)
            return int_list
        elif input_value == 48:
            order_list=[1, 37, 6, 44, 15, 27, 22, 32, 12, 41, 5, 48, 11, 26, 19, 31, 23, 38, 4, 33, 16, 45, 10, 42,
                        25, 13,30,20,39, 3, 46, 8, 36, 17, 29, 24, 35, 2, 43, 7, 47, 14, 28, 9, 40, 21, 34, 18]
            for item in range(order_list[sort_index],49):
                int_list.append(item)
            for item_ in range(1,order_list[sort_index]):
                int_list.append(item_)
            return int_list
        else:
            order_list=[1] + random.sample(range(2, input_value + 1), input_value - 1)
            for item in range(order_list[sort_index],input_value-1):
                int_list.append(item)
            for item_ in range(1,order_list[sort_index]):
                int_list.append(item_)
            return int_list
    def RandomData(self):
        data_list = []
        for row in range(self.table.rowCount()):
            row_data = []
            for col in range(self.table.columnCount()):
                item = self.table.item(row, col)
                if item is not None:
                    if col == 1 or col == 2:
                        row_data.append(float(item.text()))
                    else:
                        row_data.append(item.text())
            data_list.append(row_data)
        return data_list
    def SetHeader(self):
        header_texts = []
        columns_to_delete=[]
        for i in range(self.table.columnCount()):
            header_item=self.table.horizontalHeaderItem(i)
            if header_item is not None:
                header_texts.append(header_item.text())
            else:
                columns_to_delete.append(i)

        if set(header_texts) == set(self.header_order):
            for col_index in columns_to_delete:
                self.table.removeColumn(col_index)
            new_header_indexes = [header_texts.index(header) for header in self.header_order]
            new_columns_data=[]
            for new_index in new_header_indexes:
                column_data = [self.table.item(row,new_index).text() for row in range(self.table.rowCount())]
                new_columns_data.append(column_data)

            self.table.clearContents()
            self.table.setColumnCount(len(new_columns_data))
            self.table.setHorizontalHeaderLabels(self.header_order)
            for col,column_data in enumerate(new_columns_data):
                for row,data in enumerate(column_data):
                    item=QTableWidgetItem(data)
                    self.table.setItem(row,col,item)
        else:
            QMessageBox.information(self, '提示', '表头栏未定义')


if __name__ == "__main__":
    app=QApplication(sys.argv)
    apply_stylesheet(app, theme='light_pink.xml')
    win=LedWindow()
    win.show()
    sys.exit(app.exec())