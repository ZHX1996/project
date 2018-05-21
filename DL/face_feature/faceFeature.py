from itertools import islice
import numpy as np
import io


def train_data():
    dtrain, label, buff = [], [], []
    i = 0
    train_file = io.open('training.csv', 'r', encoding='utf-8')
    for s in islice(train_file, 1, 3):
        p = s.split(',')
        for i in range(len(p)-1):
            buff.append(float(p[i]))
        label.append(buff)
        buff = []

        q = p[-1]
        e = q.split(' ')
        for i in range(len(e)):
            buff.append(int(e[i]))
        dtrain.append(buff)

        buff = []
    return np.array(label), np.array(dtrain)
    # print(dtrain)
    # print(label)

def test_data():
    imageid, image, buff  = [], [], []
    test_file = io.open('test.csv', 'r', encoding='utf-8')
    for s in islice(test_file, 1, 3):
        p = s.split('\n')
        temp = p[0].split(',')
        imageid.append(int(temp[0]))
        e = temp[1].split(' ')
        for i in range(len(e)):
            buff.append(int(e[i]))
        image.append(buff)
        buff = []
    print(imageid)
    print(image)

if __name__ == '__main__':
    # train_data()
    test_data()