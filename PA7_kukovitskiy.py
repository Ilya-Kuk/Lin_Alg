import sympy as sy
import numpy as np
import matplotlib.pyplot as plt
from sympy import *

#######  1  #########
# a with hw
# b Finding spectral decomposition of S

S = sy.Matrix([[73,-36],[-36,52]])
S = S/100

Q,D = S.diagonalize(normalize=True)

print('S = Q D Q^T, where:\n  Q = ',Q,', and \n  D = ',D)


###################################### ???
def axes():
    plt.axhline(0, alpha=.1)
    plt.axvline(0, alpha=.1)
    
x1 = np.linspace(-5,5,1000)
x2 = np.linspace(-5,5,1000)

x1,x2 = np.meshgrid(x1,x2)

a = 1/np.sqrt(3)
b = 1/np.sqrt(3)
c = -1/np.sqrt(7)
d = 1/np.sqrt(7)

fig = plt.figure(1)
ax = fig.add_subplot(111)

plt.contour(x1,x2,5*x1**2 - 4*x1*x2 + 5*x2**2,[1])
plt.arrow(0,0,a,b)
plt.arrow(0,0,c,d)
ax.annotate('u1', xy=(0.5, 0.5), xytext=(1, 1),
            arrowprops=dict(facecolor='black', width = 1,shrink=0.05),
            )
ax.annotate('u2', xy=(-0.25, 0.25), xytext=(-1, 1),
            arrowprops=dict(facecolor='black', width = 1,shrink=0.1),
            )

plt.xlim([-2,2])
plt.ylim([-2,2])
axes()
plt.xlabel('x1')
plt.ylabel('x2')
plt.grid()
plt.axis('scaled')
####################################

