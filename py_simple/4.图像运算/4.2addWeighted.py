 # -*- coding: utf-8 -*-
import cv2
a=cv2.imread(r"../image/add/boat.bmp")
b=cv2.imread(r"../image/add/lena.bmp")
result=cv2.addWeighted(a,1,b,1,0)
cv2.imshow("boat",a)
cv2.imshow("lena",b)
cv2.imshow("result",result)
cv2.waitKey()
cv2.destroyAllWindows()
