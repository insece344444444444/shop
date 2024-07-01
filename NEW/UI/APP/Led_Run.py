import random
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from NEW.UI.UIC.LED import Ui_MainWindow as LED
from NEW.UI.APP.Table_logic import Table_Logic as tb

class LedWindow(QMainWindow,LED,tb):
    def __init__(self):
        super().__init__()
        self.setupUi(self)#加载UI
        self.setStyleSheet('''
                QPushButton{
                    background-color:rgb(255, 255, 255);
                    border-radius:10px;
                }
                QPushButton:hover{
                    background-color:rgb(255, 192, 203);
                    color:rgb(255, 255, 255);
                }
                ''')#设置样式

        self.selected_column = None#当前选中的列

        self.resetHeaders()#重置表头
        self.table_led.horizontalHeader().setContextMenuPolicy(Qt.CustomContextMenu)#设置表头的右键菜单,作用是在表头右键点击时触发信号
        self.table_led.horizontalHeader().setContextMenuPolicy(Qt.DefaultContextMenu)#设置默认的右键菜单
        self.table_led.horizontalHeader().sectionClicked.connect(self.showContextMenu)#绑定表头右键菜单

        self.split_Part.clicked.connect(self.PartRandom)#绑定打散按钮
        self.split_Part.setEnabled(False)#设置按钮不可用
        self.SetHeader_btn.clicked.connect(self.Led_SetHeader_Run)#绑定设置表头按钮

        self.input_dialog = QInputDialog(self)#创建输入对话框
        self.input_dialog.setInputMode(QInputDialog.InputMode.IntInput)#设置输入模式
        self.input_dialog.setIntRange(2, 65)#设置输入范围
        self.input_dialog.setIntValue(2)#设置默认值
        self.input_dialog.setLabelText('请输入需要打散的站位数量')#设置标签文本
        self.input_dialog.setWindowTitle('LED插花')#设置标题
        self.input_dialog.setOkButtonText('确定')#设置确定按钮文本
        self.input_dialog.setCancelButtonText('取消')#设置取消按钮文本
        self.input_dialog.setWindowModality(Qt.WindowModality.ApplicationModal)#设置窗口模态

    def context(self):
        self.context_menu = QMenu(self)#创建右键菜单
        #添加菜单项
        self.action_Ref = self.context_menu.addAction('位号')
        self.action_X = self.context_menu.addAction('X坐标')
        self.action_Y = self.context_menu.addAction('Y坐标')
        self.action_R = self.context_menu.addAction('R角度')
        self.action_Reset = self.context_menu.addAction('Reset')
        #绑定菜单项
        self.action_Ref.triggered.connect(lambda: self.action_Trigger(self.action_Ref,self.table_led,self.selected_column,self.context_menu))
        self.action_X.triggered.connect(lambda: self.action_Trigger(self.action_X,self.table_led,self.selected_column,self.context_menu))
        self.action_Y.triggered.connect(lambda: self.action_Trigger(self.action_Y,self.table_led,self.selected_column,self.context_menu))
        self.action_R.triggered.connect(lambda: self.action_Trigger(self.action_R,self.table_led,self.selected_column,self.context_menu))
        self.action_Reset.triggered.connect(self.resetHeaders)


    def showContextMenu(self,index):
        if not hasattr(self,'context_menu'):#如果没有右键菜单
            self.context()#创建右键菜单
        if index != self.selected_column:#如果点击的列不是当前选中的列
            self.clearColumnHighlight(self.table_led, self.selected_column)#清除当前选中列的高亮
            self.selected_column = index#设置当前选中的列
            self.highlightColumn(index, self.table_led)#高亮当前选中的列
        cursor_position = QCursor.pos()  # 获取当前鼠标的位置
        self.context_menu.exec(cursor_position)#在鼠标位置显示菜单


    def resetHeaders(self):
        self.resetHeader(self.table_led)#重置表头
        self.context()#创建右键菜单
    def import_csv(self):
        data = self.openfile()#打开文件
        self.addTableData(data,self.table_led)#添加数据到表格
        self.resetHeaders()#重置表头
    def export_csv(self):
        datalist=self.exportTableData(self.table_led)#导出表格数据
        self.exportfile(datalist)#导出数据到文件
    def PartRandom(self):
        if hasattr(self,'context_menu'):#如果有右键菜单
            self.input_dialog.show()#显示输入对话框
            if self.input_dialog.exec()==QInputDialog.DialogCode.Accepted:#如果点击了确定按钮
                input_value=self.input_dialog.intValue()#获取输入的值
            sorted_lst_x = sorted(self.RandomData(), key=lambda x: x[1])  # 根据X坐标进行排序
            sorted_lst_y = sorted(sorted_lst_x, key=lambda x: x[2])  # 根据Y坐标进行排序
            lst = self.order_list(input_value, 0)#获取排序后的列表
            min_list = min(sorted_lst_y, key=lambda x: x[2])#获取Y坐标最小值
            min_value = min_list[2]  # 获取子列表中的Y坐标的最小值
            #初始化索引
            index_one=0
            index_two=0
            index_three=0
            index_four=0
            while index_two != len(sorted_lst_y):#当索引不等于列表长度时
                if sorted_lst_y[index_two][2] == min_value:#如果Y坐标等于最小值
                    sorted_lst_y[index_two].append(lst[index_three])#添加到列表中
                    index_two += 1#索引加1
                    index_three = (index_three + 1) % len(lst)#索引取余
                elif sorted_lst_y[index_two][2] > sorted_lst_y[index_two - 1][2]:#如果Y坐标大于前一个Y坐标
                    if index_one < len(lst) - 1:#如果索引小于列表长度-1
                        index_one += 1#索引加1
                    else:
                        index_one = 0#索引等于0
                    lst = self.order_list(input_value,index_one)#获取排序后的列表
                    index_four=0#索引等于0
                    sorted_lst_y[index_two].append(lst[index_four])#添加到列表中
                    index_two += 1#索引加1
                    index_four= (index_four + 1) % len(lst)#索引取余
                elif sorted_lst_y[index_two][2] == sorted_lst_y[index_two-1][2]:#如果Y坐标等于前一个Y坐标
                    sorted_lst_y[index_two].append(lst[index_four])#添加到列表中
                    index_two += 1#索引加1
                    index_four = (index_four + 1) % len(lst)#索引取余
                else:
                    continue#继续
            new_column_count=self.table_led.columnCount()#获取列数
            self.table_led.setColumnCount(new_column_count + 1)#设置列数
            headers = [self.table_led.horizontalHeaderItem(i).text() for i in range(new_column_count)]#获取表头
            headers.append('插花序列')#添加表头
            self.table_led.setHorizontalHeaderLabels(headers)#设置表头
            for rowIndex, row in enumerate(sorted_lst_y):  # 遍历数据
                for columnIndex, item in enumerate(row):  # 遍历数据
                    self.table_led.setItem(rowIndex, columnIndex, QTableWidgetItem(str(item)))#设置单元格
            self.split_Part.setEnabled(False)#设置按钮不可用

    def order_list(self,input_value,sort_index=0):
        if input_value == 2:#如果输入的值等于2
            int_list = []#创建一个空列表
            order_list=[1,2]#创建一个列表
            for ZW1 in range(order_list[sort_index],3):#遍历列表
                int_list.append(ZW1)#添加到列表中
            for ZW2 in range(1,order_list[sort_index]):#遍历列表
                int_list.append(ZW2)#添加到列表中
            return int_list #返回列表
        elif input_value == 48:#如果输入的值等于48
            int_list = []#创建一个空列表
            order_list=[1, 37, 6, 44, 15, 27, 22, 32, 12, 41, 5, 48, 11, 26, 19, 31, 23, 38, 4, 33, 16, 45, 10, 42,
                        25, 13,30,20,39, 3, 46, 8, 36, 17, 29, 24, 35, 2, 43, 7, 47, 14, 28, 9, 40, 21, 34, 18]
            for ZW1 in range(order_list[sort_index],49):#遍历列表
                int_list.append(ZW1)#添加到列表中
            for ZW2 in range(1,order_list[sort_index]):#遍历列表
                int_list.append(ZW2)#添加到列表中
            return int_list#返回列表
        else:
            int_list = []#创建一个空列表
            order_list=[1] + random.sample(range(2, input_value + 1),input_value - 1)#创建一个列表
            for ZW1 in range(order_list[sort_index],input_value + 1):#遍历列表
                int_list.append(ZW1)#添加到列表中
            for ZW2 in range(1,order_list[sort_index]):#遍历列表
                int_list.append(ZW2)#添加到列表中
            return int_list#返回列表
    def RandomData(self):
        data_list = []#创建一个空列表
        for row in range(self.table_led.rowCount()):#遍历表格的行
            row_data = []#创建一个空列表
            for col in range(self.table_led.columnCount()):#遍历表格的列
                item = self.table_led.item(row, col)#获取单元格
                if item is not None:#判断单元格是否为空
                    if col == 1 or col == 2:#如果是X坐标或Y坐标
                        row_data.append(float(item.text()))#添加到列表中
                    else:
                        row_data.append(item.text())#添加到列表中
            data_list.append(row_data)#添加到列表中
        return data_list#返回列表

    def Led_SetHeader_Run(self):
        self.led_header_order = ['位号', 'X坐标', 'Y坐标', 'R角度']
        self.SetHeader(self.table_led,self.led_header_order,self.split_Part)#设置表头




