import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def func_logx(x):
    return np.log(x) 

rangex = np.arange(0, 20, 1)
count = len(rangex) 

logx = np.empty(count)

for i in range(count):
    logx[i] = func_logx(rangex[i])

plt.plot(rangex, rangex)
plt.plot(rangex, logx)

plt.show()
