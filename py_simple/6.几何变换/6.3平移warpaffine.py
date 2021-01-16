# -*- coding: utf-8 -*-
import cv2
import numpy as np

a=cv2.imread(r"../image/lenacolor.png")
height,width=a.shape[:2]
x=100
y=200
M = np.float32([[1, 0, x], [0, 1, y]])
b=cv2.warpAffine(a,M,(height,width))
cv2.imshow("original",a)
cv2.imshow("move",b)
cv2.waitKey()
cv2.destroyAllWindows()
