from matplotlib import pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['KaiTi']
mpl.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(6, 9))
labels = ['体育', '策略', '动作', '射击', '其它']
sizes = [27500, 11500, 6000, 3500, 1500]
colors = ['red', 'yellow', 'green', 'pink', 'gray']
explode = (0.03, 0.05, 0.05, 0.05, 0.05)

patches, l_text, p_text = plt.pie(sizes, explode = explode, labels = labels,
                                  colors = colors, labeldistance = 1.1,
                                  autopct='%3.2f%%', shadow = False,
                                  startangle=90, pctdistance=0.6)
for t in l_text:
    t.set_size(10)
for t in p_text:
    t.set_size(10)
plt.axis('equal')
plt.legend()
plt.show()