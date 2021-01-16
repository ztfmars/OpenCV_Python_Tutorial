# -*- coding: utf-8 -*-

import cv2
# 读取一张灰度图片
i=cv2.imread(r"../image/lena256.bmp", cv2.IMREAD_UNCHANGED)

#请确保当前目录下有灰度图像lena256.bmp
'''
print(i[100,100])
i[100,100]=255
print(i[100,100])
'''
print("img shape:", i.shape)
print("img array:", i)
p=i[100,100]
print("point P's value at (100,100):", p)
i[100,100]=255
p=i[100,100]
print("after P's  value has been changed:", p)