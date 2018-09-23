# import pandas as pd #the package "pandas" provides methods for loading and saving data to file 
# import matplotlib.pyplot as plt #define shorthand "plt" for package matlobplit.pyplot
# import numpy as np #define shorthand "np" for the numpy package 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Data.csv')
data = df.as_matrix()

N, D = data.shape
print('sample size N=', N)
print('feature length d=', D)

y = data[:,1]
x = data[:,0]
plt.scatter(y, x)
plt.show()

first = data[:200,:]
second = data[200:400,:]
third = data[400:,:]

plt.scatter(first[:,1], first[:,0], c='#ED1C24')
plt.scatter(second[:,1], second[:,0], c='#377A6C')
plt.scatter(third[:,1], third[:,0], c='#0072BC')
plt.show()

plt.hist(data[:,0])
plt.show()

print(data)
