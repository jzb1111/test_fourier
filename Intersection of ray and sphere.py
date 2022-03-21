# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 18:20:41 2022

@author: asus
"""

def dot(a, b):
	"""Dot product"""
	return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def rs_intersect(R0, d, C, r):
    """Ray/sphere intersection"""
    R0 = (R0[0] - C[0], R0[1] - C[1], R0[2] - C[2])
    dDotR0 = dot(d, R0)
    print(dDotR0)
    t = -dDotR0 - (dDotR0*dDotR0 - dot(R0, R0) + r*r)**0.5
    print(t)
    print(dDotR0 + (dDotR0*dDotR0 - dot(R0, R0) + r*r)**0.5)
    return (R0[0] + t*d[0], R0[1] + t*d[1], R0[2] + t*d[2])

def calc_intersect(R0,d,C,r,mode='single'):
    if (R0[0]-C[0])**2+(R0[1]-C[1])**2+(R0[2]-C[2])**2>r**2:
        
        R0 = (R0[0] - C[0], R0[1] - C[1], R0[2] - C[2])
        dDotR0 = dot(d, R0)
        #print(dDotR0)
        t = -dDotR0 - (dDotR0*dDotR0 - dot(R0, R0) + r*r)**0.5
        t1= dDotR0 + (dDotR0*dDotR0 - dot(R0, R0) + r*r)**0.5
        if t>0:
            if mode=='single':
                return (R0[0] + t1*d[0], R0[1] + t1*d[1], R0[2] + t1*d[2])
            if mode=='double':
                return [(R0[0] + t1*d[0], R0[1] + t1*d[1], R0[2] + t1*d[2]),(R0[0] + t*d[0], R0[1] + t*d[1], R0[2] + t*d[2])]
        else:
            return None
    else:
        R0 = (R0[0] - C[0], R0[1] - C[1], R0[2] - C[2])
        dDotR0 = dot(d, R0)
        #t = -dDotR0 - (dDotR0*dDotR0 - dot(R0, R0) + r*r)**0.5
        t1= dDotR0 + (dDotR0*dDotR0 - dot(R0, R0) + r*r)**0.5
        return (R0[0] + t1*d[0], R0[1] + t1*d[1], R0[2] + t1*d[2])
    

R0 = (0, -0.5, 0)
d = (0, 1, 0)
C = (0, 0, 0)
r = 1

#R0：球心
#d：射线方向
#C：射线起点
#r：球半径

res=rs_intersect(R0, d, C, r)
print(res)

res1=calc_intersect(R0, d, C, r)
print(res1)
