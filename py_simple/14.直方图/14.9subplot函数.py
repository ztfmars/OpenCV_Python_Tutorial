# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 20:41:08 2018


"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread(r'../image/equ.bmp',cv2.IMREAD_GRAYSCALE)
equ = cv2.equalizeHist(img)
plt.subplot(121),plt.hist(img.ravel(),256)
plt.subplot(122),plt.hist(equ.ravel(),256)

