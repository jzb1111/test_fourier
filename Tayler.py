# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 23:00:28 2022

@author: asus
"""

import numpy as np

def exp_Tayler(p,num):
    count=1
    for i in range(num-1):
        count+=(1/(jiecheng(i+1)))*cifang(p, i+1)
    return count

def jiecheng(n):
    if n==1:
        return n
    else:
        return n*jiecheng(n-1)
    
def cifang(p,n):
    if n==1:
        return p
    else:
        return p*cifang(p,n-1)

def matrix_cifang(p,n):
    if n==1:
        return p
    else:
        return np.matmul(p,matrix_cifang(p,n-1))

def exp_matrix_Tayler(p,num):
    count=np.eye(p.shape[0],p.shape[1])
    for i in range(num-1):
        count+=(1/(jiecheng(i+1)))*matrix_cifang(p, i+1)
    return count

