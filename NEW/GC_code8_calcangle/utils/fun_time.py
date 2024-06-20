import time

def fun_time(func):
    
    def fun(*arge,**kwarge):
        _start=time.time()
        print("运行开始")
        func(*arge,**kwarge)
        _end=time.time()
        t=_start-_end
        print('运行时间：',t)
        print('<<<欢迎您使用DGS-TOOL软件,开发不易,开发作者:LFW>>>')
        
    return fun


