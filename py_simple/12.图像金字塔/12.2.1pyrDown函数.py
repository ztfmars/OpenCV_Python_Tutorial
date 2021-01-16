# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 11:30:20 2018


"""
import cv2
import numpy as np
o=cv2.imread(r"../image/lena.bmp",cv2.IMREAD_GRAYSCALE)
r=cv2.pyrDown(o)
cv2.imshow("original",o)
cv2.imshow("PyrDown",r)
cv2.waitKey()
cv2.destroyAllWindows()
