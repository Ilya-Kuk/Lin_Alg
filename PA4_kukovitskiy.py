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

# Creating matrix for fitting linear regression y = Cx + D
print('The corresponding Matrix representation is\n  [x 1] v = y\n  [x 1 | y],\n v = (C D).transpose')
print('Calling this matrix\n [A | y], \n note that A is inconsistent, since there are many rows and 2 columns. Not all y are in C(A). So we project y onto C(A).\nTo compute the corresponding v^ of the projection:\nv^ = (A.transpose A).inverse A.transpose y .')
# converting dataset to matrix B w.r.t.(x y) for matrix manipulations
B = dataset.values
B = np.asmatrix(B)
x = B[:,0]

# Creating Matrix A w.r.t. (C D):
A = np.column_stack((X,np.ones(len(X))))

# Creating pseudo-inverse (At A)-1 At
At = A.transpose()
ps_inv = np.linalg.inv( At @ A ) @ At

np_inv = np.linalg.pinv(A) # the Numpy command for the pseudo-inverse

# multiply pseudo-inverse by "b", our 'after' data points
# to get our V-hat, the vector of our coefficients for the regression line
# y = C+Dx
V_h = np_inv.dot(Y)

## Recording V_h for later use
Q1_V_h = V_h

# V_h = [C, D]
C_fit = V_h[0]
D_fit = V_h[1]

print('The linear equation for line of best fit is y=',C_fit,'x + ',D_fit,'.')

# Plot the regression line with the data
plt.plot(X,C_fit*X+D_fit,'k') # plot (x,C+Dx) line in 'k' - black
plt.scatter(X, Y)
plt.title('Heart Rates')
plt.xlabel('before')
plt.ylabel('after')

# calculate residual/errors = predicted y - measured y_i
e = (C_fit*X+D_fit)-Y

# make new plot of residual errors
plt.figure(2)
plt.plot(X,e,'or') # 'or' means red circles 
plt.grid(True)
plt.title('Plot of Residuals')
plt.xlabel('Before')
plt.ylabel('difference between measured and predicted After')

# Use regression line to "predict" a Heart weight given a Body weight
x = 82
print('If before heart rate is',x,'bpm, the model predicts the after heart rate to be',round(C_fit*x+D_fit,0),'bpm.')


#####  2  #######

# Importing Data
dataset = pd.read_csv('revisedHR.csv')

# Printing shape of data
print('The shape of the data is:',dataset.shape,'.')

# Visualising the data
X = dataset.before
Y = dataset.after

plt.figure(3)
plt.scatter(X, Y)
plt.title('Heart Rates')
plt.xlabel('before')
plt.ylabel('after')

# Creating matrix for fitting linear regression y = Cx + D
print('The corresponding Matrix representation is\n  [x 1] v = y\n  [x 1 | y],\n v = (C D).transpose')
print('Calling this matrix\n [A | y], \n note that A is inconsistent, since there are many rows and 2 columns. Not all y are in C(A). So we project y onto C(A).\nTo compute the corresponding v^ of the projection:\nv^ = (A.transpose A).inverse A.transpose y .')
# converting dataset to matrix B w.r.t.(x y) for matrix manipulations
B = dataset.values
B = np.asmatrix(B)
x = B[:,0]
# Creating Matrix A w.r.t. (C D):
A = np.column_stack((X,np.ones(len(X))))
# Creating pseudo-inverse (At A)-1 At
np_inv = np.linalg.pinv(A) # the Numpy command for the pseudo-inverse
# multiply pseudo-inverse by "b", our 'after' data points
# to get our V-hat, the vector of our coefficients for the regression line
# y = C+Dx
V_h = np_inv.dot(Y)
# V_h = [C, D]
C_fit = V_h[0]
D_fit = V_h[1]
print('The linear equation for line of best fit is y=',C_fit,'x + ',D_fit,'.')

# Plot the regression line with the data
plt.plot(X,C_fit*X+D_fit,'k') # plot (x,C+Dx) line in 'k' - black
plt.scatter(X, Y)
plt.title('Heart Rates')
plt.xlabel('before')
plt.ylabel('after')

# calculate residual/errors = predicted y - measured y_i
e = (C_fit*X+D_fit)-Y

# make new plot of residual errors
plt.figure(4)
plt.plot(X,e,'or') # 'or' means red circles 
plt.grid(True)
plt.title('Plot of Residuals')
plt.xlabel('Before')
plt.ylabel('difference between measured and predicted After')

# Use regression line to "predict" a Heart weight given a Body weight
x = 82
print('If before heart rate is',x,'bpm, the model predicts the after heart rate to be',round(C_fit*x+D_fit,0),'bpm.')

# Comparing least squares solutions from data with and without outlier removed.

print('The first (black) least squares line was:\n  y = ',Q1_V_h[0],'*x +',Q1_V_h[1])
print('The second (blue) least squares line was:\n  y = ',C_fit,'*x +',D_fit)

plt.plot(X,Q1_V_h[0]*X+Q1_V_h[1],'k') # plot Q1 line in 'k' - black
plt.plot(X,C_fit*X+D_fit,'b') # plot Q2 line in 'b' - blue

