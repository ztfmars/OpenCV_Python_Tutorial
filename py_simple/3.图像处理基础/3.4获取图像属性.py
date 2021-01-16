# -*- coding: utf-8 -*-

import cv2
a=cv2.imread(r"../image/lena256.bmp",cv2.IMREAD_UNCHANGED)
b=cv2.imread(r"../image/lenacolor.png",cv2.IMREAD_UNCHANGED)
print(a.shape)
print(b.shape)
print(a.size)
print(b.size)
print(a.dtype)
print(b.dtype)

