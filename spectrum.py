import numpy as np
import matplotlib.pyplot as plt


# xmin = 10
# xmax = 20000
# ymin = -1.0
# ymax = 1.0
locs = [10, 100, 200, 500, 1000, 2000, 3000, 5000, 10000, 20000]
labels = ['10', '100', '200', '500', '1k', '2k', '3k', '5k', '10k', '20k']

ting = plt.axis(xmin=10, xmax=20000, ymin=-1.0, ymax=1.0)
plt.xscale('log')
plt.xticks(locs, labels)
plt.show()
