# coding:'utf-8'
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

inputfile = 'F:/python data mining/chapter5/demo/data/consumption_data.xls'
outputfile = 'C:/Users/Administrator/Desktop/data_type.xls'


def kmeans():
    k = 3  # 聚类的类别
    iteration = 500
    data = pd.read_excel(inputfile, index_col='Id')
    data_zs = 1.0*(data-data.mean())/data.std()  # 标准化
    model = KMeans(n_clusters=k, n_jobs=2, max_iter=iteration)  # 并发数
    model.fit(data_zs)

    r1 = pd.Series(model.labels_).value_counts()  # 统计各个类别的数目
    r2 = pd.DataFrame(model.cluster_centers_)  # 找出聚类中心
    r = pd.concat([r2, r1], axis=1)  # 横向连接，得到聚类中心对应的类别下的数目
    r.columns = list(data.columns) + [u'类别数目']  # 重命名表头
    # 对数据进行了标准化，所以在0附近
    print(r)
    #
    # tsne = TSNE()
    # tsne.fit_transform(data_zs)
    # tsne = pd.DataFrame(tsne.embedding_, index = data.index)
    # print(tsne)
    # plt.rcParams['font.sans-serif'] = ['SimHei']
    # plt.rcParams['axes.unicode_minus'] = False
    # d = tsne[r['聚类类别'] == 0]
    # plt.plot(d[0], d[1], 'r.')
    # d = tsne[r['聚类类别'] == 1]
    # plt.plot(d[0], d[1], 'go')
    # d = tsne[r['聚类类别'] == 2]
    # plt.plot(d[0], d[1], 'b*')
    # plt.show()

    # r = pd.concat([data, pd.Series(model.labels_, index = data.index)], axis=1)
    # r.columns = list(data.columns) + [u'聚类类别']
    # r.to_excel(outputfile)

if __name__ == '__main__':
    kmeans()
