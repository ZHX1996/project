import matplotlib.pyplot as plt
from matplotlib import collections, colors, transforms
import numpy as np

nverts = 50
npts = 100

r = np.arange(nverts)
theta = np.linspace(0, 2*np.pi, nverts)
xx = r * np.sin(theta)
yy = r * np.cos(theta)
spiral = list(zip(xx, yy))

rs = np.random.RandomState(19680801)

xo = rs.randn(npts)
yo = rs.randn(npts)
xyo = list(zip(xo, yo))

colors = [colors.to_rgba(c)
          for c in plt.rcParams['axes.prop_cycle'].by_key()['color']]

fig, axes = plt.subplots(2, 2)
fig.subplots_adjust(top=0.92, left=0.07, right=0.97, hspace=0.3, wspace=0.3)
((ax1, ax2), (ax3, ax4)) = axes

col = collections.LineCollection([spiral], offsets=xyo, transOffset=ax1.transData)
trans = fig.dpi_scale_trans + transforms.Affine2D().scale(1.0/72.0)
col.set_transform(trans)
ax1.add_collection(col, autolim=True)
col.set_color(colors)
ax1.autoscale_view()
ax1.set_title('LineCollection using offsets')

col = collections.PolyCollection([spiral], offsets=xyo, transOffset=ax2.transData)
trans = transforms.Affine2D().scale(fig.dpi/72.0)
col.set_transform(trans)
ax2.add_collection(col, autolim=True)
col.set_color(colors)
ax2.autoscale_view()
ax2.set_title('PolyCollection using offsets')

col = collections.RegularPolyCollection(7, sizes=np.abs(xx) * 10.0, offsets=xyo, transOffset=ax3.transData)
trans = transforms.Affine2D().scale(fig.dpi/72.0)
col.set_transform(trans)
ax3.add_collection(col, autolim=True)
col.set_color(colors)
ax3.autoscale_view()
ax3.set_title('RegularPolyCollection using offsets')

nverts = 60
ncurves = 20
offs = (0.1, 0.0)

yy = np.linspace(0, 2*np.pi, nverts)
ym = np.max(yy)
xx = (0.2 + (ym -yy)**2 * np.cos(yy-0.4)*0.5)
segs = []
for i in range(ncurves):
    xxx = xx + 0.02*rs.randn(nverts)
    curve = list(zip(xxx, yy*100))
    segs.append(curve)

col = collections.LineCollection(segs, offsets = offs)
ax4.add_collection(col, autolim=True)
col.set_color(colors)
ax4.autoscale_view()
ax4.set_title('Successive data offsets')
ax4.set_xlabel('Zonal velocity component (m/s)')
ax4.set_ylabel('Depth(m)')
ax4.set_ylim(ax4.get_ylim()[::-1])

plt.show()
