# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 09:12:13 2018


"""
import cv2
o=cv2.imread(r"../image/girl.bmp")
down=cv2.pyrDown(o)
up=cv2.pyrUp(down)
cv2.imshow("original",o)
cv2.imshow("down",down)
cv2.imshow("up",up)
cv2.waitKey()
cv2.destroyAllWindows()