# https://blog.csdn.net/herosofearth/article/details/52347820
# https://blog.csdn.net/herosofearth/article/details/52425952
import math


# H(X) = -sum(p*log(p))
def shannon_ent(dataset):
    '''
    计算香农熵
    :param dataset: 数据集
    :return: 计算结果
    '''
    numEntries = len(dataset)
    labelCounts = {}
    for featVec in dataset:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * math.log(prob, 2)
    return shannonEnt

def splitDataSet(dataSet, axis, value):
    '''
    按照给定特征划分数据集
    :param dataSet: 待划分的数据集
    :param axis: 划分数据集的特征
    :param value: 需要返回的特征的值
    :return: 划分结果列表
    '''
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

# H(Y|X) = sum(p * H(Y|X=x_i))
def ConditionalEntropy(dataSet, i, featList, uniqueVals):
    '''
    计算X_i给定的条件下，Y的条件熵
    :param dataSet: 数据集
    :param i: 维度i
    :param featList: 数据集特征列表
    :param uniqueVals: 数据集特征集合
    :return: 条件熵
    '''
    conditionEnt = 0.0
    for value in uniqueVals:
        subDataSet = splitDataSet(dataSet, i, value)
        prob = len(subDataSet) / float(len(dataSet))
        conditionEnt += prob * float(shannon_ent(subDataSet))
    return conditionEnt

def informationGain(dataSet, baseEntropy, i):
    '''
    计算信息增益
    :param dataSet: 数据集
    :param baseEntropy: 数据集的信息熵
    :param i: 特征维度i
    :return: 特征i对应的信息增益
    '''
    featList = [example[i] for example in dataSet]
    uniqueVals = set(featList)
    newEntropy = ConditionalEntropy(dataSet, i, featList, uniqueVals)
    infoGain = baseEntropy - newEntropy
    return infoGain

def informationGainRatio(dataSet, baseEntropy, i):
    '''
    计算信息增益比
    :param dataSet: 数据集
    :param baseEntropy: 数据集的信息熵
    :param i: 特征维度i
    :return: 信息增益比
    '''
    # return informationGain(dataSet, baseEntropy, i) / baseEntropy
    featList = [example[i] for example in dataSet]
    uniqueVals = set(featList)
    splitInfo = 0.0
    for value in uniqueVals:
        subDataSet = splitDataSet(dataSet, i, value)
        prob = len(subDataSet) / float(len(dataSet))
        splitInfo -= prob * math.log(prob, 2)
    return informationGain(dataSet, baseEntropy, i) / splitInfo
