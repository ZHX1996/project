# coding:'utf-8'
import pandas as pd
from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR

filename = 'F:/python data mining/chapter5/demo/data/bankloan.xls'
data = pd.read_excel(filename)

x = data.iloc[:, :8]
y = data.iloc[:, 8]
rlr = RLR()
rlr.fit(x.as_matrix(), y.as_matrix())
# 获取特征筛选结果
# print(rlr.get_support())

print('有效特征: %s' % ','.join(x.columns[rlr.get_support()]))
x = x[x.columns[rlr.get_support()]]

lr = LR()
lr.fit(x.as_matrix(), y.as_matrix())
print('模型的平均正确率: %s' % lr.score(x.as_matrix(), y.as_matrix()))
