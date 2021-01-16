# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 07:38:43 2018


"""
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,2*np.pi*8,0.01)
y=3*np.sin(0.8*x)+7*np.sin(1/3*x)+2*np.sin(0.2*x)

y1=3*np.sin(0.8*x)
y2=7*np.sin(0.5*x)
y3=2*np.sin(0.2*x)

plt.subplot(221)
plt.plot(y)
plt.subplot(222)
plt.plot(y1)
plt.subplot(223)
plt.plot(y2)
plt.subplot(224)
plt.plot(y3)
plt.figure()
plt.plot(y)
plt.show()