import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19690801)
fig, ax = plt.subplots()
ax.plot(np.random.rand(20), '-o', ms=10, lw=2, alpha=0.7, mfc='orange')
ax.grid()

fig.text(0.95, 0.05, 'Property of MPL',
         fontsize=50, color='gray',
         ha='right', va='bottom', alpha=0.5)

plt.show()