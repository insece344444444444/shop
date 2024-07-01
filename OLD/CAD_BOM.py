import os
import re
import pdfplumber
import pandas as pd
from PySide6.QtWidgets import QWidget, QPushButton, QTableWidget, QHBoxLayout, QVBoxLayout, QFileDialog, \
    QTableWidgetItem, QHeaderView, QMessageBox, QAbstractItemView
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPixmap
import Lance

class CadWindow(QWidget):#创建一个类，继承QWidget类
    def __init__(self):
        super().__init__()
        self.resize(800,600)#设置窗口大小
        self.setWindowTitle('CAD合并')  # 设置窗口标题
        self.setWindowIcon(QPixmap(':/icon/Lance.png'))  # 设置窗口图标
        # 设置按钮的默认背景颜色和鼠标悬停时按钮的背景颜色
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
        # background-color:rgb代表背景颜色
        # border-radius:10px代表圆角半径
        # border:2px solid rgb(255, 170, 127)代表边框宽度和颜色
        # font-size:20px代表字体大小
        # font-weight:700代表字体粗细
        # color:rgb(255, 170, 127)代表字体颜色
        # height:40px代表按钮高度
        self.btn1 = QPushButton('CAD导入', self)  # 创建一个按钮
        self.btn1.clicked.connect(self.import_csv)  # 为按钮绑定事件
        self.btn2 = QPushButton('BOM拆分', self)  # 创建一个按钮
        self.btn2.clicked.connect(self.import_bom)  # 为按钮绑定事件
        self.btn3 = QPushButton('导出坐标', self)  # 创建一个按钮
        self.btn3.clicked.connect(self.export_cad)  # 为按钮绑定事件
        self.table = QTableWidget()  # 创建一个表格
        self.searchlayout = QHBoxLayout()  # 创建一个水平布局
        self.searchlayout.addWidget(self.btn1)  # 将按钮添加到布局中
        self.searchlayout.addWidget(self.btn2)  # 将按钮添加到布局中
        self.searchlayout.addWidget(self.btn3)  # 将按钮添加到布局中

        subLayout = QVBoxLayout()  # 创建一个垂直布局
        subLayout.addLayout(self.searchlayout)  # 将水平布局添加到布局中
        subLayout.addWidget(self.table)  # 将表格添加到布局中
        self.setLayout(subLayout)  # 设置布局
        self.btn2.setEnabled(False)
        self.btn3.setEnabled(False)
    def import_csv(self):
        file = QFileDialog.getOpenFileName(self, '导入CSV坐标', '..', '文件(*.csv);;所有文件(*.*)')  # 获取文件路径
        if file[0] == '':  # 判断是否选择了文件
            return
        data = pd.read_csv(file[0], header=None)  # 读取文件
        num_rows = data.shape[0]  # 获取行数
        self.table.clear()#清空表格
        self.table.setRowCount(num_rows)  # 设置表格的行数
        self.table.setColumnCount(5)  # 设置表格的列数
        self.data_list = data.values.tolist()  # 转换成列表
        for rowIndex, row in enumerate(self.data_list):  # 遍历数据
            for columnIndex, item in enumerate(row):  # 遍历数据
                self.table.setItem(rowIndex, columnIndex, QTableWidgetItem(str(item)))  # 将数据添加到表格中
        self.table.setHorizontalHeaderLabels(['Ref', 'X', 'Y', 'R', 'Part'])  # 设置表头
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)  # 设置表头的拉伸模式
        self.btn2.setEnabled(True)
    def import_bom(self):
        self.subwindow = BomWindow(self)  # 创建一个次级窗口
        self.subwindow.show()  # 显示次级窗口
        # 子窗口打开时主窗口隐藏
        self.subwindow.closeEvent = lambda event: self.show()
        # 主窗口关闭时子窗口也关闭
        self.closeEvent = lambda event: self.subwindow.close()
        self.hide()  # 隐藏主窗口
    def displayMergedData(self,data_list,decpmpose):#这个函数名的中文意思是显示合并的数据

        cad = {item[0]: item[1:] for item in data_list}  # 将data_list中的第一列作为key,第二列到最后一列作为value
        bom = {item[2]: item[1] for item in decpmpose}  # 将decpmpose中的第三列作为key,第二列作为value
        for key,value in cad.items():#遍历cad字典
            if key in bom.keys():#判断cad字典的key是否在bom字典的key中
                value.append(bom[key])#将bom字典的key添加到cad字典的value中
            else:
                value.append('NC')
        merged_data = [[key] + value for key, value in cad.items()]  # 将cad字典的key和value合并成列表
        # 清空表格
        self.table.clearContents()
        # 将merged_data中的数据替换到表格中
        for rowIndex, row in enumerate(merged_data):
            for columnIndex, item in enumerate(row):
                self.table.setItem(rowIndex, columnIndex, QTableWidgetItem(str(item)))
        #隐藏子窗口，显示主窗口
        self.subwindow.hide()
        self.show()
        self.btn3.setEnabled(True)
    def export_cad(self):
        file,_= QFileDialog.getSaveFileName(self, '导出CAD坐标', '..', '文件(*.csv);;所有文件(*.*)')  # 获取文件路径
        if file == '':  # 判断是否选择了文件
            return
        with open(file, 'w') as f:  # 打开文件
            for row in range(self.table.rowCount()):#遍历表格的行数
                row_data = []#创建一个空列表
                for column in range(self.table.columnCount()):#遍历表格的列数
                    item = self.table.item(row, column)#获取表格的数据
                    row_data.append(item.text())#将数据添加到row_data中
                f.write(','.join(row_data) + '\n')#使用join函数将row_data中的数据用,连接起来,用\n换行,写入文件
        QMessageBox.information(self, '提示', '导出成功')  # 弹出提示框
        self.close()#关闭窗口
