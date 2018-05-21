import numpy as np
import matplotlib.pyplot as plt


def two_scales(ax1, time, data1, data2,  c1, c2):
    ax2 = ax1.twinx()
    ax1.plot(time, data1, color=c1)
    ax1.set_xlabel('time (s)')
    ax1.set_ylabel('exp')

    ax2.plot(time, data2, color=c2)
    ax2.set_ylabel('sin', color=c2)
    return ax1, ax2

t = np.arange(0.01, 10.0, 0.01)
s1 = np.exp(t)
s2 = np.sin(2*np.pi*t)

fig, ax = plt.subplots()
ax1, ax2 = two_scales(ax, t, s1, s2, 'r', 'b')


# 刻度颜色
def color_y_axis(ax, color):
    for t in ax.get_yticklabels():
        t.set_color(color)
    return None

color_y_axis(ax1, 'r')
color_y_axis(ax2, 'b')
plt.show()
