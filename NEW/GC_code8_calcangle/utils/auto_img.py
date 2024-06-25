import pyautogui
import time
from NEW.GC_code8_calcangle.utils.get_gc_api import *
from GC_code8_calcangle.utils.get_gc_api import get_gcapi_name, get_gcapi_part, get_gcapi_angle


def dg_auto_mun(bmp,name,part,ang,hwnd,t):
    pyautogui.PAUSE = t
    pyautogui.FAILSAFE = True
    x,y,width,height =  pyautogui.locateOnScreen(bmp,confidence=0.5)
   
##    print ("该图标在屏幕中的位置是：X={},Y={}，宽{}像素,高{}像素".format(x,y,width,height))

    
    pyautogui.doubleClick(x=x+80,y=y,button='left')
    
    
    get_gcapi_name(name,hwnd)
    get_gcapi_part(part,hwnd)
    get_gcapi_angle(ang,hwnd)

    
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('down')
    pyautogui.keyUp('down')
    pyautogui.keyUp('ctrl')
    time.sleep(t)



##dg_auto_mun('./img/name.png',1,"查看",0.1)
