import numpy as np
import matplotlib.pyplot as plt

N = 37
x, y = np.mgrid[:N, :N]
Z = (np.cos(x*0.2) + np.sin(y*0.3))

Zpos = np.ma.masked_less(Z, 0)
Zneg = np.ma.masked_greater(Z, 0)

fig, (ax1, ax2) = plt.subplots(figsize=(8, 3), ncols=2)

pos = ax1.imshow(Zpos, cmap='Blues', interpolation='none')
fig.colorbar(pos, ax=ax1)

neg = ax2.imshow(Zneg, cmap='Reds_r', interpolation='none')
fig.colorbar(neg, ax=ax2)

plt.show()
