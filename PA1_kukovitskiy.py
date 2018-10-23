# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

## 1) creating and printing row vectors

v1 = np.array([-1,0,1])
v2 = np.array([1,1,1])

print('v1 =',v1,'; v2 =',v2)

## 2) performing and printing linear algebra

a2 = 3*v1
b2 = v1 + v2
c2 = - 1*v1 - 2*v2

print('The scalar multiple 3v1 is',a2,',\nthe linear combination v1 + v2 is,',b2,',\nand the linear combination -v1-2 v2 is,',c2,'.')

## 3) storing and printing components of a vector

a3 = v1[0]
b3 = v2[2]

print('The 1st component of v1 is',a3,'\nand the 3rd component of v2 is',b3,'.')

## 4) creating and printing column vector

v3 = np.array([ [3],[0],[3] ])

print('The column vector v3 is:\n',v3)

## 5) printing sizes of vectors

a5 = v1.size
b5 = v3.size

print('The size of v1 is',a5,', and the size of v3 is',b5,'.')

## 6) creating matrices

A = np.array([ [1,-1,1],[1,1,-1],[-1,-1,1] ])
B = np.array([ [1,0,-1],[3,1,-1] ])

## 7) printing properties and transformations of matrices

a7 = A.size
b7 = B.size
c7 = 2*B

print('The size of A is',a7,'\n, the size of B is',b7,'\n, and the scalar multiple 2B is\n',c7,'.')

## 8) printing particular rows, columns, and entries in matrices

a8 = B[0,:]
b8 = A[:,1]
c8 = A[1,2]

print('The first row of B is',a8,'\n, the second column of A is',b8,'\n, and the entry at the 2nd row & 3rd column of A is',c8,'.')

## 9) filling an array non-manually

c = np.array([], dtype=int)

for i in range(1,101):
    c = np.append(c,[i])

## 10) printing particular entry of c

print('The 13th entry of c is',c[12],'.')