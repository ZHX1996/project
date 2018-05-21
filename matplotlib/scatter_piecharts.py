import math
import numpy as np
import matplotlib.pyplot as plt

#define the ratios
r1 = 0.2
r2 = r1 + 0.4
#define some sizes of the scatter marker
sizes = [60, 80, 120]

x = [0] + np.cos(np.linspace(0, 2*math.pi*r1, 10)).tolist()
y = [0] + np.sin(np.linspace(0, 2*math.pi*r1, 10)).tolist()
xy1 = list(zip(x, y))
s1 = max(max(x), max(y))

x = [0] + np.cos(np.linspace(2*math.pi*r1, 2*math.pi*r2, 10)).tolist()
y = [0] + np.sin(np.linspace(2*math.pi*r1, 2*math.pi*r2, 10)).tolist()
xy2 = list(zip(x, y))
s2 = max(max(x), max(y))

x = [0] + np.cos(np.linspace(2*math.pi*r2, 2*math.pi, 10)).tolist()
y = [0] + np.sin(np.linspace(2*math.pi*r2, 2*math.pi, 10)).tolist()
xy3 = list(zip(x, y))
s3 = max(max(x), max(y))

fig, ax = plt.subplots()
ax.scatter(np.arange(3), np.arange(3), marker=(xy1, 0),
           s=[s1*s1*_ for _ in sizes], facecolor='blue')
ax.scatter(np.arange(3), np.arange(3), marker=(xy2, 0),
           s=[s2*s2*_ for _ in sizes], facecolor='green')
ax.scatter(np.arange(3), np.arange(3), marker=(xy3, 0),
           s=[s3*s3*_ for _ in sizes], facecolor='red')

plt.show()