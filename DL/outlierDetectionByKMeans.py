#-*-coding:utf-8-*-
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def detection():
    inputfile = '/home/zhx/PycharmProjects/others/chapter5/data/consumption_data.xls'
    k = 3
    threshold = 2
    iteration = 500
    data = pd.read_excel(inputfile, index_col='Id')
    data_zs = 1.0*(data-data.mean())/data.std()

    model = KMeans(n_clusters=k, n_jobs=2, max_iter=iteration)
    model.fit(data_zs)
    # 标准化数据及其类别
    r = pd.concat([data_zs, pd.Series(model.labels_, index = data.index)], axis=1)
    r.columns = list(data.columns) + [u'聚类类别']

    norm = []
    for i in range(k):
        norm_tmp = r[['R', 'F', 'M']][r[u'聚类类别'] == i]-model.cluster_centers_[i]
        norm_tmp = norm_tmp.apply(np.linalg.norm, axis=1)
        norm.append(norm_tmp/norm_tmp.median())

    norm = pd.concat(norm)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    norm[norm <= threshold].plot(style='go')
    discrete_points = norm[norm > threshold]
    discrete_points.plot(style='r*')

    for i in range(len(discrete_points)):
        id = discrete_points.index[i]
        n = discrete_points.iloc[i]
        plt.annotate('(%s, %0.2f)' % (id, n), xy=(id, n), xytext=(id, n))
    plt.xlabel(u'编号')
    plt.ylabel(u'相对距离')
    plt.show()

if __name__ == '__main__':
    detection()