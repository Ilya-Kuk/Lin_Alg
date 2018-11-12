import sympy as sy
import numpy as np
import matplotlib.pyplot as plt
from sympy import simplify

#######  1  #########

# a with hw

# b Finding spectral decomposition of S

S = sy.Matrix([[73,-36],[-36,52]]) #inputting matrix
S = S/100

Q,D = S.diagonalize(normalize=True) #diagonalizing

print('S = Q D Q^T, where:\n  Q = ',Q,', and \n  D = ',D)

# c Plotting level curve xT S x = 1 with lables

def axes():  #defining axes, a function that sets the axes at the origin
    plt.axhline(0, alpha=.1)
    plt.axvline(0, alpha=.1)
    
x1 = np.linspace(-5,5,1000) #creating grid axes
x2 = np.linspace(-5,5,1000)

x1,x2 = np.meshgrid(x1,x2) #creating grid

a = float(Q[0,0]/np.sqrt(float(Q[0,0]))) #eigenvector components, normalized by square root of eigenvalue
b = float(Q[1,0]/np.sqrt(float(D[0,0])))
c = float(Q[0,1]/np.sqrt(float(D[1,1])))
d = float(Q[1,1]/np.sqrt(float(D[1,1])))

fig = plt.figure(1)  #creating figure
ax = fig.add_subplot(111)

plt.contour(x1,x2,(1/100)*(73*x1**2 - 72*x1*x2 + 52*x2**2),[1])  #plotting curve
plt.arrow(0,0,a,b) #u1
plt.arrow(0,0,c,d) #u2
ax.annotate('u1', xy=(1.9, 1.3), xytext=(3, 0),  #label u1
            arrowprops=dict(facecolor='black', width = 1,shrink=5),
            )
ax.annotate('u2', xy=(-1, 1.6), xytext=(-1.5, 3),  #label u2
            arrowprops=dict(facecolor='black', width = 1,shrink=0.1),
            )

plt.xlim([-2,2]) #plot window
plt.ylim([-2,2]) #plot window
axes() #using axes
plt.xlabel('x1') #label axes
plt.ylabel('x2')
plt.grid()
plt.axis('scaled')

# d with hw

# e expressing in quadratic form:

y = sy.Matrix([['y1'],['y2']]) #creating arbitrary vector y to represent quadratic equation
Quady = simplify(y.T*D*y)[0]

print('The quadratic form q(y1,y2) = y^T * D * y = ',Quady)

# f plotting the new curve q(y1,y2)=1.

y1 = np.linspace(-5,5,1000) #creating grid axes
y2 = np.linspace(-5,5,1000)

y1,y2 = np.meshgrid(y1,y2) #creating grid

fig = plt.figure(2) #creating figure
ax = fig.add_subplot(111)

plt.contour(y1,y2,y1**2/4 + y2**2,[1]) #plotting curve
plt.arrow(0,0,1/np.sqrt(1/4),0)  #u1
plt.arrow(0,0,0,1/np.sqrt(1))  #u2
ax.annotate('u1', xy=(1, -.25), xytext=(1, -1.5),  #label u1
            arrowprops=dict(facecolor='black', width = 1,shrink=5),
            )
ax.annotate('u2', xy=(-.25, .5), xytext=(-1.5, 1),  #label u2
            arrowprops=dict(facecolor='black', width = 1,shrink=0.1),
            )
# plot arguments
plt.xlim([-2,2])
plt.ylim([-2,2])
axes()
plt.xlabel('y1')
plt.ylabel('y2')
plt.grid()
plt.axis('scaled')

# g ###############right??

print(' We should note that the level curve of the quadratic form is an ellipse because the eigenvalues are both real, positive, and not equal to each other.')

#######  2  #########

# a with hw

# b Finding spectral decomposition of S

S = sy.Matrix([[0,2],[2,3]])

Q,D = S.diagonalize(normalize=True)

print('S = Q D Q^T, where:\n  Q = ',Q,', and \n  D = ',D)

# c Plotting level curve xT S x = 1 with lables

#creating plot grid
x1 = np.linspace(-5,5,1000)
x2 = np.linspace(-5,5,1000)

x1,x2 = np.meshgrid(x1,x2)

#eigenvector components
a = float(Q[0,0]) # sqrt(-1) is not valid here, but ||sqrt(-1)||==1
b = float(Q[1,0]) ## these components are for the reflecting axis anyway, scaling is sort of meaningless
c = float(Q[0,1]/2) # sqrt(4)==2
d = float(Q[1,1]/2)

#creating figure
fig = plt.figure(3)
ax = fig.add_subplot(111)

#plotting curve and eigenvectors with labels
plt.contour(x1,x2,x2*(4*x1 + 3*x2),[1])
plt.arrow(0,0,a,b)
plt.arrow(0,0,c,d)
ax.annotate('u1', xy=(-1, 0.3), xytext=(-3, 1),
            arrowprops=dict(facecolor='black', width = 1,shrink=0.1),
            )
ax.annotate('u2', xy=(1, 1), xytext=(2, 2),
            arrowprops=dict(facecolor='black', width = 1,shrink=5),
            )

#plot arguments
plt.xlim([-2,2])
plt.ylim([-2,2])
axes()
plt.xlabel('x1')
plt.ylabel('x2')
plt.grid()
plt.axis('scaled')

# d with hw

# e expressing in quadratic form:

y = sy.Matrix([['y1'],['y2']])
Quady = simplify(y.T*D*y)[0]

print('The quadratic form q(y1,y2) = y^T * D * y = ',Quady)

# f plotting the new curve q(y1,y2)=1.

# creating plot grid
y1 = np.linspace(-5,5,1000)
y2 = np.linspace(-5,5,1000)

y1,y2 = np.meshgrid(y1,y2)

#creating figure 4
fig = plt.figure(4)
ax = fig.add_subplot(111)

#plot curve and eigenvectors with labels
plt.contour(y1,y2,-y1**2 + 4*y2**2,[1])
plt.arrow(0,0,-1,0)
plt.arrow(0,0,0,1)
ax.annotate('u1', xy=(-2, 0), xytext=(-4,0),
            arrowprops=dict(facecolor='black', width = 1,shrink=5),
            )
ax.annotate('u2', xy=(0, 2), xytext=(0, 4),
            arrowprops=dict(facecolor='black', width = 1,shrink=0.1),
            )

#plot arguments			
plt.xlim([-2,2])
plt.ylim([-2,2])
axes()
plt.xlabel('y1')
plt.ylabel('y2')
plt.grid()
plt.axis('scaled')

# g ###############right??

print(' We should note that the level curve of the quadratic form is a hyperbola because the eigenvalues are both real, and one is negative whil the other is positive.')
