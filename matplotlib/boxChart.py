from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

plt.style.use("ggplot")
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif']=['SimHei']

df = pd.DataFrame()
df["英语"]=[76,90,97,71,70,93,86,83,78,85,81]
df["经济数学"]=[65,95,51,74,78,63,91,82,75,71,55]
df["西方经济学"]=[93,81,76,88,66,79,83,92,78,86,78]
df["计算机应用基础"]=[85,78,81,95,70,67,82,72,80,81,77]

plt.boxplot(x=df.values, labels=df.columns, whis=1.5)
plt.show()