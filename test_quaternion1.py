# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 16:00:43 2022

@author: asus
"""

import numpy as np
import quaternion
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

threshold=0.1

def add_ax(ax,mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            for k in range(len(mat[i][j])):
                if mat[i][j][k]==1:
                    ax.scatter(i,j,k,c='r',marker='o')
                    
    return ax

ori_im=np.ones((100,100))

res=np.zeros((100,100,100))

fourier_map=np.zeros((100,100))

sphere=np.zeros((101,101,101))
center=[50,50,50]

spherelis=[]
for i in range(101):
    for j in range(101):
        for k in range(101):
            dist=((i-center[0])**2+(j-center[1])**2+(k-center[2])**2)**0.5
            
            if abs(dist-50)<=0.01:
                #print(i,j,k)
                sphere[i][j][k]=1
                spherelis.append([(i-50)/(101/2),(j-50)/(101/2),(k-50)/(101/2)])
fig=plt.figure(0)
ax=fig.add_subplot(111,projection='3d')

ax=add_ax(ax,sphere)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
 
plt.show()

sphere_q_lis=[]
for i in range(1):
    for j in range(51):
        for k in range(51):
            for l in range(51):
                #for o in range(len(spherelis)):
                q=np.quaternion(i/51,(j-25)/51,(k-25)/51,(l-25)/51)
                res=np.exp(2*np.pi*1*q)
                x=res.x
                y=res.y
                z=res.z
                
                #label=spherelis[o]
                dist=((x*101+50-center[0])**2+(y*101+50-center[1])**2+(z*101+50-center[2])**2)**0.5
                if abs(dist-50)<=threshold:
                    print(res)
                    sphere_q_lis.append([q,res])
                    
qsphere=np.zeros((101,101,101))
for i in range(len(sphere_q_lis)):
    q=sphere_q_lis[i][1]
    x=q.x
    y=q.y
    z=q.z
    qsphere[int(x*101+50)][int(y*101+50)][int(z*101+50)]=1
    
fig=plt.figure(1)
ax=fig.add_subplot(111,projection='3d')

ax=add_ax(ax,qsphere)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
 
plt.show()

qsphere_q=np.zeros((101,101,101))
for i in range(len(sphere_q_lis)):
    q=sphere_q_lis[i][0]
    x=q.x
    y=q.y
    z=q.z
    qsphere_q[int(x*101+50)][int(y*101+50)][int(z*101+50)]=1
    
fig=plt.figure(2)
ax=fig.add_subplot(111,projection='3d')

ax=add_ax(ax,qsphere_q)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()