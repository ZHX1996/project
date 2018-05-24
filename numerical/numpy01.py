import numpy as np

# student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
# a = np.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=student)
# print(a)
# print(a['name'])

# shape reshape
# a = np.array([[1,2,3], [4,5,6]])
# print(a.shape)
# a.shape = (3, 2)
# print(a)
# b = a.reshape(3, 2)
# print(b)

# ndim 维度
# a = np.arange(24)
# print(a)
# print(a.ndim) # 1
# a.shape = (2, 4, 3)
# print(a)
# print(a.ndim) # 3

# 元素占几个字节
# x = np.array([1,2,3,4,5], dtype=np.int16)
# print(x.itemsize)

# flags 对象拥有的属性
# x = np.array([1,2,3,4,5])
# print(x.flags)

# 创建新数组
# np.empty 创建未初始化数组，元素为随机值
# np.zeros 以0填充新数组
# np.ones 以1填充新数组
# 参数为shape，dtype，order
# order参数为'C'，按行的C风格数组， 为'F'，按列的Fortran风格数组

# asarray 从现有数据创建数组
# 参数第一个变为任意形式的输入，其它同上

# frombuffer 将缓冲区解释为一维数组
# s = 'Hello World'
# a = np.frombuffer(s, dtype='S1', count=-1, offset=0)
# print(a)

# fromiter 从可迭代对象构建一维数组
# list = range(5)
# it = iter(list)
# a = np.fromiter(it, dtype='f')
# print(a)

# 从数值范围生成数组
# np.arange 参数start end step dtype
# np.linspace 参数start stop num(等间隔样例数量) endpoint(是否包含stop，默认为true) retstep(如果为true，返回样例以及步长) dtype
# x = np.linspace(10, 20 ,5, endpoint=True, retstep=True)
# print(x)
# np.logspace 参数start stop num(范围内的数值数量) endpoint base(对数空间的底,默认为10) dtype
# x = np.logspace(1.0, 2.0, num = 10)
# print(x)

# 切片和索引
# 基本切片 slice 参数 start stop step
# a = np.arange(10)
# print(a[slice(2,7,2)])
# print(a[2:7:2])

# 省略号 使选择元组的长度与数组的维度相同
# a = np.array([[1,2,3], [4,5,6], [7,8,9]])
# print(a[...,1])
# print(a[1,...])
# print(a[1:,...])

# 高级索引：整数和布尔值
# 高级索引返回数据的副本，切片提供一个视图
# x = np.array([[1,2], [3,4], [5,6]])
# y = x[[0,1,2], [0,1,0]]
# print(y)

# x = np.array([[0,1,2], [3,4,5], [6,7,8], [9,10,11]])
# y1 = x[[0,0,3,3], [0,2,0,2]]
# # 行索引是[0,0]和[3,3]，列索引是[0,2]和[0,2]
# y2 = x[[[0,0],[3,3]], [[0,2], [0,2]]]
# print(y1)
# print(y2)

# 布尔索引
# x = np.array([[0,1,2], [3,4,5], [6,7,8], [9,10,11]])
# print(x[x>5])
# a = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
# print(a[~np.isnan(a)])
# b =np.array([1, 2+6j, 5, 3.5+5j])
# print(b[np.iscomplex(b)])

# 广播 在算术运算期间处理不同形状的数组的能力
# a = np.array([[0.0,0.0,0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]])
# b = np.array([1.0,2.0,3.0])
# print(a+b)

# a = np.arange(0, 60, 5)
# a.shape = (3, 4)
# for x in np.nditer(a):
#     print(x,)

# 迭代的顺序匹配数组的内容布局，不考虑特定的排序,下面的结果同上
# b =a.T
# for x in np.nditer(a):
#     print(x,)

# 以C风格顺序排序，顺序改变了；以F风格顺序排序，顺序不变(C按行，F按列)
# c = b.copy(order = 'C')
# for x in np.nditer(c):
#     print(x,)
#
# for x in np.nditer(b, order='F'):
#     print(x,)

# 修改数组的值
# a = np.arange(0, 60, 5)
# a.shape = (3, 4)
# for x in np.nditer(a, op_flags=['readwrite']):
#     x[...] = 2*x
# print(a)

# nditer的flags参数
# a = np.arange(0, 60, 5)
# a.shape = (3, 4)
# for x in np.nditer(a, flags=['external_loop'], order='F'):
#     print(x,)

# 广播迭代
# a = np.arange(0, 60, 5)
# a.shape = (3, 4)
# b = np.array([1,2,3,4], dtype=int)
# for x,y in np.nditer([a,b]):
#     print('%d:%d' % (x,y))

# 数组操作
# a = np.arange(8).reshape(2, 4)
# print(a)
# # 一维情况下的下标
# print(a.flat[5])
# # 折叠成一维的数组 flatten返回拷贝，ravel返回视图
# print(a.flatten())
# print(a.ravel())

# T和transpose都是转置

# rollaxis 向后滚动特定的轴
# arr, axis(要向后滚动的轴,其它轴的相对位置不变), start(要滚到的位置,默认为0)
# a = np.arange(8).reshape(2,2,2)
# print(a)
# print(np.rollaxis(a, 2))
# print(np.rollaxis(a, 2, 1))

#  swapaxes 交换数组的两个轴
# a = np.arange(8).reshape(2,2,2)
# print(np.swapaxes(a,2,0))

# 修改维度
# x = np.array([[1],[2],[3]]) # 3*1
# y = np.array([4,5,6])       # 1*3
# b = np.broadcast(x, y)      # 3*3
# for (u,v) in b:
#     print((u,v))

# c = np.empty(b.shape)
# c.flat = [u + v for (u,v) in b]
# print(c) # 结果和x+y一样
