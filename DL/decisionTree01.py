# https://blog.csdn.net/herosofearth/article/details/52347820
# https://blog.csdn.net/herosofearth/article/details/52425952
import math
import operator


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

def chooseBestFeatureToSplitByID3(dataSet):
    '''
    选择最好的数据集划分方式
    :param dataSet: 数据集
    :return: 划分结果
    '''
    numFeatures = len(dataSet[0]) - 1 # 最后一列不属于特征向量
    baseEntropy = shannon_ent(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        infoGain = informationGain(dataSet, baseEntropy, i)
        if infoGain > bestInfoGain: # 选择最大的信息增益
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature


def chooseBestFeatureToSplitByC45(dataSet):
    '''
    选择最好的数据集划分方式
    :param dataSet: 数据集
    :return: 划分结果
    '''
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = shannon_ent(dataSet)
    bestInfoGainRate = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        infoGainRate = informationGainRatio(dataSet, baseEntropy, i)
        if infoGainRate > bestInfoGainRate:
            bestInfoGainRate = infoGainRate
            bestFeature = i
    return bestFeature


def majorityCnt(classList):
    '''
    多数表决决定叶节点的分类
    :param classList: 所有类标签列表
    :return: 出现次数最多的类
    '''
    classCount = {}
    for vote in classCount:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount += 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def createTree(dataSet, labels):

    '''
    创建决策树
    :param dataSet: 训练数据集
    :return labels: 所有的类标签
    '''
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):  # 第一个递归结束条件:所有类标签相同
        return classList[0]
    if len(dataSet[0]) == 1:  # 第二个递归结束条件:用完了所有特征
        return majorityCnt(classList)
    # bestFeature = chooseBestFeatureToSplitByID3(dataSet)  # 最优划分特征
    bestFeature = chooseBestFeatureToSplitByC45(dataSet)
    bestFeatureLabel = labels[bestFeature]
    myTree = {bestFeatureLabel: {}}  # 使用字典存储树的信息
    del(labels[bestFeature])
    featureValues = [example[bestFeature] for example in dataSet]
    uniqueValues = set(featureValues)
    for value in uniqueValues:
        subLabels = labels[:]
        myTree[bestFeatureLabel][value] = createTree(splitDataSet(dataSet, bestFeature, value), subLabels)
    return myTree


def classify(inputTree, featureLabels, testVec):
    '''
    做出决策
    :param inputTree: 决策树模型
    :param featureLabels: 所有的类标签
    :param testVec: 测试数据
    :return: 分类决策结果
    '''
    firstStr = list(inputTree.keys())[0]
    secondDict = inputTree[firstStr]
    featureIndex = featureLabels.index(firstStr)
    key = testVec[featureIndex]
    valueOfFeature = secondDict[key]
    if isinstance(valueOfFeature, dict):
        classLabel = classify(valueOfFeature, featureLabels, testVec)
    else:
        classLabel = valueOfFeature
    return classLabel

if __name__ == '__main__':
    dataSet = [['youth', 'no', 'no', '1', 'refuse'],
               ['youth', 'no', 'no', '2', 'refuse'],
               ['youth', 'yes', 'no', '2', 'agree'],
               ['youth', 'yes', 'yes', '1', 'agree'],
               ['youth', 'no', 'no', '1', 'refuse'],
               ['mid', 'no', 'no', '1', 'refuse'],
               ['mid', 'no', 'no', '2', 'refuse'],
               ['mid', 'yes', 'yes', '2', 'agree'],
               ['mid', 'no', 'yes', '3', 'agree'],
               ['mid', 'no', 'yes', '3', 'agree'],
               ['elder', 'no', 'yes', '3', 'agree'],
               ['elder', 'no', 'yes', '2', 'agree'],
               ['elder', 'yes', 'no', '2', 'agree'],
               ['elder', 'yes', 'no', '3', 'agree'],
               ['elder', 'no', 'no', '1', 'refuse'],
               ]
    labels = ['age', 'working', 'house', 'credit_situation']
    labels1 = ['age', 'working', 'house', 'credit_situation']
    myTree = createTree(dataSet, labels)
    print(myTree)
    testVec = ['youth', 'no', 'no', '1']
    ret = classify(myTree, labels1, testVec)
    print(ret)