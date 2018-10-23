# Importing the libraries
import sympy as sy

#####  1  #######
### 4.4#15
## a)
A = sy.Matrix([[1,1],[2,-1],[-2,4]]) #input matrix A

Q,R = A.QRdecomposition() #decomposing A into Q and R s.t. A=QR

print('Q = ',Q)

## b)
print('q3 is in the left nullspace.')

## c)
B = sy.Matrix([[1,1,0],[2,-1,0],[-2,4,5]]) #input matrix B with additional independent vector

Q,R = B.QRdecomposition() #decompose B into QR

print('Q = ',Q)

print('q3 = ',Q[:,2]) #additional vector in Q is q3 which is orthonormal wrt q1 and q2

## d)

b = sy.Matrix([[1],[2],[7]]) #input vector b

proj_Ab = A*((A.T*A).inv())*A.T*b #projecting b on C(A)

xhat = ((A.T*A).inv())*A.T*b #define xhat, where A*xhat = proj_Ab

print('x-hat is ',xhat,', \np is ',proj_Ab)

#####  2  #######
### 4.4#21
## a)

A = sy.Matrix([[1,-2],[1,0],[1,1],[1,3]]) #input matrix A

Q,R = A.QRdecomposition() #decompose A

print('Q = ',Q)

## b)

b = sy.Matrix([[-4],[-3],[3],[0]])

proj_Ab = A*((A.T*A).inv())*A.T*b # projecting b on C(A) = C(Q)

print('projection of b on C(A)=C(Q) is ',proj_Ab)

#####  2  #######
### 4.4#23

A = sy.Matrix([[1,2,4],[0,0,5],[0,3,6]]) #input matrix A

Q,R = A.QRdecomposition() #decompose A

print('A\n=\nQ\nR\n is\n',A,'\n=\n',Q,'\n',R)

