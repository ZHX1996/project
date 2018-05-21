from matplotlib import pyplot as plt
import numpy as np

fig = plt.figure(1)
ax1 = plt.subplot(121)
ax2 = plt.subplot(122)

sampleNo = 1000
mu = 3
sigma = 0.1
np.random.seed(0)
s = np.random.normal(mu, sigma, sampleNo)
plt.hist(s, 5, color='lightblue')

plt.hist(s, color='lightblue')
plt.show()