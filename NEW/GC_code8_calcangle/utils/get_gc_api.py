import win32gui

titles = set()
def foo(hwnd, mouse):
    # 去掉下面这句就所有都输出了，但是我不需要那么多
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        titles.add(win32gui.GetWindowText(hwnd))
  
#parent为父窗口句柄id
def get_child_windows(parent):
    '''
    获得parent的所有子窗口句柄
     返回子窗口句柄列表
     '''
    if not parent:
        return
    hwndChildList = []
    win32gui.EnumChildWindows(parent, lambda hwnd, param: param.append(hwnd),  hwndChildList)
    return hwndChildList

def get_hwnd_api(name,scops,off):
    
    win32gui.EnumWindows(foo, 0)
    for ts in [t for t in titles if t]:
        try:
            if str(ts[0:scops]).strip()==str(name).strip():
                # print("找到句柄")
                hwnd = win32gui.FindWindow(None,str(ts))
                _li=get_child_windows(hwnd)
                _num = win32gui.GetWindowText(_li[52])
                _num=eval(_num)
                if off==1:
##                    print("User mm:{},{}".format(_num[0],_num[1]))
                    pass
                return _num      
        except:                
            pass

##if __name__ == '__main__':
##    get_hwnd_api("GC-PowerStation",16,1)


import win32gui
import win32api
import win32con

def enum_child_windows(hwnd, lParam):
    """
    EnumChildWindows回调函数，用于获取子窗口句柄
    """
    child_windows = lParam
    child_windows.append(hwnd)
    return True

def get_edit_control(hwnd):
    """
    获取编辑框句柄
    """
    child_windows = []
    li = []
    win32gui.EnumChildWindows(hwnd, enum_child_windows, child_windows)
    for child in child_windows:
        class_name = win32gui.GetClassName(child)
        if class_name == "Edit":
            li.append(child)
    return li

def set_edit_text(hwnd, text):
    """
    设置编辑框文本
    """
    win32api.SendMessage(hwnd, win32con.WM_SETTEXT, 0, text)

def get_gcapi_name(c,name):

        # 获取窗口句柄
        hwnd = win32gui.FindWindow(None, name[0])
        print(hwnd)
        if hwnd != 0:

            # 获取编辑框句柄
            edit_hwnd = get_edit_control(hwnd)
            set_edit_text(edit_hwnd[1], str(c))
            ##    1元件位号，4角度，6PN
##            set_edit_text(edit_hwnd[1], str("R1"))
##            set_edit_text(edit_hwnd[4], str("90"))
##            set_edit_text(edit_hwnd[6], str("3216R"))
            
##            set_edit_text(edit_hwnd[1], str(r)) 
##            set_edit_text(edit_hwnd[4], str(a))

def get_gcapi_part(c,name):

        # 获取窗口句柄
        hwnd = win32gui.FindWindow(None, name[0])
        print(hwnd)
        if hwnd != 0:

            # 获取编辑框句柄
            edit_hwnd = get_edit_control(hwnd)
            set_edit_text(edit_hwnd[6], str(c))

def get_gcapi_angle(c,name):

        # 获取窗口句柄
        hwnd = win32gui.FindWindow(None, name[0])
        print(hwnd)
        if hwnd != 0:

            # 获取编辑框句柄
            edit_hwnd = get_edit_control(hwnd)
            set_edit_text(edit_hwnd[4], str(c))
##
##get_gcapi("1206")
##
##