class BomWindow(QWidget):
    mergeCompleted = Signal(list)  # 创建一个信号
    def __init__(self,parent=None):#初始化方法,parent的默认值为None,作用是为了让子窗口能够访问主窗口的属性
        super().__init__()
        self.parent=parent#将主窗口的属性赋值给子窗口的parent属性
        self.resize(600,600)#设置窗口大小
        self.setWindowTitle('BOM')  # 设置窗口标题
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu) # 设置窗体的上下文菜单策略
        self.dele=QAction('删除')
        self.addAction(self.dele)
        self.btn1 = QPushButton('BOM导入', self)  # 创建一个按钮
        self.btn1.clicked.connect(self.bom)  # 为按钮绑定事件
        self.btn2 = QPushButton('提取内容', self)  # 创建一个按钮
        self.btn2.clicked.connect(self.tidy_bom)  # 为按钮绑定事件
        self.btn3= QPushButton('文字过滤', self)  # 创建一个按钮
        self.btn3.clicked.connect(self.bom_filtration)  # 为按钮绑定事件
        self.btn4= QPushButton('位号拆分', self)  # 创建一个按钮
        self.btn4.clicked.connect(self.bom_spilt)  # 为按钮绑定事件
        self.btn5=QPushButton('检查用量',self)#创建一个按钮
        self.btn5.clicked.connect(self.bom_inspect)#为按钮绑定事件
        self.btn6= QPushButton('合并', self)  # 创建一个按钮
        self.table = QTableWidget()  # 创建一个表格
        self.SubLayout = QHBoxLayout()  # 创建一个水平布局
        self.SubLayout.addWidget(self.btn1)  # 将按钮添加到布局中
        self.SubLayout.addWidget(self.btn2)  # 将按钮添加到布局中
        self.SubLayout.addWidget(self.btn3)  # 将按钮添加到布局中
        self.SubLayout.addWidget(self.btn4)  # 将按钮添加到布局中
        self.SubLayout.addWidget(self.btn5)  # 将按钮添加到布局中
        self.SubLayout.addWidget(self.btn6)  # 将按钮添加到布局中
        self.mainLayout = QVBoxLayout()  # 创建一个垂直布局
        self.mainLayout.addLayout(self.SubLayout)  # 将水平布局添加到布局中
        self.mainLayout.addWidget(self.table)  # 将表格添加到布局中
        self.setLayout(self.mainLayout)  # 设置布局
        self.btn2.setEnabled(False)
        self.btn3.setEnabled(False)
        self.btn4.setEnabled(False)
        self.btn5.setEnabled(False)
        self.btn6.setEnabled(False)
        self.bind()
    def bind(self):
        self.dele.triggered.connect(self.delete_selected_items)
        self.mergeCompleted.connect(self.parent.displayMergedData)
        self.btn6.clicked.connect(self.Merge)

    def delete_selected_items(self):
        selected_rows = set()  # 使用集合来存储选中的行索引，以去除重复项
        selected_items = self.table.selectedItems()  # 获取选中的表格项
        for item in selected_items:
            selected_rows.add(item.row())  # 将选中的行索引添加到集合中

        # 从最后一行开始删除，以避免删除时的索引错位
        for row in sorted(selected_rows, reverse=True):
            self.table.removeRow(row)  # 删除选中的行
    def bom(self):
        self.btn3.setEnabled(False)
        self.btn4.setEnabled(False)
        self.btn5.setEnabled(False)
        self.btn6.setEnabled(False)
        msg_box = QMessageBox()#创建一个QMessageBox对象
        msg_box.setWindowTitle("选择")#设置标题
        msg_box.setText("请选择BOM的格式")#设置文本
        msg_box.setIcon(QMessageBox.Icon.Information)#设置图标
        #添加自定义按钮
        msg_box.addButton("BOM格式(csv)", QMessageBox.ButtonRole.YesRole)
        msg_box.addButton("BOM格式(PDF)", QMessageBox.ButtonRole.NoRole)
        msg_box.addButton("取消", QMessageBox.ButtonRole.RejectRole)
        msg_box.exec()#显示消息框
        if msg_box.clickedButton().text()=='BOM格式(csv)':#判断点击的按钮
            self.file,_= QFileDialog.getOpenFileName(self, '导入csv格式bom', '..', '文件(*.csv);;所有文件(*.*)')  # 获取文件路径
            if self.file == '':  # 判断是否选择了文件
                return
            data = pd.read_csv(self.file, header=None)  # 读取文件
            num_rows = data.shape[0]  # 获取行数
            num_cols = data.shape[1]  # 获取列数
            self.table.setRowCount(num_rows)  # 设置表格的行数
            self.table.setColumnCount(num_cols)  # 设置表格的列数
            self.bom_list = data.values.tolist()  # 转换成列表
            for rowIndex, row in enumerate(self.bom_list):  # 遍历数据
                for columnIndex, item in enumerate(row):
                    self.table.setItem(rowIndex, columnIndex, QTableWidgetItem(str(item)))  # 将数据添加到表格中
            self.table.setHorizontalHeaderLabels(['料号', '数量', '位号'])  # 设置表头
            self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)  # 设置表头的拉伸模式
            self.btn4.setEnabled(True)
        elif msg_box.clickedButton().text()=='BOM格式(PDF)':
            self.bom_list = []  # 创建一个空列表
            self.file,_= QFileDialog.getOpenFileName(self, '导入pdf格式bom', '..', '文件(*.pdf);;所有文件(*.*)')  # 获取文件路径
            if self.file == '':  # 判断是否选择了文件
                return
            with pdfplumber.open(self.file) as pdf:  # 打开PDF文件
                for i in pdf.pages:  # 遍历PDF的页数赋值给i
                    text = i.extract_tables()  # 提取PDF内容赋值给text
                    for item in text:  # 遍历text中的内容赋值给item
                        for items in item:  # 遍历item中的内容赋值给items
                            self.bom_list.append(items)  # 将items添加到bom_list中
            num_rows = len(self.bom_list)  # 获取行数
            num_cols = len(self.bom_list[0])  # 获取列数
            self.table.setRowCount(num_rows)  # 设置表格的行数
            self.table.setColumnCount(num_cols)  # 设置表格的列数
            for rowIndex, row in enumerate(self.bom_list):  # 遍历数据
                for columnIndex, item in enumerate(row):  # 遍历数据
                    self.table.setItem(rowIndex, columnIndex, QTableWidgetItem(str(item)))  # 将数据添加到表格中
            self.btn2.setEnabled(True)
    def tidy_bom(self):
        self.btn2.setEnabled(False)
        self.bom_list=[]
        for row in range(self.table.rowCount()):  # 遍历表格的行数
            row_data = []  # 创建一个空列表
            for column in range(self.table.columnCount()):  # 遍历表格的列数
                item = self.table.item(row, column)  # 获取表格的数据
                row_data.append(item.text())
            self.bom_list.append(row_data)  # 将数据添加到bom_list中  num_rows = len(self.bom_list)  # 获取行数
        self.bom_list1 = []  # 创建一个空列表
        for i in self.bom_list:  # 遍历bom()中的列表
            part_Number = i[1]  # 将i[1]赋值给parts
            parts= i[2]  # 将i[2]赋值给parts
            pcs = i[4]  # 将i[4]赋值给pcs
            ref = i[7]  # 将i[7]赋值给ref
            self.bom_list1.append([part_Number,parts, pcs, ref])  # 将parts,pcs,ref添加到bom_list中
        #清空表格
        self.table.clear()
        num_rows = len(self.bom_list1)  # 获取行数
        num_col = len(self.bom_list1[0]) # 获取列数
        #设置表格的行数
        self.table.setRowCount(num_rows)
        # 设置表格的列数
        self.table.setColumnCount(num_col)
        # 将bom_list1中的数据替换到表格中
        for rowIndex, row in enumerate(self.bom_list1):
            for columnIndex, item in enumerate(row):
                self.table.setItem(rowIndex, columnIndex, QTableWidgetItem(str(item)))
        QMessageBox.information(self,'提示','右键可以删除不需要的行\n位号不能为空和None')
        self.btn3.setEnabled(True)
    def bom_filtration(self):
        self.btn3.setEnabled(False)
        self.bom_list = []  # 创建一个空列表
        ic = r'IC(.+)? (\w+)'  # 正则表达式
        C = r'电容.+? (\d+),([a-zA-Z]+),?.+?,-(\d+%).+%.+(\b\d{4}\b)'
        R = r'电阻.+? (\d+),(Ω),-(\d+%).+%.+(\b\d{4}\b)'
        RP = r'排阻.+? (\d+),(Ω),-(\d+%).+%.+(\b\d{4}\b)'
        DC = r'电解电容.+? (\d+),([a-zA-Z]+),(\d+V),-(\d+%).+%'
        XD = r'聚合物铝电容.+?(\d+).0?,([a-zA-Z]+),(\d+V),-(\d+%).+%'
        XY = r'小样.+?(Ω),-(\d+%).+%.+(\b\d{4}\b).+?(\w)色灯用'
        CZ=r'磁珠.+?(.?\d+),(Ω).+?-(\d+%).+%.+?(\b\d{4}\b)'
        for row in range(self.table.rowCount()):  # 遍历表格的行数
            row_data = []  # 创建一个空列表
            for column in range(self.table.columnCount()):  # 遍历表格的列数
                item = self.table.item(row, column)  # 获取表格的数据
                row_data.append(item.text())
            self.bom_list.append(row_data)  # 将数据添加到bom_list中
        for i in self.bom_list:  # 遍历bom_list中的列表
            i[3] = i[3].replace('，', ',')  # 将子列表中的中文分隔符，替换成英文分隔符,
            r1=re.split(r'[, ]',i[3])#使用正则表达式将i[2]中的,和空格分隔开赋值给i[2]
            while '' in r1:#判断r1中是否有''
                r1.remove('')#使用remove函数删除r1中的''
            i[3]=','.join(r1)#使用join函数将r1中的数字用,连接起来,用replace函数将i[2]中的数字替换成r1
            if re.search(ic, i[1],flags=re.DOTALL):  # 使用正则表达式判断i[1]中是否有IC
                IC=re.search(ic, i[1],flags=re.DOTALL)
                i[1] = IC.group(2)  # 使用正则表达式将i[1]中的IC替换成空
            elif re.search(C, i[1],flags=re.DOTALL):  # 使用正则表达式判断i[1]中是否有C
                c=re.search(C, i[1],flags=re.DOTALL)
                i[1] = f'{c.group(1)}{c.group(2)}/{c.group(3)}/{c.group(4)}'
            elif re.search(R, i[1],flags=re.DOTALL):  # 使用正则表达式判断i[1]中是否有R
                r=re.search(R, i[1],flags=re.DOTALL)
                i[1] = f'{r.group(1)}{r.group(2)}/{r.group(3)}/{r.group(4)}'
            elif re.search(RP, i[1],flags=re.DOTALL): # 使用正则表达式判断i[1]中是否有RP
                rp=re.search(RP, i[1],flags=re.DOTALL)
                i[1] = f'{rp.group(1)}{rp.group(2)}/{rp.group(3)}/{rp.group(4)}'
            elif re.search(DC, i[1],flags=re.DOTALL):  # 使用正则表达式判断i[1]中是否有DC
                dc=re.search(DC, i[1],flags=re.DOTALL)
                i[1] = f'{dc.group(1)}{dc.group(2)}/{dc.group(3)}/{dc.group(4)}'
            elif re.search(XD, i[1],flags=re.DOTALL):  # 使用正则表达式判断i[1]中是否有XD
                xd=re.search(XD, i[1],flags=re.DOTALL)
                i[1] = f'{xd.group(1)}{xd.group(2)}/{xd.group(3)}/{xd.group(4)}'
            elif re.search(XY, i[1],flags=re.DOTALL):  # 使用正则表达式判断i[1]中是否有XY
                xy=re.search(XY, i[1],flags=re.DOTALL)
                i[1] = f'{xy.group(4)}{xy.group(1)}/{xy.group(2)}/{xy.group(3)}'
            elif re.search(CZ, i[1],flags=re.DOTALL):  # 使用正则表达式判断i[1]中是否有CZ
                cz=re.search(CZ, i[1],flags=re.DOTALL)
                i[1] = f'{cz.group(1)}{cz.group(2)}/{cz.group(3)}/{cz.group(4)}'
            else:
                i[1] = i[1]#如果i[1]中没有IC,C,R,RP,DC,XD,则不替换
        # 清空表格
        self.table.clear()
        # 设置表头
        self.table.setHorizontalHeaderLabels(self.bom_list[0])
        #设置表头后删除
        del self.bom_list[0]
        num_rows = len(self.bom_list)  # 获取行数
        num_col=len(self.bom_list[0])  # 获取列数
        # 设置表格的行数
        self.table.setRowCount(num_rows)
        # 设置表格的列数
        self.table.setColumnCount(num_col)
        # 将bom_list中的数据替换到表格中
        for rowIndex, row in enumerate(self.bom_list):
            for columnIndex, item in enumerate(row):
                self.table.setItem(rowIndex, columnIndex, QTableWidgetItem(str(item)))
        #设置表格的拉伸模式
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        QMessageBox.information(self, '提示', 'PDF格式的BOM排版有几率会有丢失,请仔细核对是否遗漏')  # 弹出提示框
        self.btn4.setEnabled(True)
    def bom_spilt(self):
        self.btn4.setEnabled(False)
        bom_list = []  # 创建一个空列表
        b_pattern = r'\b[a-zA-Z]*(\d+)[a-zA-Z]*\b'  # 提取数字的正则表达式
        c_pattern = r'[a-zA-Z]*(\d+)[a-zA-Z]+(\d+)[a-zA-Z]*'  # 提取数字的正则表达式
        for row in range(self.table.rowCount()):  # 遍历表格的行数
            row_data = []  # 创建一个空列表
            for column in range(self.table.columnCount()):  # 遍历表格的列数
                item = self.table.item(row, column)  # 获取表格的数据
                row_data.append(item.text())
            bom_list.append(row_data)  # 将数据添加到bom_list中

        for item in bom_list:  # 遍历bom_list中的列表
            ref_nums = item[-1].replace('，', ',').split(',')  # 将子列表中的中文分隔符，替换成英文分隔符,并拆分成列表
            new_ref_nums = []  # 创建一个空列表
            for ref_num in ref_nums:  # 遍历参考号列表
                if '-' in ref_num:  # 判断参考号中是否有-
                    if re.search(b_pattern, ref_num):  # 判断参考号中是否匹配b_pattern
                        start, end = ref_num.split('-')  # 将参考号中的-分隔开
                        start_num = int(re.search(b_pattern, start).group(1))  # 提取起始数字
                        end_num = int(re.search(b_pattern, end).group(1))  # 提取结束数字
                        new_ref_nums.extend(
                            [start.replace(str(start_num), str(i)) for i in range(start_num, end_num + 1)])
                    elif re.search(c_pattern, ref_num):  # 判断参考号中是否匹配c_pattern
                        start, end = ref_num.split('-')  # 将参考号中的-分隔开
                        start_num1, start_num2 = re.search(c_pattern, start).groups()  # 提取起始数字
                        end_num1, end_num2 = re.search(c_pattern, end).groups()  # 提取结束数字
                        new_ref_nums.extend([re.sub(r'(\d+)', str(h), start).replace(str(start_num2), str(k))
                                             for h in range(int(start_num1), int(end_num1) + 1)
                                             for k in range(int(start_num2), int(end_num2) + 1)])
                else:
                    new_ref_nums.append(ref_num)  # 如果参考号中没有-，直接添加到新的参考号列表中
            item[-1] = ','.join(new_ref_nums)  # 将新的参考号列表转换为字符串，并替换原来的参考号

        self.bom_list = bom_list  # 更新bom_list
        num_rows = len(self.bom_list)  # 获取行数
        num_col = len(self.bom_list[0])  # 获取列数
        # 设置表格的行数
        self.table.setRowCount(num_rows)
        # 设置表格的列数
        self.table.setColumnCount(num_col)
        # 将bom_list中的数据替换到表格中
        for rowIndex, row in enumerate(self.bom_list):
            for columnIndex, item in enumerate(row):
                self.table.setItem(rowIndex, columnIndex, QTableWidgetItem(str(item)))
        # 设置表格的拉伸模式
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.btn5.setEnabled(True)
    def bom_inspect(self):
        self.btn5.setEnabled(False)
        self.bom_list = []  # 创建一个空列表
        for row in range(self.table.rowCount()):  # 遍历表格的行数
            row_data = []  # 创建一个空列表
            for column in range(self.table.columnCount()):  # 遍历表格的列数
                item = self.table.item(row, column)  # 获取表格的数据
                row_data.append(item.text())
            self.bom_list.append(row_data)  # 将数据添加到bom_list中
        if 'None' in (self.bom_list[-1]) or '' in (self.bom_list[-1]):
            QMessageBox.information(self, '提示', '存在位号为空的情况\n请检查BOM')
            self.btn5.setEnabled(True)
            # 终止程序
            return
        #清空表格
        self.table.clearContents()
        for row,i in enumerate(self.bom_list):
            # 将小数符串转换成整数类型
            if '.' in str(i[-2]):
                i[-2] = int(float(i[-2]))
            else:
                i[-2] = int(i[-2])
            pcs = i[-2]
            ref_pcs = len(i[-1].split(','))
            # 判断PCS和参考号数量是否相等
            if pcs == ref_pcs:
                i.append('OK')
            else:
                i.append('NG')
            for columnIndex, item in enumerate(i):
                # 设置表格的列数
                self.table.setColumnCount(len(i))
                # 在不动前面的列的表头情况下，设置第5列的表头
                self.table.setHorizontalHeaderItem((len(i)-1), QTableWidgetItem('检查结果'))
                self.table.setItem(row, columnIndex, QTableWidgetItem(str(item)))
        # 设置表格的拉伸模式
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        if 'NG' in str(self.bom_list):
            QMessageBox.information(self, '提示', '存在用量和位号数量不相等的情况\n请检查BOM')
        else:
            self.btn6.setEnabled(True)#如果不存在用量和位号数量不相等的情况,则启用合并按钮
    def Merge(self):
        self.bom_list = []
        for row in range(self.table.rowCount()):  # 遍历表格的行数
            row_data = []  # 创建一个空列表
            for column in range(self.table.columnCount()):  # 遍历表格的列数
                item = self.table.item(row, column)  # 获取表格的数据
                row_data.append(item.text())#将数据添加到row_data中
            self.bom_list.append(row_data)  # 将数据添加到bom_list中
        self.decpmpose=[]#创建一个空列表
        for i in self.bom_list:#遍历bom_list中的列表
            r1=i[-2].split(',')#使用split函数将i[2]中的,分隔开赋值给r1
            for item in r1:#遍历r1中的内容
                #如果导入的是常规BOM格式(csv)则使用i[0]作为位号,如果导入的是联建BOM格式(PDF)则使用i[1]作为位号
                if self.file.endswith('.csv'):
                    self.decpmpose.append([i[1],i[0],item])#将i[1],i[0],item添加到decpmpose中
                elif self.file.endswith('.pdf'):
                    self.decpmpose.append([i[0],i[1],item])#将i[0],i[1],item添加到decpmpose中，
        self.parent.displayMergedData(self.parent.data_list, self.decpmpose)  # 调用主窗口的displayMergedData方法
        self.mergeCompleted.emit(self.decpmpose)#发送信号