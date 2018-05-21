import os
import sys
import numpy as np
import matplotlib
import scipy
import matplotlib.pyplot as plt
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
import lda
import lda.datasets


# def generate_data():
#     corpus = []
#     for line in open('LDA_text.txt', 'r', encoding='utf-8').readlines():
#         # print(line)
#         corpus.append(line.strip())
#     # 将文本中的词语转换为词频矩阵，矩阵元素a[i][j]代表j词在i类文本下的词频
#     vectorizer = CountVectorizer()
#
#     word = vectorizer.get_feature_names()
#     print('features length:' + str(len(word)))
#     for j in range(len(word)):
#         print(word[j])
#
#     X = vectorizer.fit_transform(corpus)
#     analyze = vectorizer.build_analyzer()
#     weight = X.toarray()
#
#     # print(len(weight))
#     # print(weight[:5, :5])
#     return corpus


def lda_test():
    corpus = []
    for line in open('LDA_text.txt', 'r', encoding='utf-8').readlines():
        # print(line)
        corpus.append(line.strip())
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus)

    model = lda.LDA(n_topics=2, n_iter=500, random_state=1)
    # model.fit(np.asarray(weight))
    model.fit_transform(X)

    topic_word = model.topic_word_
    word = vectorizer.get_feature_names()
    for w in word:
        print(w)
    print(topic_word[:, :3])
    n = 5
    for i, topic_dist in enumerate(topic_word):
        topic_words = np.array(word)[np.argsort(topic_dist)][:-(n+1):-1]
        print(u'*topic {}\n- {}'.format(i, ''.join(topic_words)))

    doc_topic = model.doc_topic_
    print('type(doc_topic):{}'.format(type(doc_topic)))
    print('shape:{}'.format(doc_topic.shape))

    label = []
    for n in range(10):
        topic_most_pr = doc_topic[n].argmax()
        label.append(topic_most_pr)
        print('doc:{} topic:{}'.format(n, topic_most_pr))


def tfidf_test():
    corpus = []
    for line in open('LDA_text.txt', 'r', encoding='utf-8').readlines():
        # print(line)
        corpus.append(line.strip())
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus)

    word = vectorizer.get_feature_names()
    print('features length:' + str(len(word)))
    for j in range(len(word)):
        print(word[j])

    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(X)
    weight = tfidf.toarray()

    for i in range(len(weight)):
        for j in range(len(word)):
            print(weight[i][j])
        print('\n')

if __name__ == '__main__':
    # lda_test()
    tfidf_test()
