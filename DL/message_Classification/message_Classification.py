from itertools import islice
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import PCA
from sklearn.externals import joblib
import io


def process_data():
    label, message = [], []
    train_file = io.open('message_classification_train.csv', 'r', encoding='utf-8')
    for line in islice(train_file, 1, None):
        p = line.index(',')
        label.append(line[:p])
        message.append(line[p+2:-5])
    return label, message


def tf_idf(message):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(message)
    # word = vectorizer.get_feature_names()

    transformer = TfidfTransformer()
    word_vector = transformer.fit_transform(X)
    weight = word_vector.toarray()

    # for i in range(len(weight)):
    #     for j in range(len(word)):
    print(weight.shape)
    return weight


# 5574,9364->5574,2230
def decompose(data):
    pca = PCA(n_components=0.9)
    newData = pca.fit_transform(data)
    joblib.dump(newData, 'pcaModel.pkl', compress=3)
    # print(newData.shape)


def loadModel():
    newData = joblib.load('pcaModel.pkl')
    print(newData.shape)

if __name__ == '__main__':
    # label, message = process_data()
    # data = tf_idf(message)
    # decompose(data)
    loadModel()
