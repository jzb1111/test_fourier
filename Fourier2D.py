# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 14:37:56 2022

@author: asus
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def add_ax(ax,mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            for k in range(len(mat[i][j])):
                if mat[i][j][k]==1:
                    ax.scatter(i,j,k,c='r',marker='o')
                    
    return ax


a=np.zeros((100,100,100))

a[:,:,50]=1

#for each voxel:real+i_img+j_img

fig=plt.figure(0)
ax=fig.add_subplot(111,projection='3d')

ax=add_ax(ax,a)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
 
plt.show()

