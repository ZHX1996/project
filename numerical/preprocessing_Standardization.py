# http://scikit-learn.org/stable/modules/preprocessing.html#preprocessing
# https://blog.csdn.net/sinat_33761963/article/details/53433799
from sklearn import preprocessing
import numpy as np

X_train = np.array([[1.,-1.,2.],
                    [2.,0.,0.,],
                    [0.,1.,-1.]])
# 进行标准化
# X_scaled = preprocessing.scale(X_train)
# print(X_scaled)
# print(X_scaled.mean(axis=0))
# print(X_scaled.std(axis=0))

# 用训练数据生成一个模型，后面用同样的转换处理测试数据
# scalar = preprocessing.StandardScaler().fit(X_train)
# print(scalar.mean_)
# print(scalar.scale_)
# print(scalar.transform(X_train))
# X_test = [[-1.,1.,0.]]
# print(scalar.transform(X_test))

# 在给定值之间缩放特征，通常是0和1之间
'''
x_std = (x-x_min)/(x_max-x_min)
x_scaled = x_std/(x_max-x_min) + x_min
'''
# min_max_scaler = preprocessing.MinMaxScaler()
# X_train_minmax = min_max_scaler.fit_transform(X_train)
# print(X_train_minmax)
# # 查看换算器的属性
# print(min_max_scaler.scale_)
# print(min_max_scaler.min_)

# 在-1和1之间缩放特征
max_abs_scaler = preprocessing.MaxAbsScaler()
X_train_maxabs = max_abs_scaler.fit_transform(X_train)
print(X_train_maxabs)


