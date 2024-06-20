import ctypes
from ctypes import *
import os
import time

class TemplateMatchingWrapper:
    def __init__(self, dll_path="CvTools.dll"):
        self.dll_path = dll_path
        self.dll_paths = os.path.join(os.path.dirname(__file__), self.dll_path)
        self.template_matching_dll = CDLL(self.dll_paths, winmode=0)

        # 定义函数原型
        self.TemplateMatching = self.template_matching_dll.TemplateMatching
        self.TemplateMatching.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_double, ctypes.c_int, ctypes.c_int, ctypes.c_double, ctypes.c_double]
        self.TemplateMatching.restype = ctypes.c_double

    def call_template_matching(self, src, dst, minReduceArea, toleranceAngle, num, maxPos, score, maxOverlap):
        result = self.TemplateMatching(src, dst, minReduceArea, toleranceAngle, num, maxPos, score, maxOverlap)
        return result

# if __name__ == "__main__":
#     wrapper = TemplateMatchingWrapper()
#     src = b"./img/5.png"
#     dst = b"./img/6.png"
#     minReduceArea = 256
#     toleranceAngle = 180
#     num = 3
#     maxPos = 10
#     score = 0.9
#     maxOverlap = 0.5
#     result = wrapper.call_template_matching(src, dst, minReduceArea, toleranceAngle, num, maxPos, score, maxOverlap)
#     print("识别角度：", result)
    # time.sleep(1)
