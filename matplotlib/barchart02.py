import numpy as np
from matplotlib import pyplot as plt

fig = plt.figure(1)
ax = plt.subplot(111)
index = np.arange(4)
sales_BJ = [52, 55, 63, 53]
sales_SH = [44, 66, 55, 41]
width = 0.3
rect1 = plt.bar(index, sales_BJ, width, color='lightblue')
for rec in rect1:
    width = rec.get_width()
    height = rec.get_height()
    x = rec.get_x()
    ax.text(x+width/6., height*0.9, str(height))
rect2 = plt.bar(index, sales_SH, width, color='gray', bottom=sales_BJ)
plt.show()