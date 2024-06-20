import sys
import os
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.Qt import Qt

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

import configparser

import ui.gc_view_ui as gc_view_ui 
#截图
from utils.grab import grab_img
#roi
from utils.roi import roi_img
#计算角度dll
from utils.Call_CvTools_class import TemplateMatchingWrapper
#运行
from utils.auto_img import dg_auto_mun

class EmittingStr(QObject):
    textWritten = pyqtSignal(str)  # 定义一个发送str的信号

    def write(self, text):  # 发射结果
        self.textWritten.emit(str(text))

class UpdateImageThread(QThread):
    update_image_signal = pyqtSignal(QPixmap)

    def __init__(self, image_path, label):
        super().__init__()
        self.image_path = image_path
        self.label = label

    def run(self):
        while True:
            # 生成新的图片
            new_image = QPixmap(self.image_path)
            # 发送信号，将新图片传递给主线程
            self.update_image_signal.emit(new_image)
            # 等待一段时间
            time.sleep(0.05)  # 每隔1秒发送一次信号

class ImageThread(QThread):
    pixmap_signal = pyqtSignal(QPixmap)

    def __init__(self, image_path, label):
        super().__init__()
        self.image_path = image_path
        self.label = label

    def run(self):
        pixmap = QPixmap(self.image_path)
        self.pixmap_signal.emit(pixmap)

class Gc2000_angle(QMainWindow):
    def __init__(self):
        super(Gc2000_angle,self).__init__()
        self.ui= gc_view_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()
        self.info()

    def initUI(self):
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)  # 隐藏边框|置顶
        self.setWindowIcon(QIcon("./FA.ico"))  # 图标显示
        # sys.stdout = EmittingStr(textWritten=self.outputWritten)  # 输出重定向到textBrowser中
        # sys.stderr = EmittingStr(textWritten=self.outputWritten)
        self.ui.pushButton_testimg.clicked.connect(self.test_img)
        self.ui.pushButton_showimg.clicked.connect(self.show_img)
        self.ui.pushButton_roi.clicked.connect(self.rois_img)
        self.ui.pushButton_run.clicked.connect(self.run_calc)

    def read_ini(self,path):

        global _time
        global _hwndname
        global _position
        global  _nccdll
        global _resimg
        global _version
        """
            时间，句柄名，坐标范围，匹配参数，结果图像，版本
        """
        try:
            cfg = configparser.ConfigParser()
            cfg.read(path, encoding='utf-8')

            _time = eval(cfg.get('TIME', 'time'))
            _hwndname = eval(cfg.get('HWND', 'hwnd'))
            _position = eval(cfg.get('POSITION', 'position'))
            _nccdll = eval(cfg.get('NCCDLL', 'nccdll'))
            _resimg= eval(cfg.get('RESIMG', 'resimg'))
            _version = eval(cfg.get('VERSION', 'version'))
        except:
            text=("读取Config.ini文件异常！！！")
            print(str(text))
            self.outputWritten(text)
            time.sleep(5)
            sys.exit()


    def info(self):

        global _position
        global _hwndname
        global  _nccdll
        global _resimg

        self.ini_path=r'./Config.ini'
        self.read_ini(self.ini_path)
        self.hwndname=_hwndname
        self.position=_position
        self.src ,self.dst,self.minReduceArea,self.toleranceAngle,self.num,self.maxPos,self.score,self.maxOverlap=_nccdll 
        self.wrapper=TemplateMatchingWrapper()
        self.ressrc,self.resdst,self.resimg=_resimg
        
    def test_img(self):
        self.ui.imageLabel.clear()
        result = self.wrapper.call_template_matching(self.src, self.dst, self.minReduceArea, self.toleranceAngle, self.num, self.maxPos, self.score, self.maxOverlap)
        text=("识别角度：", result)
        self.outputWritten(text)
        self.outputlineEdit(result)
        self.thread = ImageThread(self.resimg, self.ui.imageLabel)
        self.thread.pixmap_signal.connect(self.ui.imageLabel.setPixmap)
        self.thread.start()

    def show_img(self):
        self.ui.imageLabel.clear()
        grab_img(self.position,self.ressrc,0.05)
        self.thread = ImageThread(self.ressrc, self.ui.imageLabel)
        self.thread.pixmap_signal.connect(self.ui.imageLabel.setPixmap)
        self.thread.start()

    def rois_img(self):
        roi_img(self.ressrc,self.resdst)

    def run_calc(self):
        nums=self.ui.lineEdit_num.text()
        name=self.ui.lineEdit_name.text()
        part=self.ui.lineEdit_part.text()
        if nums=="":
            self.outputWritten("请输入数量个数！！！")
        else:
            for num in range(int(nums)):
                self.ui.imageLabel.clear()
                grab_img(self.position,self.ressrc, 0.05)
                result = self.wrapper.call_template_matching(self.src, self.dst, self.minReduceArea, self.toleranceAngle, self.num, self.maxPos, self.score, self.maxOverlap)
                text=("识别角度：", result)
                self.outputWritten(text)
                self.outputlineEdit(result)
                # 创建自定义线程实例
                self.update_image_thread = UpdateImageThread(self.resimg,self.ui.imageLabel)
                # 连接信号和槽函数
                self.update_image_thread.update_image_signal.connect(self.ui.imageLabel.setPixmap)
                # 启动线程
                self.update_image_thread.start()

                dg_auto_mun('./img/name.png',str(name)+str(num+1),part,int(round(result)),self.hwndname,0.05)

                QtWidgets.QApplication.processEvents()
                
                if os.path.exists(self.src):
                    os.remove(self.src)
                    print("图片已删除")
                else:
                    print("图片不存在")

    def outputWritten(self, text):  # text显示方法text
        self.ui.label_res.setText(str(text))
        

    def outputlineEdit(self, text):  # text显示方法angle
        self.ui.lineEdit_angle.setText(str(round(text,2)))
           


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = Gc2000_angle()
    mainWin.show()
    sys.exit(app.exec_())