print('The error value for the outlier removed was very high from the best fit without the outlier. Thus the square error is significant in adjusting the lines. The second line is much closer to the line y=x than the first.')


#####  3  #######

# Importing Data
dataset = pd.read_csv('SpeedMileage.csv')

# Printing shape of data
print('The shape of the data is:',dataset.shape,'.')

# Printing first 10 rows of data
print('The first 10 rows in the data are:\n',dataset.head(10) )

# Visualising the data
X = dataset.Speed
Y = dataset.Mileage

plt.figure(5)
plt.scatter(X, Y)
plt.title('Car Speeds and Mileage')
plt.xlabel('Speed')
plt.ylabel('Mileage')

## Finding line of best fit by least squares approximation:

# Creating matrix for fitting polynomial regression y = Cx + D
print('The corresponding Matrix representation is\n  [x 1] v = y\n  [x^2 x 1 | y],\n v = (C D).transpose')
print('Calling this matrix\n [A | y], \n note that A is inconsistent, since there are many rows and 2 columns. Not all y are in C(A). So we project y onto C(A).\nTo compute the corresponding v^ of the projection:\nv^ = (A.transpose A).inverse A.transpose y .')
# converting dataset to matrix B w.r.t.(x y) for matrix manipulations
B = dataset.values
B = np.asmatrix(B)
x = B[:,0]
# Creating Matrix A w.r.t. (C D):
A = np.column_stack((X,np.ones(len(X))))
# Creating pseudo-inverse (At A)-1 At
np_inv = np.linalg.pinv(A) # the Numpy command for the pseudo-inverse
# multiply pseudo-inverse by "b", our 'after' data points
# to get our V-hat, the vector of our coefficients for the regression line
# y = C+Dx
V_h = np_inv.dot(Y)
# V_h = [C, D]
C_fit = V_h[0]
D_fit = V_h[1]
print('The linear equation for line of best fit is y=',C_fit,'x + ',D_fit,'.')

# Plot the regression line with the data
plt.plot(x,C_fit*x+D_fit,'k') # plot (x,C+Dx) line in 'k' - black
plt.scatter(X, Y)
plt.title('Car Speeds and Mileage')
plt.xlabel('Speed')
plt.ylabel('Mileage')

# calculate residual/errors = predicted y - measured y_i
e = (C_fit*X+D_fit)-Y

# make new plot of residual errors
plt.figure(6)
plt.plot(X,e,'or') # 'or' means red circles 
plt.grid(True)
plt.title('Plot of Residuals')
plt.xlabel('Speed')
plt.ylabel('difference between measured and predicted Mileage')

print('This looks like a parabola. Maybe a parabolic term would be useful here...')

# Use regression line to "predict" a mileage from a given speed.
x = 80
print('If speed is',x,', the model predicts the mileage to be',round(C_fit*x+D_fit,0),'. This is not reflected in the data.')

## Using least-squares method to find parabola of best fit.

# Creating matrix for fitting polynomial regression y = Cx^2 + Dx + E
print('The corresponding Matrix representation is\n  [x^2 x 1] v = y\n  [x^2 x 1 | y],\n v = (C D E).transpose')
print('Calling this matrix\n [A | y], \n note that A is inconsistent, since there are many rows and 3 columns. Not all y are in C(A). So we project y onto C(A).\nTo compute the corresponding v^ of the projection:\nv^ = (A.transpose A).inverse A.transpose y .')

# converting dataset to matrix B w.r.t.(x y) for matrix manipulations
B = dataset.values
B = np.asmatrix(B)
x = B[:,0]

# Creating Matrix A w.r.t. (C D E):
A = np.column_stack((X,np.ones(len(X))))
A = np.column_stack((X**2,A))
# Creating pseudo-inverse (At A)-1 At
np_inv = np.linalg.pinv(A) # the Numpy command for the pseudo-inverse
# multiply pseudo-inverse by "b", our 'after' data points
# to get our V-hat, the vector of our coefficients for the regression line
# y = C+Dx
V_h = np_inv.dot(Y)
# V_h = [C, D]
C_fit = V_h[0]
D_fit = V_h[1]
E_fit = V_h[2]

print('The linear equation for line of best fit is y=',C_fit,'x^2 + ',D_fit,'x +',E_fit,'.')

# Plot the approximation with the data
plt.plot(X,C_fit*X**2+D_fit*X+E_fit,'k')
plt.scatter(X, Y)
plt.title('Car Speeds and Mileage')
plt.xlabel('Speed')
plt.ylabel('Mileage')

# calculate residual/errors = predicted y - measured y_i
e = (C_fit*X**2+D_fit*X+E_fit)-Y

# make new plot of residual errors
plt.figure(7)
plt.plot(X,e,'or') # 'or' means red circles 
plt.grid(True)
plt.title('Plot of Residuals')
plt.xlabel('Before')
plt.ylabel('difference between measured and predicted Mileage')

# Use quadratic model to predict mileage given speed
x = 80
print('If speed is',x,', the model predicts the mileage to be',round(C_fit*x**2+D_fit*x+E_fit,0),'.')