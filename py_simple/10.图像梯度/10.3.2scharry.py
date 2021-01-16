# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 13:55:27 2018


"""
import cv2
import numpy as np
o = cv2.imread(r'../image/scharr.bmp',cv2.IMREAD_GRAYSCALE)
scharry = cv2.Scharr(o,cv2.CV_64F,0,1)
scharry = cv2.convertScaleAbs(scharry)  # 转回uint8
cv2.imshow("original",o)
cv2.imshow("y",scharry)
cv2.waitKey()
cv2.destroyAllWindows()

