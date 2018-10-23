import sympy as sy
from __future__ import division
from sympy import *

#######  1  #########
### 6.2#6
## describe all matrices X that diagonalize matrix A and A^-1:

A = sy.Matrix([[4,0],[1,2]])

X,D = A.diagonalize() #diagonalizing A

print('A = X D X^-1, where\nX = ',X,'\n and D = ',D,'.')

Ai = A**-1

Xi,Di = Ai.diagonalize()

print('A^-1 = Xi Di Xi^-1, where\nXi = ',Xi,'\n and Di = ',Di,'.')

#######  2  #########
### 6.2#19
## diagonalize B, and compute XL^kX^-1 to show:

# a)
B = sy.Matrix([[5,1],[0,4]])

X,D = B.diagonalize() #diagonalizing B

print('B = X D X^-1, where \nX = ',X,'\nD = ',D,'.')

B
X*D*X**-1

# b) B_k = sy.Matrix([[5^k,5^k - 4^k],[0,4^k]])  show how the diagonalization = this

##### in hw #####

#######  3  #########
### 6.2#16

A1 = sy.Matrix([[.6,.9],[.4,.1]])

# a) diagonalize A1. Write diagonalization of A1^k.

X1,D1 = A1.diagonalize() #diagonalizing A1

print('A1 = X1 D1 X1^-1, where\nX1 = ',X1,'\n and D1 = ',D1,'.')

print('So A1^k = X1 D1^k X1^-1, where\nX1 = ',X1,'\n and D1 = ',D1,' to the power of k.')

# b) Show A1^3, A1^5, A1^10

print('A1^3 = ',A1**3,'\nA1^5 = ',A1**5,'\nA1^10 = ',A1**10,'.')

# c) Take \lim_{k\to\inf} A_1^k

##### in hw #####

#######  4  #########

# Create transition matrix T
T = sy.Matrix([[.7,.3,.6],[.2,.4,.2],[.1,.3,.2]])

# a) all 100 birds in canada, find bird location after 1 year
x0 = sy.Matrix([[100],[0],[0]])
x1 = T*x0

print('The birds after one year is the vector x1 = ',x1)

# b) Diagonalize T, write T^k
X,D = T.diagonalize() #diagonalizing T

print('T^k = X D^k X^-1, where:\nX = ',X,'\nD = ',D,'.')

# c) distribution of birds in year 10
x10 = (X * D**10 * X**-1)*x0

print('The distribution of birds in year 10 is ',x10,'.')

# d) steady state solutions

print('lim k to infinity xk = lim T^k*x0 = X lim D^k X^-1 * x0.\nlim D^k is the 3x3 matrix with all zeroes, except at the position for which D was 1, D(3,3).')

Dlim = sy.Matrix([[0,0,0],[0,0,0],[0,0,1]])

xlim = X * Dlim * X**-1 * x0

print('The steady-state solution is ',xlim,'.')

# e) what eigenvalue corresponds to this? explain.

print('The eigenvalue that corresponds to this is 1. Steady states are infinite iterations, as they approach an equilibrium. Since they can be expressed as a diagonalized matrix, this equates to infinitely multiplying a diagonal matrix D. In this context, all values within 1 of 0 approach 0, values outside 1 of 0 diverge, -1 oscillates, and 1 approaches 1. The only non-zero value in lim D^k ends up being the 3rd eigenvalue, that takes on the value 1.)

#######  5  #########

# a) Try diagonalizing A

A = sy.Matrix([[0,-6,-4],[5,-11,-6],[-6,-9,4]])

X,D = A.diagonalize()

# b) no. write eigenvals and eigenvects.

A_v = A.eigenvects()
A_e = A.eigenvals()

print('The eigenvalue', A_v[0][0],' has multiplicity', A_v[0][1],', it\'s eigenvector is', A_v[0][2],'.\n\nThe eigenvalue', A_v[1][0],' has multiplicity', A_v[1][1],', it\'s eigenvector is', A_v[1][2],'.')

# c) explain why you can't diagonalize this matrix.

lamda = symbols('lamda')
p = A.charpoly(lamda)
factor(p)

