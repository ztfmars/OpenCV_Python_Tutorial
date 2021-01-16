# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 13:55:27 2018


"""
import cv2
import numpy as np
o = cv2.imread(r'../image/scharr.bmp',cv2.IMREAD_GRAYSCALE)
scharrx = cv2.Scharr(o,cv2.CV_64F,1,0)
scharrx = cv2.convertScaleAbs(scharrx)   # 转回uint8 
cv2.imshow("original",o)
cv2.imshow("x",scharrx)
cv2.waitKey()
cv2.destroyAllWindows()

