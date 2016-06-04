# Triangle Exercise from Cyrus
# 2.5 hours
# January 30, 2016

import numpy as np               # Numpy: processes large multi-D arrays
import matplotlib.pyplot as plt  # Pyplot: provides MATLAB-like plotting framework
import random

# Constant (tuples)
INIT = (5,5)                     
A = (0,0)
B = (5,10)
C = (10,0)

# Draw Initial Triangle
plt.plot([0,5], [0,10], linestyle="-", color='b')
plt.plot([5,10], [10,0], linestyle="-", color='b')
plt.plot(INIT[0], INIT[1], '.b')
plt.title('Median Triangle')
plt.show()

def find_median(a, b):
    x = (b[0] + a[0])/2.0
    y = (b[1] + a[1])/2.0
    return (x,y)

nextpoint = INIT
for i in range(10):
    vertex = random.choice([A,B,C])
    med = find_median(nextpoint, vertex)
    plt.plot(med[0], med[1], '.b')
    nextpoint = med             