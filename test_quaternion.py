# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 08:01:14 2022

@author: asus
"""

import numpy as np
import quaternion


threshold=0.01
l100lis=[]
l010lis=[]
l001lis=[]
ln100lis=[]
l0n10lis=[]
l00n1lis=[]

for i in range(1):
    for j in range(20):
        for k in range(20):
            for l in range(20):
                q=np.quaternion(i/20,(j-10)/20,(k-10)/20,(l-10)/20)
                res=np.exp(2*np.pi*1*q)
                x=res.x
                y=res.y
                z=res.z
                if abs(x-1)<=threshold and abs(y-0)<=threshold and abs(z-0)<=threshold:
                    l100lis.append(q)
                if abs(x-0)<=threshold and abs(y-1)<=threshold and abs(z-0)<=threshold:
                    l010lis.append(q)
                if abs(x-0)<=threshold and abs(y-0)<=threshold and abs(z-1)<=threshold:
                    l001lis.append(q)
                if abs(x+1)<=threshold and abs(y-0)<=threshold and abs(z-0)<=threshold:
                    ln100lis.append(q)
                if abs(x-0)<=threshold and abs(y+1)<=threshold and abs(z-0)<=threshold:
                    l0n10lis.append(q)
                if abs(x-0)<=threshold and abs(y-0)<=threshold and abs(z+1)<=threshold:
                    l00n1lis.append(q)
                print(i,j,k,l)
                
print('l100lis')
for i in range(len(l100lis)):
    print(l100lis[i])
    
print('l010lis')
for i in range(len(l010lis)):
    print(l010lis[i])
    
print('l001lis')    
for i in range(len(l001lis)):
    print(l001lis[i])

print('ln100lis')
for i in range(len(ln100lis)):
    print(ln100lis[i])
    
print('l0n10lis')
for i in range(len(l0n10lis)):
    print(l0n10lis[i])
    
print('l00n1lis')
for i in range(len(l00n1lis)):
    print(l00n1lis[i])