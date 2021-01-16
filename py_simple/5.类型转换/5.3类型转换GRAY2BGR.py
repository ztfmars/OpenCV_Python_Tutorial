# -*- coding: utf-8 -*-

import cv2
a=cv2.imread(r"../image/lena256.bmp",cv2.IMREAD_UNCHANGED)
b=cv2.cvtColor(a,cv2.COLOR_GRAY2BGR)
cv2.imshow("GRAY",a)
cv2.imshow("BGR",b)
cv2.waitKey()
cv2.destroyAllWindows()