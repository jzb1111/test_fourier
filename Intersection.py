# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 11:25:42 2022

@author: asus
"""

def dot(a, b):
	"""Dot product"""
	return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def intersection(P,d,C,r):
    a=[C[0]-P[0],C[1]-P[1],C[2]-P[2]]
    l=dot(d,a)
    a_sq=dot(a,a)
    if a_sq>r**2 and l<0:
        return None
    
    m_sq=a_sq-l**2
    if m_sq>r**2:
        return None
    q=(r**2-m_sq)**0.5
    if a_sq>r**2:
        #t=l-q
        t=l+q
    else:
        t=l+q
    #print(t)
    Q=[P[0]+t*d[0],P[1]+t*d[1],P[2]+t*d[2]]
    return Q

#P = (0, -0.5, 0)
#d = (0, 1, 0)
#C = (0, 5, 0)
#r = 2

#P：球心
#d：射线方向
#C：射线起点
#r：球半径

#res=intersection(P,d,C,r)
#print(res)