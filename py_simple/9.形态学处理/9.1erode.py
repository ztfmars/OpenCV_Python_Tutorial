# -*- coding: utf-8 -*-

import cv2
import numpy as np
o=cv2.imread("image\\erode.bmp",cv2.IMREAD_UNCHANGED)
k=np.ones((5,5),np.uint8)
r=cv2.erode(o,k,iterations=10)
cv2.imshow("original",o)
cv2.imshow("result",r)
cv2.waitKey()
cv2.destroyAllWindows()
