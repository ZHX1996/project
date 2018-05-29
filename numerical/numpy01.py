# coding:utf-8
import numpy as np
import numpy.matlib as matlib

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

# 将数组广播到新形状
# a = np.arange(4).reshape(1, 4)
# print(np.broadcast_to(a, (4, 4)))

# 在指定位置插入新的轴来扩展数组形状
# x = np.array(([1,2], [3, 4]))
# y = np.expand_dims(x, axis = 0)
# print(y)
# print(x.shape, y.shape)

# 从给定数组的形状中删除一维条目
# x = np.arange(9).reshape(1,3,3)
# y = np.squeeze(x, 0)
# print(y)
# print(y.shape)

# 数组的连接
# 连接两个或多个相同形状的数组
# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6], [7, 8]])
# print(np.concatenate((a, b)))  # 4*2 同vstack
# print(np.concatenate((a, b), axis=1))  # 2*4 同hstack
#
# # 沿新轴连接数组序列(会多出来一维2*2*2)
# print(np.stack((a, b), 0))
# print(np.stack((a, b), 1))
# print(np.vstack((a, b)))  # 垂直堆叠
# print(np.hstack((a, b)))  # 水平堆叠


# 数组分割
# a = np.arange(9)
# # 分成大小相等的三个子数组
# print(np.split(a, 3))
# # 从给定的位置分割
# print(np.split(a, [4, 7]))

# 水平分割, 参数为分割成几份
# a = np.arange(16).reshape(4,4)
# print(np.hsplit(a, 2))
# # 垂直分割
# print(np.vsplit(a, 2))

# 添加/删除元素
# resize返回指定形状的新数组
# a = np.arange(6).reshape(2, 3)
# print(np.resize(a, (3, 2)))
# # 元素不够的话会重复
# print(np.resize(a, (3, 3)))

# 在数组的末尾添加值,如果未给定轴，数组会展开
# a = np.arange(6).reshape(2,3)
# print(np.append(a, [7,8,9]))
# print(np.append(a, [[7,8,9]], axis=0))
# print(np.append(a, [[5,5,5], [7,8,9]], axis = 1))

# 在给定索引之前沿给定轴插入值
# a = np.arange(6).reshape(3, 2)
# print(np.insert(a, 2, [11, 12]))
# print(np.insert(a, 1, [11], axis = 0))
# print(np.insert(a, 1, [11], axis = 1))

# 从数组中删除指定子数组
# a = np.arange(12).reshape(3, 4)
# print(np.delete(a, 5))
# print(np.delete(a, 1, axis=1))
# # 每两个删除一个
# print(np.delete(a, np.s_[::2]))

# 去重
# a = np.array([5,2,6,2,7,5,6,8,2,9])
# print(np.unique(a))
# print(np.unique(a, return_index=True))  # 输出数组在原数组的下标
# print(np.unique(a, return_inverse=True))  # 原数组各元素在输出数组中的下标
# print(np.unique(a, return_counts=True))  # 输出数组各元素在原数组中出现的次数
# # 重构原数组
# u, indices = np.unique(a, return_inverse=True)
# print(u[indices])

# 位操作
# a, b = 13, 17
# print(bin(a), bin(b))
# print(np.bitwise_and(a, b))
# print(np.bitwise_or(a, b))
# 计算输入数组中的位非结果，对于有符号整数，返回补码
# print(np.invert(np.array([13], dtype=np.uint8)))  # 结果为242
# print(np.binary_repr(12, width=8))
# print(np.binary_repr(242, width=8))
# 左移 补0
# print(np.left_shift(10, 2))
# # 右移
# print(np.right_shift(10, 2))

# 字符串函数
# print(np.char.add(['hello', 'hi'], [' abc,', ' 123']))  # ['hello abc,' 'hi 123']
# print(np.char.multiply('hello ', 3))
# print(np.char.center('hello', 20, fillchar='*'))  # 两边填充*，使hello位于中间
# print(np.char.capitalize('hello world'))  # 返回副本，第一个字母大写
# print(np.char.title('hello, how are you'))  # 每个单词首字母都大写
# print(np.char.lower('HELLO'))
# print(np.char.split('hello,how,are,you', sep=','))
# print(np.char.splitlines('hello\nhow are you'))
# print(np.char.strip(['arora', 'admin', 'java'], 'a'))
# print(np.char.join([':', '-'], ['dmy', 'ymd']))
# print(np.char.replace('he is a good boy', 'is', 'are'))
# a = np.char.encode('hello', 'cp500')
# print(a)
# print(np.char.decode(a, 'cp500'))

# 三角函数
# sin cos tan arcsin arccos arctan 以弧度运算(*np.pi/180)
# degrees将弧度转化为角度
# a = np.array([0, 30, 45, 60, 90])
# b = np.sin(a*np.pi/180)
# inv = np.arcsin(b)
# c = np.degrees(inv)
# print(b)
# print(inv)
# print(c)

# 舍入函数
# a = np.array([3.33333])
# print(np.around(a, 2))
# # floor 不大于输入参数的最大整数
# print(np.floor(a))
# # ceil 上限
# print(np.ceil(a))

