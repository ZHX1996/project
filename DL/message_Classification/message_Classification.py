from itertools import islice
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import PCA
from sklearn.externals import joblib
import io
from sklearn import svm
import numpy as np
import csv


def train_data():
    label, message = [], []
    train_file = io.open('message_classification_train.csv', 'r', encoding='utf-8')
    for line in islice(train_file, 1, None):
        p = line.index(',')
        label.append(0 if line[:p] == 'ham' else 1)
        message.append(line[p+2:-5])
    return label, message


def test_Data():
    SmsId, message = [], []
    test_file = io.open('test.csv', 'r', encoding='utf-8')
    for line in islice(test_file, 1, None):
        # print(line)
        p = line.index(',')
        SmsId.append(line[:p])
        message.append(line[p+1:-1])
    return SmsId, message


def classfication(label, message, SmsId, text):
    vectorizer = CountVectorizer()
    trainvec = vectorizer.fit_transform(message)
    testvec = vectorizer.transform(text)

    transformer = TfidfTransformer()
    trainvec_word_vector = transformer.fit_transform(trainvec)
    testvec_word_vector = transformer.transform(testvec)
    trainData = trainvec_word_vector.toarray()
    testData = testvec_word_vector.toarray()

    # pca = PCA(n_components=0.9)
    # pcaTrainData = pca.fit_transform(trainData)
    pca = joblib.load('pcaModel.pkl')
    pcaTestData = pca.transform(testData)
    # joblib.dump(pca, 'pcaModel.pkl', compress=3)

    # svc = svm.SVC()
    # svc.fit(pcaTrainData, label)
    svc = joblib.load('svcModel.pkl')
    result = svc.predict(pcaTestData)
    # joblib.dump(svc, 'svcModel.pkl', compress=3)

    with open('result.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['SmsId', 'Label'])
        for i in range(min(len(SmsId), len(result))):
            writer.writerow([SmsId[i], 'spam' if result[i] == 0 else 'ham'])

if __name__ == '__main__':
    label, message = train_data()
    SmsId, test = test_Data()
    classfication(label, message, SmsId, test)
