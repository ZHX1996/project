from matplotlib import pyplot as plt
import numpy as np

fig= plt.figure()
ax1 = plt.subplot(221)
ax2 = plt.subplot(222)
ax3 = plt.subplot(223)
ax4 = plt.subplot(224)

N = 1000
x = np.random.randn(N)
y = np.random.randn(N)
ax1.scatter(x, y, s=5)

color = ['r', 'y', 'k', 'g', 'm']
ax2.scatter(x, y, s=5, c=color, marker='>')

ax3.scatter(x, y, s=5, alpha=0.5)

ax4.scatter(x, y, s=5, alpha=0.5, edgecolors='white')
plt.show()