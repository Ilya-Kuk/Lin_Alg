#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 13:22:08 2018

@author: natalie
"""
import numpy as np
import sympy as sy
import matplotlib.pyplot as plt

#####################
## RREF(A) and A^T
## RREF is a command in the SymPy package and so we need to 
## enter the matrix as a SymPy matrix
print('Number 1 ****************************** \n')
A = sy.Matrix([[4,6,8,10],[5,3,1,-1],[7,-6,5,-4]]) # create matrix A
print('A = \n',A,'\n') # print the matrix A with a string to tell us what it is
print('RREF(A) = \n',A.rref(),'\n') # compute RREF(A)

####################
## rank(A)
## The rref(A) gives a "tuple", the matrix and a vector that
## gives the indices of the columns with a pivot.  We can
## ask for the length of that vector to know how many pivots
## are in the RREF(A), which is the rank(A).
pivotvector = A.rref()[1]
print('The pivots of A occur in columns',pivotvector,'. \n')
print('We can determine the rank by knowing the number\
      of pivots, which is the length of "pivotvector" = ',len(pivotvector),'\n')
##
## AND/OR, there is a rank(A) command in SymPy
print('The built-in SymPy command gives rank(A) = ', A.rank(simplify=True),'\n') # have SymPy calculate rank

#####################
## We can use the package matplotlib to make graphics in python.
## One thing we can do is plot polygons whose
## (x,y) vertices are given the columns of a 2xn matrix.
## Here is an assymetric star

x = np.array([0,6, 3, -1, 9, 0 ])
y = np.array([0,5,-1,  4, 3, 0])
plt.figure(1)
plt.plot(x,y,'m')

#####################
## We can apply a linear transform to stretch, rotate, and flip
## each vector.  Rather than do this one vector at a time,
## we can create a matrix whose column is
## each vector and then apply a linear transformation 
## to all matrices by multiplying the transform matrix
## and the matrix of vectors that create the shape. 
## 
starmatrix = np.vstack((x,y)) # create 2 by n matrix of vertices

del A # delete previous matrix A that we defined above
A = np.array([[-1,0],[0,1]]) # matrix representation of linear transform
print('A transformformation matrix that moves e_1 to (-1,0)\
      leaves e_2 at (0,1) \n ',A)
Astar = np.dot(A,starmatrix)
plt.plot(Astar[0,:],Astar[1,:],'k')
plt.axis([-9, 9, -9, 9])

## If we want to plot transform in separate figure
plt.figure(2)
plt.plot(Astar[0,:],Astar[1,:],'k')
plt.axis([-9, 9, -9, 9])


