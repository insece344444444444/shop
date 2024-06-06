from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import pandas as pd
class Table_Logic(QWidget):
    def __init__(self):
        super().__init__()

    def openfile(self):
        file = QFileDialog.getOpenFileName(self, '导入CSV坐标', '..', '文件(*.csv);;所有文件(*.*)')
        if file[0] == '':
            return
        data = pd.read_csv(file[0], header=None)
        data.fillna('', inplace=True)
        return data

    def exportfile(self,exportTable):
        file = QFileDialog.getSaveFileName(self, '导出CAD坐标', '..', '文件(*.csv);;所有文件(*.*)')
        if file[0] == '':
            return
        df = pd.DataFrame(exportTable)  # 将列表转换成DataFrame类型
        df.to_csv(file[0], index=False, header=False)  # 将数据保存到文件中
        QMessageBox.information(self, '提示', '导出成功')
        self.close()

    def addTableData(self,table_data,table):
        table.clear()
        num_rows = table_data.shape[0]
        num_cols = table_data.shape[1]
        table.setRowCount(num_rows)
        table.setColumnCount(num_cols)
        data_list = table_data.values.tolist()
        for rowIndex, row in enumerate(data_list):
            for columnIndex, item in enumerate(row):
                table.setItem(rowIndex, columnIndex, QTableWidgetItem(str(item)))
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)


    def updataTableData(self,table_data,table):
        table.clearContents()
        for rowIndex, row in enumerate(table_data):
            for columnIndex, item in enumerate(row):
                table.setItem(rowIndex, columnIndex, QTableWidgetItem(str(item)))

    def exportTableData(self,table):
        data_list = []
        for row in range(table.rowCount()):#遍历表格的行
            row_data = []#创建一个空列表
            for col in range(table.columnCount()):#遍历表格的列
                item = table.item(row, col)#获取表格的单元格
                if item is not None:#判断单元格是否为空
                    row_data.append(item.text())#将单元格的数据添加到列表中
            data_list.append(row_data)#将列表添加到列表中
        return data_list

    def highlightColumn(self,index,table):
        for i in range(table.rowCount()):
            item=table.item(i,index)
            if item:
                item.setBackground(Qt.red)

    def clearColumnHighlight(self,table,selected_column):
        if selected_column is not None:
            for i in range(table.rowCount()):
                item=table.item(i,selected_column)
                if item:
                    item.setBackground(Qt.white)

    def resetHeader(self,table):
        for i in range(table.columnCount()):
            item=QTableWidgetItem(f"{i+1}")
            table.setHorizontalHeaderItem(i,item)

    def action_Trigger(self,tiggered,table,selected_column,context_menu):
        if selected_column is not None:
            new_header_item=QTableWidgetItem(tiggered.text())
            table.setHorizontalHeaderItem(selected_column,new_header_item)
        if tiggered:
            tiggered.triggered.disconnect()
            context_menu.removeAction(tiggered)
    def contextmenu(self,context_menu,action,action_Trigger):
        action_item = context_menu.addAction(action)
        action_item.triggered.connect(action_Trigger)

    def SetHeader(self,table,header_order,split_Part=False):
        header_texts = []
        columns_to_delete=[]
        for i in range(table.columnCount()):
            header_item=table.horizontalHeaderItem(i)
            if header_item is not None and  header_item.text() in header_order:
                header_texts.append(header_item.text())
            else:
                columns_to_delete.append(i)
        if set(header_texts) == set(header_order):
            for col_index in columns_to_delete:
                table.removeColumn(col_index)
            new_header_indexes = [header_texts.index(header) for header in header_order]
            new_columns_data=[]
            for new_index in new_header_indexes:
                column_data = [table.item(row,new_index).text() for row in range(table.rowCount())]
                new_columns_data.append(column_data)

            table.clearContents()
            table.setColumnCount(len(new_columns_data))
            table.setHorizontalHeaderLabels(header_order)
            for col,column_data in enumerate(new_columns_data):
                for row,data in enumerate(column_data):
                    item=QTableWidgetItem(data)
                    table.setItem(row,col,item)
            if split_Part:
                split_Part.setEnabled(True)
        elif set(header_texts).issubset(set(header_order)) and header_texts != []:
            item=(set(header_order).difference(set(header_texts)))
            QMessageBox.information(self,'提示',f'{item}表头栏未定义')
        else:
            QMessageBox.information(self, '提示', '"坐标未导入"或"表头栏未定义"\n                  请检查')

    def Check_repetition(self,datalist):
        item_count = {}
        duplicates = []
        for item in datalist:
            key = item[0]
            if key in item_count:
                item_count[key]['count']+= 1
                item_count[key]['rows'].append(item)
            else:
                item_count[key]={'count':1,'rows':[item]}
        for key,info in item_count.items():
            if info['count'] > 1:
                duplicates.append(key)
        return duplicates

    def highlight_row(self,row,table):
        for col in range(table.columnCount()):
            item=table.item(row,col)
            if item is not None:
                item.setBackground(Qt.GlobalColor.red)




