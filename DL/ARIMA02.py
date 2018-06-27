from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.stattools import adfuller as ADF
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.tsa.arima_model import ARIMA
import pandas as pd
import matplotlib.pyplot as plt

# data = pd.read_excel("C:/Users/Administrator/Desktop/1.xlsx", index_col=u'时间')
data = pd.Series([22.5,23.2,22.9,24.1,23.7,23.4,24.2,22.5,23.2,22.9,23.4,24.2,22.5,23.2])  # 14个
data1 = data
forecast = 2


# plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文
# plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号
# # data.plot()
# # plt.title(u'时序图')
# # plt.ylim(20, 30)
# # plt.show()
#
plot_acf(data).show()
# print(u'原始序列的ADF检验结果为:', ADF(data))
i = 0
while True:
    s = ADF(data)
    print(s[1])
    if s[1] > 0.05:
        data = data.diff().dropna()
        i += 1
    else:
        break
print(i)
print(acorr_ljungbox(data, lags=1))

pmax = int(len(data)/10)
qmax = int(len(data)/10)
bic_matrix = []
for p in range(pmax+1):
    tmp = []
    for q in range(qmax+1):
        try:
            tmp.append(ARIMA(data1, (p,i,q)).fit().bic)
        except:
            tmp.append(None)
    bic_matrix.append(tmp)

bic_matrix = pd.DataFrame(bic_matrix)
p, q = bic_matrix.stack().idxmin()
print(p, q)