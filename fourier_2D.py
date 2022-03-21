 # -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 16:28:39 2022

@author: asus
"""

import numpy as np
import quaternion
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from Intersection import intersection

plane_size=[101,101]
plane=np.ones((101,101))
for i in range(101):
    for j in range(101):
        #plane[i][j]=j
        if ((i-50)**2+(j-50)**2)**0.5<10:
            plane[i][j]=1.5
center=[plane_size[0]//2,plane_size[1]//2]

def split(n):
    if n>100:
        return 100
    elif n<0:
        return 0
    else:
        return n
    
def wrap_2d(plane,center,num_circle):
    #生成直角坐标系矩阵
    center_mat=np.zeros((101,101,2))
    for i in range(len(center_mat)):
        for j in range(len(center_mat[i])):
            center_mat[i][j][0]=-(i-50)
            center_mat[i][j][1]=j-50
    #生成半径缩放矩阵
    r_mat=np.zeros((101,101))
    for i in range(len(r_mat)):
        for j in range(len(r_mat[i])):
            if center_mat[i][j][0]==0 or center_mat[i][j][1]==0:
                r=1
            else:
                big_v=abs(center_mat[i][j][0]) if abs(center_mat[i][j][0])>abs(center_mat[i][j][1]) else abs(center_mat[i][j][1])
                small_v=abs(center_mat[i][j][1]) if abs(center_mat[i][j][0])>abs(center_mat[i][j][1]) else abs(center_mat[i][j][0])
                r=np.cos(abs(np.arctan(small_v/big_v)))
            r_mat[i][j]=r
    #生成旋转向量矩阵
    vector_mat=np.zeros((101,101,3))
    for i in range(len(vector_mat)):
        for j in range(len(vector_mat[i])):
            #v=[]
            if center_mat[i][j][0]==0:
                v=[0,1,0]
            if center_mat[i][j][1]==0:
                v=[1,0,0]
            
            #vk=np.tan((np.arctan(center_mat[i][j][0]/center_mat[i][j][1])/np.pi+0.5)*np.pi)
            if i!=50 and j!=50:
                vk=[center_mat[i][j][0],center_mat[i][j][1]]/(center_mat[i][j][0]**2+center_mat[i][j][1]**2)**0.5
            else:
                vk=[0,0,1]
            #print(vk,i,j)
            if center_mat[i][j][0]>0 and center_mat[i][j][1]>0:
                v=[abs(vk[1]),-abs(vk[0]),0]
            if center_mat[i][j][0]>0 and center_mat[i][j][1]<0: 
                v=[-abs(vk[1]),-abs(vk[0]),0]
            if center_mat[i][j][0]<0 and center_mat[i][j][1]<0:
                v=[-abs(vk[1]),abs(vk[0]),0]
            if center_mat[i][j][0]<0 and center_mat[i][j][1]>0: 
                v=[abs(vk[1]),abs(vk[0]),0]
            vector_mat[i][j][0]=v[0]
            vector_mat[i][j][1]=v[1]
            vector_mat[i][j][2]=v[2]
    #生成角矩阵
    angle_mat=np.zeros((101,101))
    for i in range(len(center_mat)):
        for j in range(len(center_mat[i])):
            l=((center_mat[i][j][0]**2+center_mat[i][j][1]**2)**0.5*r_mat[i][j])/50.5
            angle_mat[i][j]=l
    #缠绕
    res=np.zeros((101,101,101))
    point_lis=[]
    for i in range(len(plane)):
        for j in range(len(plane[i])):
            p_high=plane[i][j]
            #p=[center_mat[i][j][0],center_mat[i][j][1],0]
            #p=[0,0,-50]
            p=np.quaternion(0,0,0,-1)
            angle=angle_mat[i][j]*np.pi*num_circle
            v=vector_mat[i][j]
            a=np.cos(angle/2)*np.quaternion(1,0,0,0)
            b=np.sin(angle/2)*v[0]*np.quaternion(0,1,0,0)
            c=np.sin(angle/2)*v[1]*np.quaternion(0,0,1,0)
            d=np.sin(angle/2)*v[2]*np.quaternion(0,0,0,1)
            h=a+b+c+d
            h_=a-b-c-d
            r=r_mat[i][j]
            p_new=h*p*h_
            #print(p_new,r,i,j)
            p_new=p_new#*r
            #print(p_new)
            x_=int(p_new.x*50)+50
            y_=int(p_new.y*50)+50
            z_=int(p_new.z*50)+50
            #x_=split(x_)
            #y_=split(y_)
            #z_=split(z_)
            res[x_][y_][z_]=1
            
            point_lis.append(p_new*p_high)
    
    #算出缠绕的质心
    fourier_center=np.mean(point_lis)
    return fourier_center,res

def fourier_fit(plane,f_num):
    f_lis=[0]
    f_res=[]
    for i in range(f_num):
        f_lis.append(i+1)
        f_lis.append(-i-1)
    f_lis=sorted(f_lis)
    #print(f_lis)
    center=[len(plane)//2,len(plane[0])//2]
    for i in range(len(f_lis)):
        f_n=f_lis[i]
        #print(f_n)
        f_center,f_sphere=wrap_2d(plane,center,f_n)
        f_res.append(f_center)
    return f_res

def gen_sphere():
    #生成直角坐标系矩阵
    center_mat=np.zeros((101,101,2))
    for i in range(len(center_mat)):
        for j in range(len(center_mat[i])):
            center_mat[i][j][0]=-(i-50)
            center_mat[i][j][1]=j-50
    #生成半径缩放矩阵
    r_mat=np.zeros((101,101))
    for i in range(len(r_mat)):
        for j in range(len(r_mat[i])):
            if center_mat[i][j][0]==0 or center_mat[i][j][1]==0:
                r=1
            else:
                big_v=abs(center_mat[i][j][0]) if abs(center_mat[i][j][0])>abs(center_mat[i][j][1]) else abs(center_mat[i][j][1])
                small_v=abs(center_mat[i][j][1]) if abs(center_mat[i][j][0])>abs(center_mat[i][j][1]) else abs(center_mat[i][j][0])
                r=np.cos(abs(np.arctan(small_v/big_v)))
            r_mat[i][j]=r
    #生成旋转向量矩阵
    vector_mat=np.zeros((101,101,3))
    for i in range(len(vector_mat)):
        for j in range(len(vector_mat[i])):
            #v=[]
            if center_mat[i][j][0]==0:
                v=[0,1,0]
            if center_mat[i][j][1]==0:
                v=[1,0,0]
            
            #vk=np.tan((np.arctan(center_mat[i][j][0]/center_mat[i][j][1])/np.pi+0.5)*np.pi)
            if i!=50 and j!=50:
                vk=[center_mat[i][j][0],center_mat[i][j][1]]/(center_mat[i][j][0]**2+center_mat[i][j][1]**2)**0.5
            else:
                vk=[0,0,1]
            #print(vk,i,j)
            if center_mat[i][j][0]>0 and center_mat[i][j][1]>0:
                v=[abs(vk[1]),-abs(vk[0]),0]
            if center_mat[i][j][0]>0 and center_mat[i][j][1]<0: 
                v=[-abs(vk[1]),-abs(vk[0]),0]
            if center_mat[i][j][0]<0 and center_mat[i][j][1]<0:
                v=[-abs(vk[1]),abs(vk[0]),0]
            if center_mat[i][j][0]<0 and center_mat[i][j][1]>0: 
                v=[abs(vk[1]),abs(vk[0]),0]
            vector_mat[i][j][0]=v[0]
            vector_mat[i][j][1]=v[1]
            vector_mat[i][j][2]=v[2]
    #生成角矩阵
    angle_mat=np.zeros((101,101))
    for i in range(len(center_mat)):
        for j in range(len(center_mat[i])):
            l=((center_mat[i][j][0]**2+center_mat[i][j][1]**2)**0.5*r_mat[i][j])/50.5
            angle_mat[i][j]=l
    #缠绕
    point_lis=[]
    
    sphere_map=np.zeros((101,101,3))
    for i in range(len(plane)):
        for j in range(len(plane[i])):
            #p_high=1#plane[i][j]
            #p=[center_mat[i][j][0],center_mat[i][j][1],0]
            #p=[0,0,-50]
            p=np.quaternion(0,0,0,-1)
            angle=angle_mat[i][j]*np.pi*1#num_circle
            v=vector_mat[i][j]
            a=np.cos(angle/2)*np.quaternion(1,0,0,0)
            b=np.sin(angle/2)*v[0]*np.quaternion(0,1,0,0)
            c=np.sin(angle/2)*v[1]*np.quaternion(0,0,1,0)
            d=np.sin(angle/2)*v[2]*np.quaternion(0,0,0,1)
            h=a+b+c+d
            h_=a-b-c-d
            r=r_mat[i][j]
            p_new=h*p*h_
            #print(p_new,r,i,j)
            p_new=p_new#*r
            #print(p_new)
            #x_=int(p_new.x*50)+50
            #y_=int(p_new.y*50)+50
            #z_=int(p_new.z*50)+50
            #x_=split(x_)
            #y_=split(y_)
            #z_=split(z_)
            
            #point_lis.append(p_new*p_high)
            #print(p_new)
            sphere_map[i][j][0]=p_new.x#[0]#*p_high
            sphere_map[i][j][1]=p_new.y#[1]
            sphere_map[i][j][2]=p_new.z#[2]
    return sphere_map,vector_mat,angle_mat#point_lis

def gen_ray_d(center):
    ray_map=np.zeros((101,101,3))
    
    return ray_map

def defourier1(flis):
    f_num=len(flis)//2
    f_lis=[0]
    f_lis+=[i+1 for i in range(f_num)]
    f_lis+=[-i-1 for i in range(f_num)]
    f_lis=sorted(f_lis)
    #im_res=np.zeros((im_size[0],im_size[1],im_size[2]))
    #res_lis=[]
    new_center=np.mean(flis)
    new_center=[new_center.x,new_center.y,new_center.z]
    #print('new_center')
    #print(new_center)
    #sphere_lis=[]
    ray_d_array,vector_mat,angle_mat=gen_sphere()
    mean_close_surface=np.zeros((101,101,3))
    for i in range(len(ray_d_array)):
        for j in range(len(ray_d_array[i])):
            interlis=[]
            for k in range(len(flis)):
                center=flis[k]
                center=[center.x,center.y,center.z]
                #sphere_tmp=gen_sphere(center)
                #sphere_lis.append(sphere_tmp)
                direction=ray_d_array[i][j]
                
                inter_point=intersection(new_center,direction,center,1)
                
                if inter_point!=None:
                    
                    interlis.append(inter_point)
            mean_close_surface_point=np.mean(interlis)
            mean_close_surface[i][j]=mean_close_surface_point
    res=np.zeros((101,101))
    for i in range(len(mean_close_surface)):
        for j in range(len(mean_close_surface[i])):
            p=mean_close_surface[i][j]
            p=np.quaternion(0,p[0],p[1],p[2])
            v=vector_mat[i][j]
            angle=-angle_mat[i][j]
            a=np.cos(angle/2)*np.quaternion(1,0,0,0)
            b=np.sin(angle/2)*v[0]*np.quaternion(0,1,0,0)
            c=np.sin(angle/2)*v[1]*np.quaternion(0,0,1,0)
            d=np.sin(angle/2)*v[2]*np.quaternion(0,0,0,1)
            h=a+b+c+d
            h_=a-b-c-d
            p_new=h*p*h_
            p_new_x=p_new.x
            p_new_y=p_new.y
            p_new_z=p_new.z
            p_new_x=0 if p_new_x<0 else p_new_x
            p_new_x=100 if p_new_x>100 else p_new_x
            p_new_y=0 if p_new_y<0 else p_new_y
            p_new_y=100 if p_new_y>100 else p_new_y
            
            res[int(p_new_x*100)][int(p_new_y*100)]=p_new_z
    return res

fft=fourier_fit(plane,20)
#print(fft)
Dfft=defourier1(fft)
plt.imshow(Dfft)
#dftlis,dftim=defourier(fft, [101,101], [50,50], [101,101])