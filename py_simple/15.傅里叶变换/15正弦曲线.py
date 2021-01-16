# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 07:38:43 2018


"""
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,2*np.pi*8,0.01)
y=np.sin(x)

plt.plot(x,y)
plt.xticks([0,10*np.pi,10*np.pi,10*np.pi],['0','1'])
plt.xlim(0,16*np.pi)
plt.show()