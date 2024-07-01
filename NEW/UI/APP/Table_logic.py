from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import pandas as pd
class Table_Logic(QWidget):
    def __init__(self):
        super().__init__()

    def openfile(self):
        file = QFileDialog.getOpenFileName(self, '导入CSV坐标', '..', '文件(*.csv);;所有文件(*.*)')
        # 获取文件路径
        if file[0] == '':
            return
        # 如果没有选择文件，返回
        data = pd.read_csv(file[0], header=None)
        # 读取文件
        data.fillna('', inplace=True)
        # 将空值替换为空字符串
        return data

    def exportfile(self,exportTable):
        file = QFileDialog.getSaveFileName(self, '导出CAD坐标', '..', '文件(*.csv);;所有文件(*.*)')
        # 获取文件路径
        if file[0] == '':
            return
        # 如果没有选择文件，返回
        df = pd.DataFrame(exportTable)  # 将列表转换成DataFrame类型
        df.to_csv(file[0], index=False, header=False)  # 将数据保存到文件中
        QMessageBox.information(self, '提示', '导出成功')
        self.close()

    def addTableData(self,table_data,table):
        table.clear()#清空表格
        num_rows = table_data.shape[0]#获取行数
        num_cols = table_data.shape[1]#获取列数
        table.setRowCount(num_rows)#设置行数
        table.setColumnCount(num_cols)#设置列数
        data_list = table_data.values.tolist()#将数据转换成列表
        for rowIndex, row in enumerate(data_list):
            for columnIndex, item in enumerate(row):
                table.setItem(rowIndex, columnIndex, QTableWidgetItem(str(item)))
        #遍历数据，添加到表格中
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        #设置表头自适应


    def updataTableData(self,table_data,table):
        table.clearContents()#清空表格内容
        for rowIndex, row in enumerate(table_data):
            for columnIndex, item in enumerate(row):
                table.setItem(rowIndex, columnIndex, QTableWidgetItem(str(item)))
        #遍历数据，添加到表格中

    def exportTableData(self,table):
        data_list = []#创建一个空列表
        for row in range(table.rowCount()):#遍历表格的行
            row_data = []#创建一个空列表
            for col in range(table.columnCount()):#遍历表格的列
                item = table.item(row, col)#获取表格的单元格
                if item is not None:#判断单元格是否为空
                    row_data.append(item.text())#将单元格的数据添加到列表中
            data_list.append(row_data)#将列表添加到列表中
        return data_list

    def highlightColumn(self,index,table):
        for i in range(table.rowCount()):#遍历表格的行
            item=table.item(i,index)#获取单元格
            if item:#判断单元格是否为空
                item.setBackground(Qt.red)#设置单元格背景颜色

    def clearColumnHighlight(self,table,selected_column):
        if selected_column is not None:#如果选中的列不为空
            for i in range(table.rowCount()):#遍历表格的行
                item=table.item(i,selected_column)#获取单元格
                if item:#判断单元格是否为空
                    item.setBackground(Qt.white)#设置单元格背景颜色

    def resetHeader(self,table):
        for i in range(table.columnCount()):#遍历表格的列
            item=QTableWidgetItem(f"{i+1}")#创建一个单元格
            table.setHorizontalHeaderItem(i,item)#设置表头

    def action_Trigger(self,tiggered,table,selected_column,context_menu):
        if selected_column is not None:#如果选中的列不为空
            new_header_item=QTableWidgetItem(tiggered.text())#创建一个单元格
            table.setHorizontalHeaderItem(selected_column,new_header_item)#设置表头
        if tiggered:#如果菜单项不为空
            tiggered.triggered.disconnect()#断开信号槽
            context_menu.removeAction(tiggered)#移除菜单项
    def contextmenu(self,context_menu,action,action_Trigger):
        #创建右键菜单
        action_item = context_menu.addAction(action)
        #添加菜单项
        action_item.triggered.connect(action_Trigger)

    def SetHeader(self,table,header_order,split_Part=False):
        header_texts = []#创建一个空列表
        columns_to_delete=[]#创建一个空列表
        for i in range(table.columnCount()):#遍历表格的列
            header_item=table.horizontalHeaderItem(i)#获取表头
            if header_item is not None and  header_item.text() in header_order:#判断表头是否为空
                header_texts.append(header_item.text())#将表头添加到列表中
            else:
                columns_to_delete.append(i)#将列索引添加到列表中
        if set(header_texts) == set(header_order):#判断表头是否相等
            for col_index in columns_to_delete:#遍历要删除的列
                table.removeColumn(col_index)#删除列
            new_header_indexes = [header_texts.index(header) for header in header_order]#获取新的表头索引
            new_columns_data=[]#创建一个空列表
            for new_index in new_header_indexes:#遍历新的表头索引
                column_data = [table.item(row,new_index).text() for row in range(table.rowCount())]#获取列数据
                new_columns_data.append(column_data)#将列数据添加到列表中

            table.clearContents()#清空表格内容
            table.setColumnCount(len(new_columns_data))#设置列数
            table.setHorizontalHeaderLabels(header_order)#设置表头
            for col,column_data in enumerate(new_columns_data):#遍历列数据
                for row,data in enumerate(column_data):#遍历行数据
                    item=QTableWidgetItem(data)#创建一个单元格
                    table.setItem(row,col,item)#设置单元格
            if split_Part:#如果分割零件
                split_Part.setEnabled(True)#设置可用
        elif set(header_texts).issubset(set(header_order)) and header_texts != []:#判断表头是否包含在表头栏中
            item=(set(header_order).difference(set(header_texts)))#获取差集
            QMessageBox.information(self,'提示',f'{item}表头栏未定义')
        else:
            QMessageBox.information(self, '提示', '"坐标未导入"或"表头栏未定义"\n                  请检查')

    def Check_repetition(self,datalist):
        item_count = {}#创建一个空字典
        duplicates = []#创建一个空列表
        for item in datalist:#遍历数据
            key = item[0]#获取数据的第一个元素
            if key in item_count:#判断数据是否在字典中
                item_count[key]['count']+= 1#计数加1
                item_count[key]['rows'].append(item)#将数据添加到列表中
            else:
                item_count[key]={'count':1,'rows':[item]}#创建一个新的字典
        for key,info in item_count.items():#遍历字典
            if info['count'] > 1:#判断计数是否大于1
                duplicates.append(key)#将数据添加到列表中
        return duplicates#返回重复的数据

    def highlight_row(self,row,table):
        for col in range(table.columnCount()):#遍历表格的列
            item=table.item(row,col)#获取单元格
            if item is not None:#判断单元格是否为空
                item.setBackground(QColor('yellow'))#设置单元格背景颜色
                item.setForeground(QColor('red'))#设置单元格前景颜色



