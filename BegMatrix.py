#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 15:53:11 2018

@author: natalie
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 10:53:44 2018

@author: natalie
"""
import numpy as np

#####################
# vectors
v = np.array([1,2,3]) # create a row vector
print(v) # print vector v
print('v = ',v) # print the vector v with a string to tell us what it is
print('The size of v is ', v.shape) # print its size

w = np.array([[1],[2],[3]]) # create a column vector
print('w = ',w) # print the vector w with a string to tell us what it is
print('The size of w is ', w.shape) # print its size

# another row vector
v2 = np.array([1,1,1]) # create second row vector
print('v2 = ',v2)
print('2v = ',2*v) # scalar multiplication and add line space after output
print('v+v2 = ', v+v2) # addition
print('2*v-3*v2 = ', 2*v-3*v2,'\n') # linear combination

# If we try to add vectors of a different size
# (you should try this and see what happens)
#v3 = np.array([1,2])
#v+v3

# slicing
a1 = v[1]
print('a1 = ' +str(a1)) # notice we get SECOND entry
a0 = v[0]
print('a0 = ' +str(a0)) # notice we get FIRST entry, python index starts at zero

# create vector of equally spaced point
v3 = np.linspace(1,100,50) # np.linspace(start,stop,# of points, etc...)
print('v3 = ',v3,'\n') # notice the numbers in the output.
coeff = np.arange(1,100,2) # odd numbers from 1 to 100
print('coeff = ',coeff,'\n')

cv = np.zeros((len(coeff),len(v)))  # create zero matrix with #rows = length(coeff)
                                    # and #columns = length v
print(cv.shape)

# a for loop, notice the colon and indent
# figure out what the loop does
for i in range(len(coeff)):
    cv[i,:] = coeff[i]*v
print('cv = ',cv,'\n')

#####################
# matrices

A = np.array([ [ 1,2,3],[4,5,6],[7,8,9]]) # create matrix
print('Here is matrix A \n', A,'\n')
print('The size of A is ', A.shape,'\n')

# slicing
print('entry a_{1,1} = ',A[0,0])  # a_(1,1)
print('row 1 of A = ',A[0,:]) # first row of A [0,;] is first row all columns
print('column 3 of A = ', A[:,2]) # all rows and third column, notice output is a row
print('\n') # this gives a blank line in the output

# identity matrix
print('The 3x3 identity matrix I = \n ',np.eye(3))


