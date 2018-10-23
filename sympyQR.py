#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 14:58:03 2018

@author: natalie
"""

import numpy as np
import sympy as sy

# Given a matrix A = [a,b]
a = sy.Matrix([[2],[2],[-2]])
b = sy.Matrix([[1],[0],[4]])
A = a.row_join(b)
print('A =  \n',A)
# we can ask numpy to compute its QR decomposition
Q,R = A.QRdecomposition()
print('\n Q = \n',Q)

# We know that C(A) = C(Q), so if we're trying
# to solve a least squares problem Ax = b
# by projecting b onto C(A), we can just as well
# project b onto C(Q)

b = sy.Matrix([[1],[2],[7]])

projA = A*((A.T*A).inv())*A.T*b # project b on C(A)
print('\n The projection of b onto C(A) = \n ', projA)
projQ = Q*Q.T*b
print('\n The projection of b onto C(Q) = \n', projQ)
# Notice projA = projC, as it should be
print('\n The error between our approximation/projection and b is ||proj-b|| =', sy.sqrt((projQ-b).dot(projQ-b)))


# If we want the xhat vector such that A xhat = projA = projQ
# we solve for xhat (or back up a step before finding the projection)
xhat = (A.T*A).inv()*A.T*b
print('\n xhat = \n',xhat)


