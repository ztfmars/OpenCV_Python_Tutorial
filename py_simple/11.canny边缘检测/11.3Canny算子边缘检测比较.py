# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 14:15:23 2018

sobel算子与scharr算子的比较

"""
import cv2
import numpy as np
o=cv2.imread(r"../image/lena.bmp",cv2.IMREAD_GRAYSCALE)
r1=cv2.Canny(o,100,200)
r2=cv2.Canny(o,64,128)
cv2.imshow("original",o)
cv2.imshow("result1",r1)
cv2.imshow("result2",r2)
cv2.waitKey()
cv2.destroyAllWindows()
