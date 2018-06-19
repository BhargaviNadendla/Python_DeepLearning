import numpy as np
import matplotlib.pyplot as plt

x=np.array([0,1,2,3,4,5,6,7,8,9])                 # Reading input X as an array
y=np.array([1,3,2,5,7,8,8,9,10,12])              # Reading input Y as an array
xMean=np.mean(x)                               #Calculating the mean of x
yMean=np.mean(y)                               #Calculating the mean of y
B1=(np.sum((x-xMean)*(y-yMean)))/(np.sum(np.power((x-xMean),2)))           #Calculate the y intercept using the defined formula
B0=yMean-(B1*xMean)                             #Calculate the slope using the defined formula
plt.scatter(x,y)                                #plot x and y using matplotlib
ry=B1*x+B0                                      #Applying linear regression with the equation y=mx+c
plt.plot(x,ry)                                 #Plotting the linear regression model
plt.show()                                     #showing the plot