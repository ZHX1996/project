from matplotlib import pyplot as plt
import numpy as np

fig = plt.figure(1)
ax1 = plt.subplot(211)
data = np.array([15, 20, 18, 25])
width = 0.3
x_bar = np.arange(4)
rect = ax1.bar(x_bar, data, width, color='lightblue')

for rec in rect:
    x = rec.get_x()
    width = rec.get_width()
    height = rec.get_height()
    ax1.text(x+width/2., 1.02*height, str(height), ha='center', va='bottom')

ax1.set_xticks(x_bar)
ax1.set_xticklabels(('first', 'second', 'third', 'fourth'))
ax1.set_ylabel('sales')
ax1.set_title('the sales in 2018')
ax1.grid(True)
ax1.set_ylim(0, 28)

ax2 = plt.subplot(212)
rect2 = plt.barh(x_bar, data,  height=0.3, color = 'lightblue')
for rec in rect2:
    x = rec.get_x()
    y = rec.get_y()
    height = rec.get_height()
    width = rec.get_width()
    ax2.text(width + 0.3, y, str(width), va='bottom')
plt.show()