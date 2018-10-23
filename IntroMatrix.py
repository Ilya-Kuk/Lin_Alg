#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 10:53:44 2018

@author: natalie
"""
import numpy as np
import sympy as sy

#####################
# vectors
v1 = np.array([1,2,3]) # create a row vector
print('v1 = ',v1) # print the vector v with a string to tell us what it is

v2 = np.array([1,2,3]) # create second row vector
print('v2 = ',v2)

print('unusual multiplication, v1*v2 = ', v1*v2,'\n') # multiply entrywise, aka "Hadamard multiply"!!
print('dot product v1.v2 = ',np.dot(v1,v2))  # take the dot product of the two vectors
print('another form of dot product v1.v2 = ', v1@v2,'\n') # shortcut for dot product

#####################
# matrices

A = np.array([ [ 1,2,3],[4,5,6],[7,8,9]]) # create matrix
print('Here is matrix A: \n', A,'\n')
print('The size of A is ', A.shape,'.\n')
print('2*A = \n', 2*A,'\n') # scalar multiplication
print('Unusual multiplication, v1*A = \n ', v1*A,'\n') # what happened here? entrywise (Hadamard) multiplication
print('v1@A = ', v1@A) # and here? (our standard matrix multiplication)
print('np.dot(v1,A) = ',np.dot(v1,A)) # standard matrix multiplication

print('entry a_{1,1} = ',A[0,0])  # a_(1,1)
print('row 1 of A = ',A[0,:]) # first row of A [0,;] is first row all columns
print('column 3 of A = ', A[:,2]) # all rows and third column, notice output is a row
print('\n')

B = np.array([ [ 1,2,3],[4,5,1],[1,1,1]]) # create matrix
print('Here is matrix B: \n', B,'\n')
print('The 3x3 identity matrix I = \n',np.eye(B.shape[0]),'\n') # the identity matrix
x = np.linalg.solve(B,v1) # using NumPy to solve a square, nonsingular linear system
print('The solution to Bx = v1  is x = ',x)
print('Check Bx = v1 using np.allclose:',np.allclose(B@x,v1),'\n')
# what happens if B is rectangular?  Try it and see
# https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.linalg.solve.html

# We can use SymPy RREF command for rectangular or singular systems
# print('RREF(B) = ',B.rref()) # doesn't work because B has defined in NumPy 
print('Using SymPy for symbolic computations \n')
newB = sy.Matrix([ [ 1,2,3,1],[4,5,1,1],[1,1,1,1]]) # create matrix using SymPy
print('Matrix in Sympy:  newB = ',newB,'\n')
print('RREF(newB) = \n',newB.rref(),'\n')
varb = sy.Matrix([['b1'],['b2'],['b3']]) # create array of strings
print('A vector of strings, b =',varb,'\n')
Bb = newB.col_insert(4,varb) # create the augmented matrix
print('The augmented matrix [B|b] = \n', Bb,'\n')
print('RREF([B|b]) = \n',Bb.rref(),'\n')  # RREF of augmented matrix

# Solve linear system again, this time with no solution
print('Try to solve linear system with no solution, see what happens: \n')
C = sy.Matrix([ [ 1,2,3,1],[1,2,3,1],[1,2,3,1]]) # notice the rows
print('C = \n',C,'\n')
Cb = C.col_insert(4,varb) # create the augmented matrix
print('Augmented matrix [C|b] = ',Cb,'\n')
print('RREF([C|b] = ',Cb.rref())  # compare python's output to yours by hand
