# -*- coding: utf-8 -*-

import cv2
import numpy as np
a=cv2.imread(r"../image/lenacolor.png")
b=cv2.resize(a,None,fx=1.2,fy=0.5)
cv2.imshow("original",a)
cv2.imshow("resize",b)
cv2.waitKey()
cv2.destroyAllWindows()
