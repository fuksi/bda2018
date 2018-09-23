#Important libraries to import:
# NumPy: is the fundamental package for scientific computing with Python.
# matplotlib.pyplot: provides a MATLAB-like plotting framework.

import matplotlib.pyplot as plt #define shorthand "plt" for package matlobplit.pyplot
import numpy as np #define shorthand "np" for the numpy package 

def example_func(x):
    f_x = 1/(1+np.exp(-x))
    return f_x

range_x = np.arange(-6 , 6 , 0.01)

f_x = np.empty(len(range_x))

for i in range(len(range_x)):
    f_x[i] = example_func(range_x[i])

### STUDENT TASK ###
#1) plot the results, for example use plot function in matplotlib.pyplot. Remember to show() the plot.
plt.plot(range_x, f_x)
plt.show()
### STUDENT TASK ###
#2) find the first derivative of the mentioned function and plot it
# YOUR CODE HERE
def example_func_derivative(x):
    fx = np.exp(-x) / (np.exp(-x) + 1)**2
    return fx

f_x_d = np.empty(len(range_x))

for i in range(len(range_x)):
    f_x_d[i] = example_func_derivative(range_x[i])

plt.plot(range_x, f_x_d)
plt.show()