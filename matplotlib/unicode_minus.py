import numpy as np
import matplotlib
import matplotlib.pyplot as plt

np.random.seed(19680801)
matplotlib.rcParams['axes.unicode_minus'] = False
fig, ax = plt.subplots()
ax.plot(10*np.random.randn(100), 10*np.random.randn(100), '.')
ax.set_title('Using hypen instead of unicode minus')
plt.show()
