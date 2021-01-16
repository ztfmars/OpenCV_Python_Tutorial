# -*- coding: utf-8 -*-


import cv2
a=cv2.imread(r"../image/lena256.bmp",cv2.IMREAD_UNCHANGED)
b=cv2.cvtColor(a,cv2.COLOR_GRAY2BGR)
bb,bg,br=cv2.split(b)
cv2.imshow("bb",bb)
cv2.imshow("bg",bg)
cv2.imshow("br",br)
cv2.waitKey()
cv2.destroyAllWindows()