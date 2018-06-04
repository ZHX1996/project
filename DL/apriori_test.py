import pandas as pd
from apriori import find_rule
from apyori import apriori

inputfile = 'F:/python data mining/chapter5/demo/data/menu_orders.xls'
outputfile = 'C:/Users/Administrator/Desktop/apriori.xls'

data = pd.read_excel(inputfile, header=None)
# 转换原始数据至0-1矩阵
ct = lambda x: pd.Series(1, index=x[pd.notnull(x)])
b = map(ct, data.as_matrix())
data = pd.DataFrame(list(b)).fillna(0)
del b

support = 0.2
confidence = 0.5
ms = '--'
# find_rule(data, support, confidence, ms).to_excel(outputfile)
result = list(apriori(data, support, confidence))
print(result)