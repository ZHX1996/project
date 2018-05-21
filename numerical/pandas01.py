# https://blog.csdn.net/sailist/article/details/80045374
import numpy as np
import pandas as pd

# 导入文件
# df = pd.DataFrame(pd.read_csv('name.csv', header=1))
# df = pd.DataFrame(pd.read_excel('name.xlsx'))

df = pd.DataFrame({"id":[1001,1002,1003,1004,1005,1006],
 "date":pd.date_range('20130102', periods=6),
  "city":['Beijing ', 'SH', ' guangzhou ', 'Shenzhen', 'shanghai', 'Beijing '],
 "age":[23, 44, 54, 32, 34, 32],
 "category":['100-A', '100-B', '110-A', '110-C', '210-A', '130-F'],
  "price":[1200, np.nan, 2133, 5433, np.nan, 4432]},
  columns =['id', 'date', 'city', 'category', 'age', 'price'])

#数据表信息查看
# 维度查看
# print(df.shape)
# 数据表基本信息
# print(df.info())
# 每一列数据的格式
# print(df.dtypes)
# 某一列数据的格式
# print(df['date'].dtype)
# 空值
# print(df.isnull())
# 某一列的唯一值
# print(df['age'].unique())
# 查看数据表的值
# print(df.values)
# 查看列名称
# print(df.columns)
# 查看前几行或后几行数据，默认为10
# print(df.head(2))
# print(df.tail(2))

# 数据清洗
# 用0填充空值
# print(df.fillna(value=0))
# 用平均值填充
# print(df['price'].fillna(df['price'].mean()))
# 清除city字段的字符空格
# df['city'] = df['city'].map(str.strip)
# print(df['city'])
# 大小写转换
# df['city'] = df['city'].str.lower()
# print(df['city'])
# 修改数据格式
# print(df['price'].dtype)
# df['price'] = df['price'].fillna(value=df['price'].mean())
# df['price'] = df['price'].astype('int')
# print(df['price'].dtype)
# 修改列名称
# df = df.rename(columns={'category':'category-size'})
# print(df.columns)
# 删除后出现的重复值
# df['city'] = df['city'].drop_duplicates()
# 删除先出现的重复值
#df['city'] = df['city'].drop_duplicates(keep='last')
# 数据替换
# df['city'] = df['city'].replace('SH', 'shanghai')

# 数据预处理
df1 = pd.DataFrame({'id':[1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
                    "gender": ['male', 'female', 'male', 'female', 'male', 'female', 'male', 'female'],
                    "pay": ['Y', 'N', 'Y', 'Y', 'N', 'Y', 'N', 'Y'],
                    "m-point": [10, 12, 20, 40, 40, 40, 30, 20]})
# 数据表合并
df_inner = pd.merge(df, df1, how='inner')
df_left = pd.merge(df, df1, how='left')
df_right = pd.merge(df, df1, how='right')
df_outer = pd.merge(df, df1, how='outer')
# 设置索引列
# df_inner.set_index('id')
# 重设索引
# df_inner.reset_index()
# 按照特定列的值排序
# df_inner = df_inner.sort_values(by=['age'])
# 按照索引列排序
# df_inner = df_inner.sort_index()
# 如果price列的值大于3000，group列的值显示high，否则为low
# df_inner['group'] = np.where(df_inner['price']>3000, 'high', 'low')
# 对符合多个条件的数据进行分组标记
# df_inner.loc[(df_inner['city'].map(str.strip) == 'Beijing') & (df_inner['price'] > 4000), 'sign'] = 1
# 对category字段的值进行分裂并创建数据表
# df2 = pd.DataFrame((x.split('-') for x in df_inner['category']), index=df_inner.index, columns=['category', 'size'])
# 与df_inner数据表进行匹配
# df_inner2 = pd.merge(df_inner, df2, left_index=True, right_index=True)
# print(df_inner2)

# 数据提取
# loc按标签值进行提取  iloc按位置进行提取  ix可以同时按位置和标签值进行提取
# 选取符合条件的数据
# print(df_inner.loc[3])
# print(df_inner.iloc[0:2])
# print(df_inner.loc[df_inner['price']>2000])
# print(df_inner.query('price>2000'))
# print(df_inner.loc[df_inner['city'].isin(['Beijing ', 'shanghai'])])
# 三行两列
# print(df_inner.iloc[:3,:2])
# 0 2 5行 4 5 列
# print(df_inner.iloc[[0,2,5], [4,5]])
# 20130104号之前，前四列数据
# print(df_inner.ix[:'2013-01-04', :4])
# 找出符合条件的指定列的数据
# print(df_inner.loc[(df_inner['age']>25) & (df_inner['city']=='Beijing '), ['id', 'city', 'age', 'category', 'gender']])
# 排序并按列进行计数
# print(df_inner.loc[(df_inner['city']!='Beijing '), ['id', 'city', 'gender']].sort_values(['id']))
# print(df_inner.loc[(df_inner['city']!='Beijing '), ['id', 'city', 'gender']].sort_values(['id']).city.count())
# 筛选后按列求和
# print(df_inner.query('city==["Beijing ", "shanghai"]').price.sum())

# 数据汇总
# 按城市对所有列进行计数汇总
# print(df_inner.groupby('city').count())
# 按城市对id字段进行计数汇总
# print(df_inner.groupby('city')['id'].count())
# 对两个字段进行汇总计数
# print(df_inner.groupby(['city', 'price'])['id'].count())
# 聚合函数
# print(df_inner.groupby('city')['price'].agg([len, np.sum, np.mean]))

# 数据统计
# 数据采样
# print(df_inner.sample(n=3))
# 手动设置采样权重
# weights = [0,0,0,0,0.5,0.5]
# print(df_inner.sample(n=2, weights=weights))
# 采样后不放回
# print(df_inner.sample(n=6, replace=False))
# 采样后放回
# print(df_inner.sample(n=6, replace=True))
# 描述性统计(数量，均值，标准差，最小值，分位数，最大值）
# print(df_inner.describe().round(2).T)
# 计算列的标准差
# print(df_inner['price'].std().round(3))
# 计算两个字段间的协方差
# print(df_inner['price'].cov(df_inner['m-point']))
# 所有字段间的协方差
# print(df_inner.cov().round(3))
# 两个字段的相关性分析
# print(df_inner['price'].corr(df_inner['m-point']))
# 所有字段的相关性分析
# print(df_inner.corr())

# 数据输出
# df_inner.to_excel('name.xlsx', sheet_name='sheetname')
# df_inner.to_csv('name.csv')