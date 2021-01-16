# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 13:55:27 2018


"""
import cv2
import numpy as np
o = cv2.imread(r'../image/sobel4.bmp',cv2.IMREAD_GRAYSCALE)
sobelx = cv2.Sobel(o,cv2.CV_64F,1,0,ksize=3)
sobely = cv2.Sobel(o,cv2.CV_64F,0,1,ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)   # 转回uint8  
sobely = cv2.convertScaleAbs(sobely)  
sobelxy =  cv2.addWeighted(sobelx,0.5,sobely,0.5,0)  
sobelxy11=cv2.Sobel(o,cv2.CV_64F,1,1,ksize=3)
cv2.imshow("original",o)
cv2.imshow("x",sobelx)
cv2.imshow("y",sobely)
cv2.imshow("xy",sobelxy)
cv2.imshow("xy11",sobelxy11)
cv2.waitKey()
cv2.destroyAllWindows()

