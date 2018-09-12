#-*-coding:utf-8-*-
import math
import numpy as np


def calcGini(dataset):
    num = len(dataset)
    labelCount = {}
    for vec in dataset:
        currentLabel = vec[-1]
        if currentLabel not in labelCount.keys():
            labelCount[currentLabel] = 0
        labelCount[currentLabel] += 1

    Gini = 1.0
    for key in labelCount:
        prob = float(labelCount[key])/num
        Gini -= prob*prob
    return Gini


def calcGiniwithFeature(dataset, feature, value):
    D0 = []
    D1 = []
    for featureVec in dataset:
        if featureVec[feature] == value:
            D0.append(featureVec)
        else:
            D1.append(featureVec)
    Gini = len(D0)/len(dataset)*calcGini(D0)+len(D1)/len(dataset)*calcGini(D1)
    return Gini

def chooseBestFeature(dataset):
    numFeatures = len(dataset[0])-1
    bestGini = float('inf'); bestFeature = 0; bestValue = 0; newGini = 0
    for i in range(numFeatures):
        featureList = [example[i] for example in dataset]
        uniqueVals = set(featureList)
        for splitVal in uniqueVals:
            newGini = calcGiniwithFeature(dataset, i, splitVal)
            if newGini < bestGini:
                bestFeature = i
                bestGini = newGini
    return bestFeature



def calcShannonEnt(dataset):
    num = len(dataset)
    labelCount = {}
    for vec in dataset:
        currentLabel = vec[-1]
        if currentLabel not in labelCount.keys():
            labelCount[currentLabel] = 0
        labelCount[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCount:
        prob = float(labelCount[key]/num)
        shannonEnt -= prob*math.log(prob, 2)
    return shannonEnt


def splitDataset(dataset, axis, value):
    ret = []
    for featureVec in dataset:
        if featureVec[axis] == value:
            reducedFeatureVec = featureVec[:axis]
            reducedFeatureVec.extend(featureVec[axis+1:])
            ret.append(reducedFeatureVec)
    return ret


def conditionEntropy(dataset, i, featurelist, uniqueVals):
    conditionEnt = 0.0
    for value in uniqueVals:
        subDataset = splitDataset(dataset, i, value)
        prob = len(subDataset)/float(len(dataset))
        conditionEnt += prob * float(calcShannonEnt(subDataset))
    return conditionEnt

def informationGain(dataset, baseEntroy, i):
    featureList = [example[i] for example in dataset]
    uniqueVals = set(featureList)
    newEntroy = ConditionEntroy(dataset, i, featureList, uniqueVals)
    infoGain = baseEntroy - newEntroy
    return infoGain

def informationGainRatio(dataset, baseEntroy, i):
    featureList = [example[i] for example in dataset]
    uniqueVals = set(featureList)
    splitInfo = 0.0
    for value in uniqueVals:
        subdataset = splitDataset(dataset, i, value)
        prob = len(subdataset)/float(len(dataset))
        splitInfo -= prob/math.log(prob,2)
    return informationGain(dataset, baseEntroy, i)/splitInfo


# 逻辑回归
#  https://blog.csdn.net/csqazwsxedc/article/details/69690655
def sigmoid(inx):
    return 1.0/(1+np.exp(-inx))

def gradAscent(data, label):
    dataMatrix = np.mat(data)
    classLabel = np.mat(label).transpose()
    m,n = np.shape(dataMatrix)
    alpha = 0.001
    maxCycles = 500
    weights = np.ones((n, 1))
    for k in range(maxCycles):
        h = sigmoid(dataMatrix*weights)
        error = classLabel-h
        weights = weights + alpha*dataMatrix.transpose()*error
    return weights

def stocgradAscent(data, label):
    dataMatrix = np.mat(data)
    classLabel = label
    m,n = np.shape(dataMatrix)
    alpha = 0.001
    maxCycles = 500
    weights = np.ones((n, 1))
    for k in range(maxCycles):
        for i in range(m):
            h = sigmoid(sum(dataMatrix[i]*weights))
            error = classLabel-h
            weights = weights + alpha*dataMatrix[i].transpose()*error
    return weights


# KL散度
def KL(p ,q):
    p_total = len(p) + 1e-5
    q_total = len(q) + 1e-5
    x_unique = set(p+q)
    p_stat = {x:0 for x in x_unique}
    q_stat = {x:0 for x in x_unique}
    for x in p:
        p_stat[x] += 1
    for x in q:
        q_stat[x] += 1
    kl_val = 0
    for x in x_unique:
        p_prob = p_stat[x]/p_total + 1e-5
        q_prob = q_stat[x]/q_total + 1e-5
        kl_val += p_prob * math.log(p_prob/q_prob, 2)
    print("%.2f" % kl_val)


# 朴素贝叶斯
#  https://blog.csdn.net/qq_36047182/article/details/79753395
def createVocabList(dataset):
    vocabSet = set([])
    for document in dataset:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

def word2Vec(vocabList, inputSet):
    ret = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            ret[vocabList.index(word)] = 1
    return ret

def naiveBayesian(trainMatrix, label):
    numTrain = len(trainMatrix)
    numWord = len(trainMatrix[0])
    pAbusive = sum(label)/float(numTrain)  # 1的概率

    p0 = np.zeros(numWord)
    p1 = np.zeros(numWord)
    p0Denmo = 0.0
    p1Denmo = 0.0
    for i in range(numTrain):
        if label[i] == 1:
            p1 += trainMatrix[i]
            p1Denmo += sum(trainMatrix[i])
        else:
            p0 += trainMatrix[i]
            p0Denmo += sum(trainMatrix[i])
    p1Vec = p1/p1Denmo
    p0Vec = p0/p0Denmo
    return p0Vec, p1Vec, pAbusive

def classify(newVec, p0Vec, p1Vec, pAbusive):
    p1 = sum(newVec* p1Vec) + math.log(pAbusive)
    p0 = sum(newVec * p0Vec) + math.log(1.0-pAbusive)
    if p1 > p0:
        return 1
    else:
        return 0

if __name__ == '__main__':
    dataset = [['young', 'myope', 'no', 'reduced', 'no lenses'],
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
    # print(splitDataset(dataset))

    p = [1,1,1,2,3,4,1,2,3,4,1,3,4,1,2,3,3,1,2,3,1,2,3,1,3,1]
    q = [2,2,2,2,3,4,4,2,2,1,2,4,3,2,2,1,3,4,4,2,4,3]
    KL(p, q)


    dataset = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    label = [0,1,0,1,0,1]
    vocabset = createVocabList(dataset)
    trainMatrix = []
    for data in dataset:
        trainMatrix.append(word2Vec(vocabset, data))

    p0Vec, p1Vec, pAbusive = naiveBayesian(trainMatrix, label)

    newData = ['my', 'dog', 'has', 'flea', 'problems', 'help', 'please']
    newVec = word2Vec(vocabset, newData)
    print(classify(newVec, p0Vec, p1Vec, pAbusive))