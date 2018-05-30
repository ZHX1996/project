# coding:'utf-8'
import pandas as pd
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO

filename = 'F:/python data mining/chapter5/demo/data/sales_data.xls'
data = pd.read_excel(filename, index_col=u'序号')
# print(data.values)
data[data==u'好'] = 1
data[data==u'是'] = 1
data[data==u'高'] = 1
data[data != 1] = -1
# print(data.values)
x = data.iloc[:, :3].as_matrix().astype(int)
x1 = data.iloc[:, :3]
y = data.iloc[:, 3].as_matrix().astype(int)
# print(x, type(x))
dtc = DTC(criterion='entropy')
dtc.fit(x, y)

result = dtc.predict([[-1, 1, 1]])
print(result)

# with open("tree.dot", 'w') as f:
#     f = export_graphviz(dtc, feature_names=x1.columns, out_file=f)