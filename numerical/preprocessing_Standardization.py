# -*- coding: utf-8 -*-
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
# max_abs_scaler = preprocessing.MaxAbsScaler()
# X_train_maxabs = max_abs_scaler.fit_transform(X_train)
# print(X_train_maxabs)

# 有异常值,根据中位数或四分位数中心化数据
# train2 = np.array([[1., -1., 0.],
#                   [16., 2., 0.],
#                   [0.5, 0., 1.]])
# robust = preprocessing.RobustScaler()
# train2_robust = robust.fit_transform(train2)
# print(train2_robust)

# 非线性转换，同样可以把每个特征放在同样的分布或范围里，并且受异常值的影响小
# 使不常见的分布变得平滑。  使用四分位函数把数据转换到0和1之间
# QuantileTransformer


# 正则化
# X_normalized = preprocessing.normalize(X_train, norm='l2')
# print(X_normalized)
# normalizer = preprocessing.Normalizer()
# print(normalizer.transform(X_train))

# 特征的二值化，将数值型转换成布尔型，默认按0，大于0则1，小于等于0则0，也可以自己设置threshold
# binarizer01 = preprocessing.Binarizer()
# X_train_bin01 = binarizer01.fit_transform(X_train)
# binarizer02 = preprocessing.Binarizer(threshold=1.5)
# X_train_bin02 = binarizer02.fit_transform(X_train)
# print(X_train_bin01)
# print(X_train_bin02)

# 为类别特征编码，可以用one-of-k编码或one-hot编码，都通过OneHotEncoder实现
# 特征1中有（0，1）两个值，特征2中有（0，1，2）三个值，特征3中有（0，1，2，3）四个值
# 所以编码之后有9个二元特征
# enc = preprocessing.OneHotEncoder()
# enc.fit([[0,0,3],[1,1,0],[0,2,1],[1,0,2]])
# enc_test = enc.transform([[0,1,3]]).toarray()
# print(enc_test)
# 传入参数指明每个特征中的值的总个数
# enc = preprocessing.OneHotEncoder(n_values=[2,3,4])

# 弥补缺失值, missing_values可以不止为NaN，可以为0等
# from sklearn.preprocessing import Imputer
# imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
# imp.fit([[1,2],[np.nan, 3], [7, 6]])
# x = [[np.nan, 2], [6, np.nan], [7, 6]]
# x_fillna = imp.transform((x))
# print(x_fillna)

# 多项式特征 非线性
# （x1,x2)->(1, x1, x2, x1^2, x1*x2, x2^2)第一列是bias
from sklearn.preprocessing import PolynomialFeatures
# x = np.arange(6).reshape(3,2)
# # 创建二次方的多项式
# poly = PolynomialFeatures(2)
# x_poly = poly.fit_transform(x)
# print(x_poly)

# 自定义只要保留特征相乘的项 （1，x1*x2,x1*x3,...)
# x = np.arange(9).reshape(3,3)
# poly = PolynomialFeatures(degree=3, interaction_only=True)
# x_poly = poly.fit_transform(x)

# 自定义特征的转换函数, 函数的输出值为特征
from sklearn.preprocessing import FunctionTransformer
transformer = FunctionTransformer(np.log1p)
x = np.array([[0,1],[2,3]])
x_functrans = transformer.transform(x)
print(x_functrans)

