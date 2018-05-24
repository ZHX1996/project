import operator
import copy
from decisionTree01 import splitDataSet, majorityCnt, classify


def calcGini(dataSet):
    '''
    计算基尼系数
    :param dataSet: 数据集
    :return: 结果
    '''
    numEntries = len(dataSet)
    labelCounts = {}
    for featureVec in dataSet:
        currentLabel = featureVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel]+=1
    Gini = 1.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        Gini -= prob * prob
    return Gini


def calcGiniWithFeature(dataSet, feature, value):
    '''
    计算给定特征下的基尼系数
    :param dataSet: 数据集
    :param feature: 特征维度
    :param value: 该特征变量所取的值
    :return: 结果
    '''
    D0 = []
    D1 = []
    for featureVec in dataSet:
        if featureVec[feature] == value:
            D0.append(featureVec)
        else:
            D1.append(featureVec)
    Gini = len(D0)/len(dataSet)*calcGini(D0) + len(D1)/len(dataSet)*calcGini(D1)
    return Gini


def chooseBestSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    bestGini = float('inf'); bestFeature = 0; bestValue = 0; newGini = 0
    for i in range(numFeatures):
        featureList = [example[i] for example in dataSet]
        uniqueVals = set(featureList)
        for splitVal in uniqueVals:
            newGini = calcGiniWithFeature(dataSet, i, splitVal)
            if newGini < bestGini:
                bestFeature = i
                bestGini = newGini
    return bestFeature


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
    bestFeature = chooseBestSplit(dataSet)
    bestFeatureLabel = labels[bestFeature]
    myTree = {bestFeatureLabel: {}}  # 使用字典存储树的信息
    del(labels[bestFeature])
    featureValues = [example[bestFeature] for example in dataSet]
    uniqueValues = set(featureValues)
    for value in uniqueValues:
        subLabels = labels[:]
        myTree[bestFeatureLabel][value] = createTree(splitDataSet(dataSet, bestFeature, value), subLabels)
    return myTree


def calcTestErr(myTree, testData, labels):
    errorCount = 0.0
    for i in range(len(testData)):
        if classify(myTree, labels, testData[i]) != testData[i][-1]:
            errorCount += 1
    return float(errorCount)


def testMajor(major, testData):
    '''
    计算剪枝后的预测误差
    :param major:
    :param testData:
    :return:
    '''
    errorCount = 0.0
    for i in range(len(testData)):
        if major != testData[i][-1]:
            errorCount += 1
    return float(errorCount)


def pruningtree(inputTree, dataSet, testData, labels):
    if type(inputTree).__name__ != 'dict':
        return
    firstStr = list(inputTree.keys())[0]
    secondDict = inputTree[firstStr]
    classList = [example[-1] for example in dataSet]
    featureKey = copy.deepcopy(firstStr)
    labelIndex = labels.index(featureKey)
    subLabels = copy.deepcopy(labels)
    del(labels[labelIndex])
    for key in list(secondDict.keys()):
        if type(secondDict[key]).__name__ == 'dict':
            subDataSet = splitDataSet(dataSet, labelIndex, key)
            subTestSet = splitDataSet(testData, labelIndex, key)
            if len(subDataSet)>0 and len(subTestSet)>0:
                inputTree[firstStr][key] = pruningtree(secondDict[key], subDataSet, subTestSet, copy.deepcopy(labels))
    if calcTestErr(inputTree, testData, subLabels) < testMajor(majorityCnt(classList), testData):
        return inputTree
    else:
        return majorityCnt(classList)

if __name__ == '__main__':
    dataSet = [['young', 'myope', 'no', 'reduced', 'no lenses'],
               ['young', 'myope', 'no', 'normal', 'soft'],
               ['young', 'myope', 'yes', 'reduced', 'no lenses'],
               ['young', 'hyper', 'no', 'normal', 'soft'],
               ['young	', 'hyper', 'yes', 'reduced',	'no lenses'],
               ['young', 'hyper', 'yes', 'normal', 'hard'],
               ['pre', 'myope', 'no', 'reduced	', 'no lenses'],
               ['pre', 'myope', 'no', 'normal', 'soft'],
               ['presbyopic', 'myope', 'yes', 'reduced', 'no lenses'],
               ['presbyopic', 'hyper', 'no', 'normal', 'soft'],
               ['presbyopic', 'hyper', 'yes', 'reduced', 'no lenses'],
               ['presbyopic', 'hyper', 'yes', 'normal', 'no lenses'],
               ['pre', 'hyper', 'yes', 'normal', 'no lenses'],
               ['presbyopic', 'myope', 'no', 'reduced', 'no lenses'],
               ['pre', 'hyper', 'yes', 'reduced', 'no lenses'],
               ['presbyopic', 'myope', 'no', 'normal', 'no lenses'],
               ['pre', 'myope', 'yes', 'normal', 'hard'],
               ['pre', 'hyper', 'no', 'reduced', 'no lenses']]
    labels = ['age', 'prescript', 'astigmatic', 'tearRate']
    testData =[['presbyopic', 'myope', 'yes', 'normal', 'hard'],
               ['presbyopic', 'hyper', 'no', 'reduced', 'no lenses'],
               ['young', 'myope', 'yes', 'normal', 'hard'],
               ['young', 'hyper', 'no', 'reduced', 'no lenses'],
               ['pre', 'myope', 'yes', 'reduced', 'no lenses'],
               ['pre', 'hyper', 'no', 'normal', 'soft']]
    myTree = createTree(dataSet, labels)
    print(myTree)

    labels01 = ['age', 'prescript', 'astigmatic', 'tearRate']
    testErr = calcTestErr(myTree, testData, labels01)
    print(testErr)

    # myTree01 = pruningtree(myTree, dataSet, testData, labels01)
    # testErr01 = calcTestErr(myTree01, testData, labels01)
    # print(testErr01)
