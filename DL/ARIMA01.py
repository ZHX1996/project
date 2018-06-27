# -*-coding:utf-8-*-

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.stattools import adfuller as ADF
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.tsa.arima_model import ARIMA

discfile = 'C:/Users/Administrator/Desktop/chapter5/data/arima_data.xls'
forecastnum = 5
data = pd.read_excel(discfile, index_col=u'日期')

# 时序图
plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号
data.plot()
plt.title(u'时序图')
plt.show()

# 自相关图
plot_acf(data).show()

# 平稳性检测
# adf, pvalue, usedlag, nobs, critical values, icbest, regresults, resstore
print(u'原始序列的ADF检验结果为:', ADF(data[u'销量']))

# 差分后的结果
D_data = data.diff().dropna()
D_data.columns = [u'销量差分']
D_data.plot()
plt.show()
plot_acf(D_data).show()
plot_pacf(D_data).show()
# 单位根检验
print(u'差分序列的ADF检验结果为:', ADF(D_data[u'销量差分']))
# 白噪声检验
# 返回统计量和p值
# print(u'差分序列的白噪声检验结果为:', acorr_ljungbox(D_data, lags=1))

# 定阶 一般阶数不超过length/10
# pmax = int(len(D_data)/10)
# qmax = int(len(D_data)/10)
# bic_matrix = []
# for p in range(pmax+1):
#     tmp = []
#     for q in range(qmax+1):
#         try:
#             tmp.append(ARIMA(data, (p,1,q)).fit().bic)
#         except:
#             tmp.append(None)
#     bic_matrix.append(tmp)
#
# bic_matrix = pd.DataFrame(bic_matrix)
# p, q = bic_matrix.stack().idxmin()  # 先用stack展开。再用idxmin找出最小值的位置
# print(u'BIC最小的p值和q值为: %s, %s' % (p, q))
# model = ARIMA(data, (p,1,q)).fit()  # 建立ARIMA(0,1,1)模型
# model.summary2()  # 给出一份模型报告
# model.forecast(5)  # 作出为期5天的预测。返回预测结果，标准误差，置信区间