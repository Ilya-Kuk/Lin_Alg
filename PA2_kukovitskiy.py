# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:06:38 2018

@author: kukoviti1
"""
import numpy as np
import sympy as sy

### 1) Solving problems 1-4 and 5b from HW2:

## 1

#creating matrix of vector space
x = np.array([ [1,3],[-1,-2] ])
#creating desired vector
y = np.array([-3,4])

#solving for linear combination
scalars = np.linalg.solve(x,y)
#returning scalar factors
print('Ther would have been an error if there was no solution. The scalars are:',scalars,'.')

## 2

S = sy.Matrix([ [0,2,3,1],[0,-2,-2,0],[-2,1,2,1] ])
S.rref()

u = np.array([3,0,-3,6])

print('In reduced row echelon form, there is no linear combination of the vectors that can make the vector u.')

## 3

A = sy.Matrix([ [1,6,4],[2,4,-1],[-1,2,5] ])
A.rref()

print('Since one of the vectors is reduced to 0, the 3 vectors do not span 3D space. Since they don\'t span R3, these vectors do not form a basis for R3.')

## 4

B = sy.Matrix([ [-2,0,1],[3,2,5],[6,-1,1],[7,0,-2] ])
B.rref()

print('The set is linearly dependent, since there is one vector is reduced to 0. This is expected, of course, since there are 4 vectors in R3. The distinction is that more than one vector could have been expressed as a linear combination of the others - this was not the case. That is, the set spans all of R3.')

## 5

C = sy.Matrix([ [ 1,1,-2],[1,0,-1],[2,1,-3] ])
varb = sy.Matrix([['b1'],['b2'],['b3']])

Cc = C.col_insert(3,varb) # create the augmented matrix
Cc.rref()



