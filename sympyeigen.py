#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 21:53:31 2018

@author: natalie
"""

import sympy as sy

# Create matrix A
A = sy.Matrix([[3,-2,4,-2],[5,3,-3,-2],[5,-2,2,-2],[5,-2,-3,3]])
print('A = \n',A, '\n')

# find eigenvalues and their multiplicities 
# output in form as (eigenvalue:algebraic multiplicity)
print('\n Eigenvalues of A and their AM: \n',A.eigenvals()) 
print('\n This one has lambda_1 = 3 with multiplicity 1, ')
print(' lambda_2 = -2, with multiplicity 1,')
print(' lambda_3 = 2, with multiplicity 2')
print(' Notice 4 x 4 matrix and 4 eigenvalues, counting multiplicities.')

# find eigenvectors
#output form is (eigenvalue:algebraic multiplicity, [eigenvectors])
print('\n Eigenvalues,AM,eigenvectors of A: \n',A.eigenvects())
eig = A.eigenvects()
print('\n Sometimes it is hard to see the output clearly,')
print(' let us print each eigenpair one at a time')
for var in eig:
    print('\n Eigenpair',eig.index(var)+1,'of A with AM: \n', var)
print('Notice this matrix is diagonalizable as it has four linearly independent eigenvectors,')
print('two eigenvectors for lambda_3 = 5.')
# diagonalize the matrix 
# (in one step, although the above gives us the necessary information)
X,D = A.diagonalize() # gives 
print('\n Matrix of eigenvectors, X = \n ',X)
print('\n Diagonal matrix of eigenvalues, D = \n',D)
# Note X**-1 computes the inverse of X (** means an exponent follows)
print('\n Inverse of matrix of eigenvectors, X^(-1) = \n',X**-1)

# we can check that A = XDX^(-1)
verifyA = X*D*X**-1
print('\n verifyA-A  = \n', verifyA-A) #look at difference, should be zero if they are equal

