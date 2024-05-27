from PySide6.QtWidgets import *
import sys
from NEW.UI.UIC.LOGIN import Ui_Form as Main_Ui
from qt_material import apply_stylesheet
from  NEW.UI.APP.Led_Run import LedWindow
class MyWindow(QWidget,Main_Ui):
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

        self.LED.clicked.connect(self.bind)

    def bind(self):
        self.subwindow=LedWindow()
        self.subwindow.show()
        self.subwindow.closeEvent = lambda event: self.show()
        self.closeEvent = lambda event: self.subwindow.close()
        self.hide()  # 隐藏主窗口

if __name__ == "__main__":
    app=QApplication(sys.argv)
    apply_stylesheet(app, theme='light_pink.xml')
    win=MyWindow()
    win.show()
    sys.exit(app.exec())