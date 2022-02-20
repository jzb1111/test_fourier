# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 16:00:43 2022

@author: asus
"""

import numpy as np
import quaternion
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

p_t=np.quaternion(0,0,0,-1)
v_t=np.quaternion(0,10,0,0)

for i in range(10):
    angle=np.pi/9*i
    h_t=np.quaternion(np.cos(angle/2),np.sin(angle/2)*v_t.x,np.sin(angle/2)*v_t.y,np.sin(angle/2)*v_t.z)
    h_t_=np.quaternion(np.cos(angle/2),-1*np.sin(angle/2)*v_t.x,-1*np.sin(angle/2)*v_t.y,-1*np.sin(angle/2)*v_t.z)
    p_new_t=h_t*p_t*h_t_
    print(angle,p_new_t)