# 算术运算
# add subtract multiply divide
# reciprocal 倒数 对于绝对值大于1的整数，返回0，对于0，溢出警告
# a = np.array([0.25, 1.33, 1, 0, 100])
# print(np.reciprocal(a))

# power 以第一个数组为底，计算与第二个数组对应元素的幂
# a = np.array([10, 100, 1000])
# print(np.power(a, 2))

# mod/remainder 返回除法余数
# a = np.array([10, 20, 30])
# b = np.array([3, 5, 7])
# print(np.mod(a, b))

# 复数
# real:实部  image：虚部  conj：反转虚部符号后的共轭复数 angle：复数参数的角度 deg为true是角度表示

# 统计函数
# 从指定轴返回最小，最大值
# a = np.array([[3,7,5], [8,4,3], [2,4,9]])
# print(np.amin(a,1))
# print(np.amax(a,1))

# 返回沿轴的值的范围(最大值-最小值)
# print(np.ptp(a, axis = 1))

# 返回数组中可以按照百分比划分数组的元素
# a = np.array([[30,40,70], [80,20,10], [50,90,60]])
# print(np.percentile(a, 50, axis=1))

# 将数据样本上半部分和下半部分分开的值
# print(np.median(a, axis=0))

# 平均值
# print(np.mean(a, axis=0))

# 加权平均, 在多维数组中可以指定用于计算的轴
# a = np.array([1,2,3,4])
# wts = np.array([4,3,2,1])
# print(np.average(a, weights=wts))

# 标准差和方差
# print(np.std(a))
# print(np.var(a))

# 排序
# 参数kind有quicksort，mergesort(归并), heapsort
# 参数order， 要排序的字段
# dt = np.dtype([('name', 'S10'), ('age', int)])
# a = np.array([("raju",21), ("anil",25), ("ravi", 17), ("amar",27)], dtype = dt)
# print(np.sort(a, order='name'))

# 间接排序，返回下标
# x = np.array([3,1,2])
# y = np.argsort(x)
# print(y)
# print(x[y])

# 间接排序，返回下标 sort by a, then by b
# 先根据a内的数据从小到大排序，相同的数按b内的数据来排
# a = [1,5,1,4,3,4,4]
# b = [9,4,0,4,0,2,1]
# ind = np.lexsort((b, a))
# print(ind)

# 返回沿指定轴最大和最小元素的索引
# a = np.array([[30,40,70],[80,20,10],[50,90,60]])
# print(np.argmax(a, axis=1))
# print(np.argmin(a, axis=1))

# 非0元素的索引
# print(np.nonzero(a))

# 满足条件的元素的索引
# y = np.where(x>30)
# print(x[y]) # 获取满足条件的元素


# 返回满足条件的元素
# condition = np.mod(a, 2) == 0
# print(np.extract(condition, a))

# 小端存储(最小有效位存储在最小地址)
# 大端存储(最小有效位存储在最大地址)
# 大端和小端之间切换
# a = np.array([1, 256, 8755], dtype=np.int16)
# print(a.byteswap(True))

# 视图或浅拷贝(数据相同，维度改变时不影响原数组)
# a = np.arange(6).reshape(3,2)
# b = a.view()
# print(id(a))
# print(id(b))
# b.shape = 2, 3
# print(a)
# print(b)
# # 深拷贝，不与原始数组共享
# b = a.copy()

# 矩阵库，返回矩阵而不是ndarray
# a = matlib.empty((2,3), dtype=np.int8, order='C')
# print(a)
# zeros ones

# 对角线为1的矩阵，参数(n,M,k,dtype) ： (行数，列数，索引，类型)
# a = matlib.eye(3,4)
# print(a)

# 给定大小的单位矩阵：主对角线元素都为1的方阵
# a = matlib.identity(5)
# print(a)

# 给定大小的填充随机值的矩阵
# a = matlib.rand(3, 3)
# print(a)

# matrix和ndarray转换
# i = np.matrix('1,2;3,4')
# j = np.asarray(i)
# k = np.asmatrix(j)

# 线性代数
import numpy.linalg as linalg
# a = np.array([[1,2],[3,4]])
# b = np.array([[11,12], [13,14]])

# 两个数组的点积 [[1*11+2*13, 1*12+2*14], [3*11+4*13, 3*12+4*14]]
# print(np.dot(a,b))

# 两个向量的点积(得到一个数) 1*11 + 2*12 + 3*13 + 4*14 = 130
# print(np.vdot(a,b))

# 向量内积 [[1*11+2*12, 1*13+2*14], [3*11+4*12, 3*13+4*14]]
# print(np.inner(a,b))

# 矩阵乘积
# a = [[1,0], [0,1]]
# b = [[4,1], [2,2]]
# print(np.matmul(a,b))

# 行列式
# a = np.array([[1,2], [3,4]])
# print(linalg.det(a))

# 矩阵形式线性方程组的解
# a = np.array([[1,1,1], [0,2,5], [2,5,-1]])
# b = np.array([[6], [-4], [27]])
# print(linalg.solve(a,b))

# 矩阵的逆
# a = np.array([[1,1,1], [0,2,5], [2,5,-1]])
# b = linalg.inv(a)
# print(b)

# I/O操作
# load和save函数处理numpy二进制文件
# loadtxt和savetxt函数处理文本文件