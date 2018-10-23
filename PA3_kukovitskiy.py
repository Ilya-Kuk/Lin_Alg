# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 00:59:33 2018

@author: ilyak
"""

import numpy as np
import sympy as sy
import matplotlib.pyplot as plt


## 1

A = sy.Matrix([ [1,-1,3],[5,-4,-4],[7,-6,2] ])

A.rref()

## 2

At = A.transpose()
At
At.rref()

## 3

A.rank()

## 4

A = sy.Matrix([ [2,4,1,-5,5],[1,2,1,-2,3],[1,2,0,-3,3] ])

A.rref()

## 5

At = A.transpose()
At
At.rref()

## 6

A.rank()

## 7

# House matrix
H = np.array([  #  1st row x, 2nd row y; first column point 1...
        [-6, -6, -7, 0, 7, 6,  6, -3, -3,  0,  0, -6] , 
        [-7, 2 , 1 , 8, 1, 2, -7, -7, -2, -2, -7, -7] ])

T = np.eye(2,2)  # identity_2

Ht = T@H  #  cross-product
x = Ht[0,:]  # plot plt.plot takes args as single arrays
y = Ht[1,:]

plt.plot(x,y)  #  plot house

## (a)

# plot houses under the following transformation matrices

D = np.array([ [2,0],[0,1] ])
A = np.array([ [.7,.7],[.3,.3] ])
U = np.array([ [1,1],[0,1] ])

x_d = D[0,:]
y_d = D[1,:]

x_a = A[0,:]
y_a = A[1,:]

x_u = U[0,:]
y_u = U[1,:]

plt.plot(x_d,y_d)

plt.plot(x_a,y_a)

plt.plot(x_u,y_u)

## (b)

# adding chimney to house matrix H

chimney = np.array([
        [4,4,2,2], 
        [4,7,7,6] ])

H_chim = np.insert(arr=H, obj=4, values=chimney.transpose(), axis=1) # args: inserted, index, inserting, axis

#plotting H_chim

x_H_c = H_chim[0,:]
y_H_c = H_chim[1,:]

plt.plot(x_H_c,y_H_c)

## (c)

# flip the chimneyed house over the x-axis

flipX = np.array([
        [1,0],
        [0,-1] ])

H_c_flipX = flipX@H_chim

x_HcfX = H_c_flipX[0,:]
y_HcfX = H_c_flipX[1,:]

plt.plot(x_HcfX,y_HcfX)
plt.plot(x_H_c,y_H_c)

## (d)

flipXY = np.array([
        [0,-1],
        [-1,0] ])

H_c_flipXY = flipXY@H_chim

x_HcfXY = H_c_flipXY[0,:]
y_HcfXY = H_c_flipXY[1,:]

