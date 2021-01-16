# -*- coding: utf-8 -*-
"""
Created on Mon Jul  10 10:26:57 2018


"""
import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r'../image/girl.bmp')
b,g,r=cv2.split(img)
img2=cv2.merge([r,g,b])
plt.subplot(121)
plt.imshow(img),plt.axis('off')
plt.subplot(122)
plt.imshow(img2),plt.axis('off')
plt.show()
