from PySide6.QtWidgets import *
import sys
from NEW.UI.UIC.LOGIN import Ui_Form as Main_Ui
from qt_material import apply_stylesheet
from NEW.UI.APP.Led_Run import LedWindow
from NEW.UI.APP.Cad_Bom_Run import CadWindow


class MyWindow(QWidget,Main_Ui):
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

        self.LED.clicked.connect(self.bind_led)#绑定信号槽
        self.BOM.clicked.connect(self.bind2_cadbom)#绑定信号槽

    def bind_led(self):
        self.subwindow_Led=LedWindow()#创建子窗口
        self.subwindow_Led.show()#显示子窗口
        self.subwindow_Led.closeEvent = lambda event: self.show()#子窗口关闭时显示主窗口
        self.closeEvent_L = lambda event: self.subwindow_Led.close()#主窗口关闭时关闭子窗口
        self.hide()  # 隐藏主窗口

    def bind2_cadbom(self):
        self.subwindow_Cad=CadWindow()
        self.subwindow_Cad.show()
        self.subwindow_Cad.closeEvent = lambda event:self.show()
        self.closeEvent_C = lambda  event: self.subwindow_Cad.close()
        self.hide()
if __name__ == "__main__":
    app=QApplication(sys.argv)
    #apply_stylesheet(app, theme='light_pink.xml')
    win=MyWindow()
    win.show()
    sys.exit(app.exec())