import os

# 定义DLL文件的路径
dll_path = r'D:\Program Files\SMT\NEW\GC_code8_calcangle\utils\CvTools.dll'

# 检查DLL文件是否存在
if not os.path.exists(dll_path):
    print(f"{dll_path} 不存在。")
else:
    print(f"{dll_path} 存在。")

# 检查DLL文件是否在Python的搜索路径中
python_search_path = os.getcwd() + os.pathsep + os.environ["PATH"]
if dll_path not in python_search_path.split(os.pathsep):
    print(f"{dll_path} 不在Python的搜索路径中。")
else:
    print(f"{dll_path} 在Python的搜索路径中。")
print(os.environ["PATH"])

import ctypes

# 定义DLL文件的路径
dll_path = r'D:\Program Files\SMT\NEW\GC_code8_calcangle\utils\CvTools.dll'

# 加载DLL文件
try:
    dll = ctypes.cdll.LoadLibrary(dll_path)
    print(f"成功加载 {dll_path}")
except OSError as e:
    print(f"加载 {dll_path} 失败：{e}")