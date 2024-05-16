from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QPushButton, \
    QMessageBox, QWidget, QVBoxLayout, QLabel ,QHBoxLayout
from qt_material import apply_stylesheet
from CAD_BOM import CadWindow
from LED import LedWindow
from PySide6.QtGui import QPixmap
import sys
class Mywindow(QWidget):#创建一个类，继承QMainWindow类
    def __init__(self):#初始化
        super().__init__()#调用父类的初始化方法
        self.resize(200,320)#设置窗口大小
        self.setWindowTitle('SMT')#设置窗口标题
        self.setWindowIcon(QPixmap(':/icon/Lance.png'))#设置窗口图标
        self.lb=QLabel('新厚泰BOM工具',self)#创建一个标签
        self.lb.setAlignment(Qt.AlignmentFlag.AlignCenter)#设置标签的对齐方式
        #设置按钮的默认背景颜色和鼠标悬停时按钮的背景颜色
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
        self.btn1=QPushButton('LED站位插花',self)#创建一个按钮
        self.btn2=QPushButton('CAD_BOM合并',self)#创建一个按钮
        self.btn1.clicked.connect(self.bind)#为按钮绑定事件
        self.btn2.clicked.connect(self.bind1)#为按钮绑定事件
        self.mainLayout=QVBoxLayout()#创建一个垂直布局
        self.QHBoxLayout=QHBoxLayout()#创建一个水平布局
        self.mainLayout.addWidget(self.lb)#将标签添加到布局中
        self.mainLayout.addWidget(self.btn1)#将按钮添加到布局中
        self.mainLayout.addWidget(self.btn2)#将按钮添加到布局中
        self.QHBoxLayout.addLayout(self.mainLayout)
        self.setLayout(self.QHBoxLayout)#设置布局
        # 将按钮添加到布局或窗口中
    def bind(self):
        self.subwindow = LedWindow()  # 创建一个次级窗口
        self.subwindow.show()  # 显示次级窗口
        #子窗口打开时主窗口隐藏
        self.subwindow.closeEvent = lambda event: self.show()
        # 主窗口关闭时子窗口也关闭
        self.closeEvent = lambda event: self.subwindow.close()
        self.hide()  # 隐藏主窗口
    def bind1(self):
        self.subwindow = CadWindow()  # 创建一个次级窗口
        self.subwindow.show()  # 显示次级窗口
        #子窗口打开时主窗口隐藏
        self.subwindow.closeEvent = lambda event: self.show()
        # 主窗口关闭时子窗口也关闭
        self.closeEvent = lambda event: self.subwindow.close()
        self.hide()  # 隐藏主窗口

if __name__ == '__main__':
    app = QApplication(sys.argv)#创建一个应用
    apply_stylesheet(app, theme='light_pink.xml')  # 设置主题
    window = Mywindow()#创建一个窗口
    window.show()#显示窗口
    app.exec_()#应用循环
