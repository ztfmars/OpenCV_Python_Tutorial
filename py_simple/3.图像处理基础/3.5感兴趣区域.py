# -*- coding: utf-8 -*-
"""
Created on Wed May  9 07:47:01 2018


"""
import cv2
import numpy as np
lena=cv2.imread(r"../image/lenacolor.png")
girl=cv2.imread(r"../image/girl.bmp")

b=np.ones((180,100,3))
b=lena[220:400,250:350]
girl[190:370,230:330]=b
cv2.imshow("original",girl)

cv2.waitKey()
cv2.destroyAllWindows()

