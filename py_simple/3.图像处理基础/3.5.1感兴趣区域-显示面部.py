# -*- coding: utf-8 -*-


import cv2
import numpy as np
a=cv2.imread(r"../image/lenacolor.png",cv2.IMREAD_UNCHANGED)
face=np.ones((101,101,3))
cv2.imshow("original",a)
face=a[220:400,250:350]
cv2.imshow("face",face)
cv2.waitKey()
cv2.destroyAllWindows()
