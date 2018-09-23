import numpy as np
import matplotlib.pyplot as plt
import pandas as pd #the package "pandas" provides methods for loading and saving data to file 

# read in the data from "DataTask3.csv"
#df = ...
# YOUR CODE HERE
df = pd.read_csv('DataTask3.csv')
X = df.as_matrix() # convert the data frame to numpy matrix
print(X)



### STUDENT TASK ###
#Step 1: draw the scatter plot for data X
plt.figure(figsize=(8,8))
plt.scatter(X[:,0], X[:,1])
plt.show()

sample_matrix = [
    [1,1],
    [1,2],
    [1,3]
]

### STUDENT TASK ###
#Step 2: compute the sample covariance of data X
#C = ...
# np.cov expect 2-D array, of which rows are features, and columns are observation
# our data is the other way around so we'll need transpose it first
Xt = np.transpose(X)
cov = np.cov(Xt)
print(cov)
#Hint: C should be a 2x2 matrix. 

### STUDENT TASK ###
#Step 3: find eigenvalues and eigenvectors of C and print them
#values, vectors = ...
#print('eigenvalues= ', values)
#print('eigenvectors= ', vectors)
# YOUR CODE HERE
values, vectors = np.linalg.eig(cov)
print('eigenvalues= ', values)
print('eigenvectors= ', vectors)

### STUDENT TASK ###
#Step 4: plot each eigenvector as a line from [0,0] to the coordinate of the eigenvector
# YOUR CODE HERE
for v in vectors:
    x = [0, v[0]]
    y = [0, v[1]]
    plt.plot(x, y)

plt.xlim((-4, 4))
plt.ylim((-4, 4))

plt.legend()
plt.show()