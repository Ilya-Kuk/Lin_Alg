# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#####  1  #######

# Importing Data
dataset = pd.read_csv('HeartRates.csv')

# Printing shape of data
print('The shape of the data is:',dataset.shape,'.')

# Printing first 10 rows of data
print('The first 10 rows in the data are:\n',dataset.head(10) )

# Visualising the data
X = dataset.before
Y = dataset.after

plt.scatter(X, Y)
plt.title('Heart Rates')
plt.xlabel('before')
plt.ylabel('after')

###

# Creating matrix for fitting linear regression y = Cx + D
print('The corresponding Matrix representation is\n  [x 1] v = y\n  [x 1 | y],\n v = (C D).transpose')
print('Calling this matrix\n [A | y], \n note that A is inconsistent, since there are many rows and 2 columns. Not all y are in C(A). So we project y onto C(A).\nTo compute the corresponding v^ of the projection:\nv^ = (A.transpose A).inverse A.transpose y .')
# converting dataset to matrix B w.r.t.(x y) for matrix manipulations
B = dataset.values
B = np.asmatrix(B)
x = B[:,0]

# Creating Matrix A w.r.t. (C D):
A = np.concatenate((x, new_col), 1)

# Creating pseudo-inverse (At A)-1 At
At = A.transpose()
B = np.dot( np.invert( np.dot(At,A) ), At )
# ?
np.linalg.pinv