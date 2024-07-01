from PySide6.QtWidgets import *
from PySide6.QtCore import *
from NEW.UI.UIC.Import_Cad import Ui_Cad_Data as Sub_Ui
from PySide6.QtGui import *
from NEW.UI.APP.Table_logic import Table_Logic as tb
from NEW.UI.UIC.CAD_BOM import Ui_MainWindow as Cad
class CadWindow(QMainWindow,Cad):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

        self.import_CAD.triggered.connect(self.bind_importcad)

    def initUI(self):
        self.table_cadbom.setColumnCount(11)#设置表格列数
        headers=['序号','位号','X坐标','Y坐标','R角度','元件号码','物料描述','T/B','拼板','数据号','错误异常']#表头
        self.TB_combobox.addItems(['All','Top','Bot'])#添加下拉框选项

        self.table_cadbom.setHorizontalHeaderLabels(headers)#设置表头
        self.table_cadbom.verticalHeader().setVisible(False)
        self.table_cadbom.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)#设置表头自适应
        self.table_cadbom.horizontalHeader().setSectionResizeMode(0,QHeaderView.Fixed)#设置第一列固定大小
        self.table_cadbom.setColumnWidth(0,30)#设置第一列大小
        for col in range(1,6):#设置第2-6列固定大小
            self.table_cadbom.horizontalHeader().setSectionResizeMode(col,QHeaderView.Fixed)#设置列固定大小
            self.table_cadbom.setColumnWidth(col,90)#设置列大小
        for row in range(self.table_cadbom.rowCount()):#遍历表格的行
            for col in range(self.table_cadbom.columnCount()):#遍历表格的列
                if col == 0:#如果是第一列
                    item=QTableWidgetItem(f"Row {row+1}")#创建一个单元格
                else:
                    item=QTableWidgetItem(f"Item {row+1}-{col+1}")#创建一个单元格
                self.table_cadbom.setItem(row,col,item)#设置单元格

        self.button_group = QButtonGroup(self)#创建按钮组
        self.button_group.setExclusive(True)#设置互斥

        self.buttons = [
            self.Place_Data,
            self.Pcbsize_Data,
            self.Part_Data,
            self.PartTable_Data
        ]#按钮列表
        for button in self.buttons:#遍历按钮
            button.setCheckable(True)#设置可选中
            button.setStyleSheet(self.default_style())#设置样式
            button.clicked.connect(self.update_button_styles)#绑定信号槽
            button.enterEvent = lambda event,b=button:self.on_hover_enter(b)#绑定鼠标进入事件
            button.leaveEvent = lambda event,b=button:self.on_hover_leave(b)#绑定鼠标离开事件
            self.button_group.addButton(button)#添加按钮到按钮组
            self.buttons[0].setChecked(True)#设置第一个按钮选中
        self.update_button_styles()#更新按钮样式

    def update_button_styles(self):
        for button in self.buttons:#遍历按钮
            if button.isChecked():#如果按钮被选中
                button.setStyleSheet(self.checked_style())#设置选中样式
            else:
                button.setStyleSheet(self.default_style())#设置默认样式
    def on_hover_enter(self,button):
        if not button.isChecked():#如果按钮没有被选中
            button.setStyleSheet(self.hover_style())#设置悬停样式
    def on_hover_leave(self,button):
        if not button.isChecked():#如果按钮没有被选中
            button.setStyleSheet(self.default_style())#设置默认样式

    def default_style(self):
        return """
        QPushButton {
            background-color: none;
            border: 1px solid#cccccc;
            }
            """#默认样式

    def checked_style(self):
        return """
        QPushButton {
            background-color:#FF69B4;
            border: 1px solid#cccccc;
            }
            """#选中样式

    def hover_style(self):
        return """
        QPushButton {
            background-color:#FFC0CB;
            border: 1px solid#cccccc;
            }
            """#悬停样式

    def bind_importcad(self):
        self.subwindow_importcad=ImportCadWindow(self)#创建子窗口
        self.subwindow_importcad.show()#显示子窗口
        self.subwindow_importcad.closeEvent = lambda event:self.show()#子窗口关闭时显示主窗口
        self.closeEvent_i=lambda  event: self.subwindow_importcad.close()#主窗口关闭时关闭子窗口
        self.hide()#隐藏主窗口

    def displayMergedData(self,data_dict):
        #设置表格的行，原表格的表头和列数不动
        self.table_cadbom.setRowCount(max([len(data) for data in data_dict.values()]))
        #IF判断只有键一样的才能根据键添加列数据，键不存在时添加空列
        for col, header in enumerate(self.table_cadbom.horizontalHeaderItem(i).text() for i in range(self.table_cadbom.columnCount())):
            if header in data_dict:
                for row, item in enumerate(data_dict[header]):
                    self.table_cadbom.setItem(row, col, QTableWidgetItem(item))

        #显示表格
        self.subwindow_importcad.hide()
        self.show()

