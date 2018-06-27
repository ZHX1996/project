#-*-coding:utf-8-*-
import sys
sys.path.append('../')

import jieba
import jieba.analyse

file_name = 'qishu.txt'
topK = 20
# 自定义语料库
# jieba.analyse.set_idf_path(file_name)
# 停止词
# jieba.analyse.set_stop_words(file_name)
content = open(file_name, 'rb').read()
# allowPOS属性：仅包括指定词性的词
tags = jieba.analyse.extract_tags(content, topK=topK, withWeight=True)
for tag in tags:
    print('tag:%s\t\t weight:%f' % (tag[0], tag[1]))
