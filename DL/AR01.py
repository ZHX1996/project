from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.tsa.arima_model import ARMA
from statsmodels.tsa.stattools import adfuller
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

origindata = pd.Series([24,27,24,26,26,28,26,26,27,26,25,26,26,25, 26,27,26,26,25,25,25,25,27,25])  # 24
np.random.seed(1231)
noise1 = np.random.randn(24)
data1 = origindata+noise1
np.random.seed(1232)
noise2 = np.random.randn(24)
data2 = origindata+noise2
np.random.seed(1233)
noise3 = np.random.randn(24)
data3 = origindata+noise3
np.random.seed(1234)
noise4 = np.random.randn(24)
data4 = origindata+noise4

print(data4[14:].tolist())

# for i in range(10):
#     AR1 = ARMA(data1[i:i+14], order=(1, 0)).fit(disp=-1)
#     predict1 = AR1.predict(start=0, end=0)
#     AR2 = ARMA(data2[i:i+14], order=(1, 0)).fit(disp=-1)
#     predict2 = AR2.predict(start=0, end=0)
#     AR3 = ARMA(data3[i:i+14], order=(1, 0)).fit(disp=-1)
#     predict3 = AR3.predict(start=0, end=0)
#     AR4 = ARMA(data4[i:i+14], order=(1, 0)).fit(disp=-1)
#     predict4 = AR4.predict(start=0, end=0)
#
#     var1 = (data1[i+14]**2-predict1*data1[i+14])/2
#     var2 = (data2[i+14]**2-predict2*data2[i+14])/2
#     var3 = (data3[i+14]**2-predict3*data3[i+14])/2
#     var4 = (data4[i+14]**2-predict4*data4[i+14])/2
#
#     w1 = 1/((1/(var1**2)+1/(var2**2)+1/(var3**2)+1/(var4**2))* (var1**2))
#     w2 = 1/((1/(var1**2)+1/(var2**2)+1/(var3**2)+1/(var4**2))* (var2**2))
#     w3 = 1/((1/(var1**2)+1/(var2**2)+1/(var3**2)+1/(var4**2))* (var3**2))
#     w4 = 1/((1/(var1**2)+1/(var2**2)+1/(var3**2)+1/(var4**2))* (var4**2))
#
#     temp = w1*data1[i+14]+w2*data2[i+14]+w3*data3[i+14]+w4*data4[i+14]
    # print(round(temp, 3))




# x = np.arange(0, 14, 1)
# plt.plot(x, data1, label='data1', linewidth=2, color='k', marker='o')
# plt.plot(x, data2, label='data2', linewidth=2, color='k', marker='*')
# plt.plot(x, data3, label='data3', linewidth=2, color='k', marker='+')
# plt.plot(x, data4, label='data4', linewidth=2, color='k', marker='s')

# x = np.arange(0, 10, 1)
# plt.plot(x, origindata[14:], label='origindata', linewidth=2, color='k', marker='o')
# plt.plot(x, res, label='aggregation', linewidth=2, color='k', marker='o')
# plt.xlabel('time')
# plt.ylabel('temperature')
# plt.title('origin data')
# plt.ylim(15, 40)
# plt.legend()
# plt.show()

# plot_acf(data).show()

# data.plot()
# plt.title(u'origin data')
# plt.ylim(15, 40)
# plt.show()

# s = ADF(data)
# print(s[1])
# # diff_data = data.diff().dropna()
# data = pd.Series(list(map(math.log, data)))
# print(data)
# print(acorr_ljungbox(data, lags=1))

# adftest = adfuller(data, autolag='AIC')
# adf_res = pd.Series(adftest[0:4], index=['Test Statistic', 'p-value', 'Lags Used', 'Number of Observations Used'])
# for key, value in adftest[4].items():
#     adf_res['Critical Value (%s)' % key] = value
# lag = int(adf_res['Lags Used'])
# pvalue = int(adf_res['p-value'])
