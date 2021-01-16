# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 15:14:29 2018


"""

import cv2
import matplotlib.pyplot as plt
o=cv2.imread(r"../image/boatGray.bmp")
histb = cv2.calcHist([o],[0],None,[256],[0,255])
plt.plot(histb,color='r')
plt.show()