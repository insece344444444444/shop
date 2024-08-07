"""
图像踩点和校准流程
    ├── 1. 图像读取和预处理
    │   ├── 使用OpenCV读取图像
    │   ├── 将图像转换为灰度图
    │   └── 二值化处理图像
    ├── 2. 检测标记点
    │   ├── 形态学操作去除噪声
    │   ├── 使用边缘检测找到边缘
    │   └── 使用轮廓检测找到标记点
    ├── 3. 标记点的匹配和校准
    │   ├── 确定标记点的实际坐标
    │   ├── 找到图像中的标记点位置
    │   ├── 计算单应性变换矩阵
    │   └── 应用转换矩阵进行图像校准
    └── 4. 绘制和验证
        ├── 在校准后的图像上绘制标记点
        ├── 对比实际位置和校准后的位置
        └── 进行进一步处理和标注
"""