class ImportCadWindow(Sub_Ui,tb):
    mergeCompleted = Signal(dict)
    def __init__(self,parent=None):
        super().__init__()
        self.parent=parent
        self.setupUi(self)
        self.CadWindow = CadWindow()
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

        self.selected_column = None#当前选中的列

        self.resetHeaders()#重置表头
        self.table_importcad.verticalHeader().setVisible(False)
        self.OpenFile_BTN.clicked.connect(self.open)#绑定打开文件按钮
        self.table_importcad.horizontalHeader().setContextMenuPolicy(Qt.CustomContextMenu)#设置表头的右键菜单,作用是在表头右键点击时触发信号
        self.table_importcad.horizontalHeader().setContextMenuPolicy(Qt.DefaultContextMenu)#设置默认的右键菜单
        self.table_importcad.horizontalHeader().sectionClicked.connect(self.showContextMenu)#绑定表头右键菜单
        self.SetHeader_BTN.clicked.connect(self.ImportCad_SetHeader_Run)#绑定设置表头按钮
        self.Check_repetition_BTN.clicked.connect(self.Check_repetition_Run)#绑定检查重复按钮
        self.Export_BTN.clicked.connect(self.ExportData)#绑定导出按钮
        self.mergeCompleted.connect(self.parent.displayMergedData)#绑定合并完成信号

    def open(self):
        data=self.openfile()#打开文件
        self.addTableData(data,self.table_importcad)#添加数据到表格
        self.resetHeaders()#重置表头
        self.repetition_label.setText("")#清空重复标签

    def showContextMenu(self, index):
        if not hasattr(self, 'context_menu'):#如果没有右键菜单
            self.context()#创建右键菜单
        if index != self.selected_column:#如果点击的列不是当前选中的列
            self.clearColumnHighlight(self.table_importcad, self.selected_column)#清除当前选中列的高亮
            self.selected_column = index#设置当前选中的列
            self.highlightColumn(index, self.table_importcad)#高亮当前选中的列
        cursor_position = QCursor.pos()  # 获取当前鼠标的位置
        self.context_menu.exec(cursor_position)#在鼠标位置显示菜单

    def context(self):
        #创建右键菜单
        self.context_menu = QMenu(self)
        #添加菜单项
        self.action_Ref = self.context_menu.addAction('位号')
        self.action_X = self.context_menu.addAction('X坐标')
        self.action_Y = self.context_menu.addAction('Y坐标')
        self.action_R = self.context_menu.addAction('R角度')
        self.action_TB = self.context_menu.addAction('T/B')
        self.action_Reset = self.context_menu.addAction('Reset')
        #绑定菜单项
        self.action_Ref.triggered.connect(lambda: self.action_Trigger(self.action_Ref,self.table_importcad,self.selected_column,self.context_menu))
        self.action_X.triggered.connect(lambda: self.action_Trigger(self.action_X,self.table_importcad,self.selected_column,self.context_menu))
        self.action_Y.triggered.connect(lambda: self.action_Trigger(self.action_Y,self.table_importcad,self.selected_column,self.context_menu))
        self.action_R.triggered.connect(lambda: self.action_Trigger(self.action_R,self.table_importcad,self.selected_column,self.context_menu))
        self.action_TB.triggered.connect(lambda: self.action_Trigger(self.action_TB,self.table_importcad,self.selected_column,self.context_menu))
        self.action_Reset.triggered.connect(self.resetHeaders)

    def resetHeaders(self):
        self.resetHeader(self.table_importcad)#重置表头
        #在表格前面插入一列
        self.table_importcad.insertColumn(0)
        self.table_importcad.setHorizontalHeaderItem(0, QTableWidgetItem('序号'))#设置表头
        self.table_importcad.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.table_importcad.setColumnWidth(0, 30)  # 设置第一列大小
        self.context()#创建右键菜单

    def ImportCad_SetHeader_Run(self):
        self.ImportCad_header_order=['序号','位号', 'X坐标', 'Y坐标', 'R角度','T/B']#设置表头
        #填充序号的列数据，生成Range
        for row in range(self.table_importcad.rowCount()):
            item = QTableWidgetItem(str(row + 1))
            self.table_importcad.setItem(row, 0, item)
        self.SetHeader(self.table_importcad, self.ImportCad_header_order)#设置表头

    def Check_repetition_Run(self):
        datalist = self.exportTableData(self.table_importcad)#导出表格数据
        test=self.Check_repetition(datalist)#检查重复
        for i in test:#遍历重复的数据
            result=self.table_importcad.findItems(i,Qt.MatchContains)#查找重复的数据
            for item in result:#遍历重复的数据
                row=item.row()#获取行
                self.highlight_row(row,self.table_importcad)#高亮行
            self.repetition_label.setText(f"坐标数据中发现：{i}....等位号重复")#设置重复标签

    def ExportData(self):
        lebel_text=self.repetition_label.text()#获取重复标签的文本
        header_data=[self.table_importcad.horizontalHeaderItem(i).text() for i in range(self.table_importcad.columnCount())]
        #判断表头是否定义完全
        if lebel_text == "":
            #生产表头为键，列数据为值的字典
            data_dict={header: [self.table_importcad.item(row, col).text() for row in range(self.table_importcad.rowCount())] for col, header in enumerate(header_data)}
            self.mergeCompleted.emit(data_dict)
        else:
            QMessageBox.information(self,'提示','请检查位号是否有重复')#弹出提示框