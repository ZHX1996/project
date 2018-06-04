#-*-coding:utf-8-*-
import pandas as pd
from random import shuffle

datafile = '/home/zhx/PycharmProjects/others/chapter6/model.xls'
data = pd.read_excel(datafile)
data = data.as_matrix()
shuffle(data)

p = 0.8
train = data[:int(len(data)*p), :]
test = data[int(len(data)*p):, :]


from keras.models import Sequential  # 神经网络初始化函数
from keras.layers.core import Dense, Activation  # 神经网络层函数，激活函数
netfile = '/home/zhx/PycharmProjects/others/chapter6/net.model'
# 建立神经网络
net = Sequential()
# 输入层(3节点)到隐藏层(10节点)的连接
net.add(Dense(10, input_dim=3))
net.add(Activation('relu'))
# 隐藏层到输出层
net.add(Dense(1))
net.add(Activation('sigmoid'))
# net.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# net.fit(train[:, :3], train[:, 3], epochs=1000, batch_size=1)
# 保存模型
# net.save_weights(netfile)
# 预测结果变形
# predict是预测概率 predict_classes是预测类别
# predict_result = net.predict_classes(train[:, :3]).reshape(len(train))

from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib

treefile = '/home/zhx/PycharmProjects/others/chapter6/tree.pkl'
# tree = DecisionTreeClassifier()
# tree.fit(train[:, :3], train[:, 3])
# joblib.dump(tree, treefile)

net.load_weights(netfile, by_name=True)
tree = joblib.load(treefile)

# 混淆矩阵
# from confusionMatrixVisualization import *
# cm_plot(train[:, 3], predict_result).show()
# cm_plot(train[:, 3], tree.predict(train[:, :3])).show()

# ROC曲线，越靠近左上越好
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve

predict_result = net.predict(test[:, :3]).reshape(len(test))
fpr, tpr, thresholds = roc_curve(test[:, 3], predict_result, pos_label=1)
plt.subplot(2,1,1)
plt.plot(fpr, tpr, linewidth=2, label='ROC OF LM')
plt.xlabel('False Positive Rate')
plt.ylabel('True Position Rate')
plt.ylim(0, 1.05)
plt.xlim(0, 1.05)
plt.legend(loc=4)

fpr1, tpr1, thresholds1 = roc_curve(test[:, 3], tree.predict_proba(test[:, :3])[:, 1], pos_label=1)
plt.subplot(2,1,2)
plt.plot(fpr1, tpr1, linewidth=2, label='ROC of CART')
plt.xlabel('False Positive Rate')
plt.ylabel('True Position Rate')
plt.ylim(0, 1.05)
plt.xlim(0, 1.05)
plt.legend(loc=4)

plt.show()

