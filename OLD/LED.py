import pandas as pd
import random
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QTableWidget, QVBoxLayout, QFileDialog, \
    QTableWidgetItem, QHeaderView, QMessageBox, QInputDialog, QLineEdit
from PySide6.QtGui import QPixmap
import Lance
class LedWindow(QWidget):#创建一个类，继承QWidget类
    def __init__(self,i=0):#初始化
        self.i=i
        super().__init__()#调用父类的初始化方法
        self.resize(800, 600)#设置窗口大小
        self.setWindowTitle('LED')#设置窗口标题
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
        self.btn1= QPushButton('CAD导入', self)  # 创建一个按钮
        self.btn1.clicked.connect(self.import_csv)  # 为按钮绑定事件
        self.btn2= QPushButton('打散站位', self)  # 创建一个按钮
        self.btn2.clicked.connect(self.LED_random)  # 为按钮绑定事件
        self.btn3= QPushButton('CAD导出', self)  # 创建一个按钮
        self.btn3.clicked.connect(self.export_cad)  # 为按钮绑定事件
        self.table = QTableWidget()  # 创建一个表格
        self.searchlayout=QHBoxLayout()#创建一个水平布局
        self.searchlayout.addWidget(self.btn1)#将按钮添加到布局中
        self.searchlayout.addWidget(self.btn2)#将按钮添加到布局中
        self.searchlayout.addWidget(self.btn3)#将按钮添加到布局中

        subLayout=QVBoxLayout()#创建一个垂直布局
        subLayout.addLayout(self.searchlayout)#将水平布局添加到布局中
        subLayout.addWidget(self.table)#将表格添加到布局中
        self.setLayout(subLayout)#设置布局
        self.btn2.setEnabled(False)#设置按钮不可用
        self.btn3.setEnabled(False)#设置按钮不可用
    def import_csv(self):
        file = QFileDialog.getOpenFileName(self, '导入CSV坐标', '..', '文件(*.csv);;所有文件(*.*)')  # 获取文件路径
        if file[0] == '':  # 判断是否选择了文件
            return
        data = pd.read_csv(file[0], header=None)  # 读取文件
        num_rows = data.shape[0]  # 获取行数
        self.table.setRowCount(num_rows)  # 设置表格的行数
        self.table.setColumnCount(5)  # 设置表格的列数
        data_list = data.values.tolist()  # 转换成列表
        self.table.clearContents()#清空表格
        #替换表格数据
        for rowIndex, row in enumerate(data_list):  # 遍历数据
            for columnIndex, item in enumerate(row):  # 遍历数据
                self.table.setItem(rowIndex, columnIndex, QTableWidgetItem(str(item)))  # 将数据添加到表格中
        self.table.setHorizontalHeaderLabels(['位号', 'X', 'Y', 'R', '站位'])  # 设置表头
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)  # 设置表头的拉伸模式
        self.btn2.setEnabled(True)#设置按钮可用
    def LED_random(self):
        self.btn2.setEnabled(False)#设置按钮不可用
        global ip  # 局部变量变全局变量
        input=QInputDialog(self)#创建一个输入对话框
        input.setInputMode(QInputDialog.InputMode.IntInput)#设置输入模式
        input.setIntRange(2,65)#设置输入范围
        input.setIntValue(2)#设置默认值
        input.setLabelText('请输入Parts数量')#设置标签
        input.setWindowTitle('LED插花')#设置窗口标题
        input.setOkButtonText('确定')#设置确定按钮的文本
        input.setCancelButtonText('取消')#设置取消按钮的文本
        input.setWindowModality(Qt.WindowModality.ApplicationModal)#设置窗口模态
        input.show()#显示对话框
        #获取输入的值
        if input.exec()==QInputDialog.DialogCode.Accepted:#判断是否点击了确定按钮
            ip=input.intValue()#获取输入的值
        #获取表格数据
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
        sorted_lst_x = sorted(data_list, key=lambda x: x[1])  # 根据X坐标进行排序
        sorted_lst_y = sorted(sorted_lst_x, key=lambda x: x[2])  # 根据Y坐标进行排序
        lst = self.Ch48() if ip == 48 else self.Ch2() if ip == 2 else self.Ch()
        min_list = min(sorted_lst_y, key=lambda x: x[2])
        min_value = min_list[2]  # 获取子列表中的Y坐标的最小值
        e = 0  # 索引赋值
        I = 0  # 索引赋值
        j = 0  # 索引赋值
        h = 0  # 索引赋值
        while I != len(sorted_lst_y):  # 使用while循环判断I的值是否与坐标的行相等，相等为True，结束循环
            if sorted_lst_y[I][2] == min_value:  # 判断Y坐标是否等于最小值
                sorted_lst_y[I].append(lst[j])  # 添加插花序列
                I += 1  # 换行
                j = (j + 1) % len(lst)  # 根据除余算法按照顺序添加序列
            elif sorted_lst_y[I][2] > sorted_lst_y[I - 1][2]:  # Y坐标变动一次  插花的序列变动一次
                if e < len(lst) - 1:  # 插花的序列索引利用if判断循环
                    e += 1
                else:
                    e = 0
                self.i = e
                lst = self.Ch48() if ip == 48 else self.Ch2() if ip == 2 else self.Ch()  # 插花索引+1
                h = 0  # 重置顺序索引
                sorted_lst_y[I].append(lst[h])  # 按照重置后的顺序添加序列
                I += 1  # 继续换行
                h = (h + 1) % len(lst)  # 根据除余算法继续按照顺序添加序列
            elif sorted_lst_y[I][2] == sorted_lst_y[I - 1][2]:  # 判断变动后的行数
                sorted_lst_y[I].append(lst[h])  # 按照顺序添加序列
                I += 1  # 换行
                h = (h + 1) % len(lst)  # 根据除余算法继续按照顺序添加序列
            else:
                continue  # 返回本层循环
        #替换表格数据
        for rowIndex, row in enumerate(sorted_lst_y):  # 遍历数据
            for columnIndex, item in enumerate(row):  # 遍历数据
                self.table.setItem(rowIndex, columnIndex, QTableWidgetItem(str(item)))  # 将数据添加到表格中
        self.table.setHorizontalHeaderLabels(['Ref', 'X', 'Y', 'R', 'Parts'])  # 设置表头
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)  # 设置表头的拉伸模式
        self.btn3.setEnabled(True)#设置按钮可用
    def Ch(self):
        zw = []  # 存储整数序列
        ch = [1] + random.sample(range(2, ip + 1), ip - 1)  # 序列打散
        for zw1 in range(ch[self.i], ip + 1):  # 根据索引生成序列1
            zw.append(zw1)  # 添加到列表中
        for zw2 in range(1, ch[self.i]):  # 根据索引生成序列2
            zw.append(zw2)  # 添加到列表中
        return zw  # 返回值

    def Ch2(self):
        zw = []  # 存储整数序列
        ch = [1, 2]
        for zw1 in range(ch[self.i], 3):  # 根据索引生成序列1
            zw.append(zw1)  # 添加到列表中
        for zw2 in range(1, ch[self.i]):  # 根据索引生成序列2
            zw.append(zw2)  # 添加到列表中
        return zw  # 返回值

    def Ch48(self):  # 定义函数名和形参
        zw = []  # 存储整数序列
        ch = [1, 37, 6, 44, 15, 27, 22, 32, 12, 41, 5, 48, 11, 26, 19, 31, 23, 38, 4, 33, 16, 45, 10, 42, 25, 13,
              30,
              20,
              39, 3, 46, 8, 36, 17, 29, 24, 35, 2, 43, 7, 47, 14, 28, 9, 40, 21, 34, 18]
        for zw1 in range(ch[self.i], 49):  # 根据索引生成序列1
            zw.append(zw1)  # 添加到列表中
        for zw2 in range(1, ch[self.i]):  # 根据索引生成序列2
            zw.append(zw2)  # 添加到列表中
        return zw  # 返回值
    def export_cad(self):
        file=QFileDialog.getSaveFileName(self, '导出CAD坐标', '..', '文件(*.csv);;所有文件(*.*)')
        #保存坐标文件并输出
        if file[0] == '':  # 判断是否选择了文件
            return#退出函数
        data_list = []#创建一个空列表
        for row in range(self.table.rowCount()):#遍历表格的行
            row_data = []#创建一个空列表
            for col in range(self.table.columnCount()):#遍历表格的列
                item = self.table.item(row, col)#获取表格的单元格
                if item is not None:#判断单元格是否为空
                    row_data.append(item.text())#将单元格的数据添加到列表中
            data_list.append(row_data)#将列表添加到列表中
        df = pd.DataFrame(data_list)#将列表转换成DataFrame类型
        df.to_csv(file[0], index=False, header=False)#将数据保存到文件中
        QMessageBox.information(self, '提示', '导出成功')  # 弹出提示框
        #关闭窗口
        self.close()
