from PySide6.QtWidgets import *
import sys
from NEW.UI.UIC.LOGIN import Ui_Form as Main_Ui
from qt_material import apply_stylesheet
from NEW.UI.APP.Led_Run import LedWindow
from NEW.UI.APP.Cad_Bom_Run import CadWindow

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

        self.LED.clicked.connect(self.bind_led)
        self.BOM.clicked.connect(self.bind2_cadbom)

    def bind_led(self):
        self.subwindow_Led=LedWindow()
        self.subwindow_Led.show()
        self.subwindow_Led.closeEvent = lambda event: self.show()
        self.closeEvent_L = lambda event: self.subwindow_Led.close()
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