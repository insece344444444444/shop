
import time
import mss
import cv2
import numpy as np

##import pyautogui
##
##while True:
##    input()
##    print(pyautogui.position())   # 得到当前鼠标位置；输出：Point(x=200, y=800)
        
def grab_img(pos,path_imgs,t):
    
    x,y,i=pos
    # 创建一个 mss 视频对象
    with mss.mss() as sct:
        # 设置截图区域
        monitor = {"top": y-i, "left":x-i, "width": i*2, "height": i*2}
        while True:
            # 截取屏幕
            img = sct.grab(monitor)
            # 将Image对象转换为numpy数组
            img_np = np.array(img)
##            cv2.imshow("IMG",img_np)
            # 保存图像
            cv2.imwrite(str(path_imgs), img_np)
            # 等待10毫秒
            time.sleep(t)
            break

##grab_img("./img/5.png",0.02)
