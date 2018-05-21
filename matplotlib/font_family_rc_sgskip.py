from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Verdana']
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3], label='test')
ax.plot([3, 2, 1], label='test1')
ax.plot([1, 3, 1, 2], label='test2')

ax.legend()
plt.show()