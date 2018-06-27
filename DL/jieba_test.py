# -*-coding:utf-8-*-
# https://www.cnblogs.com/hudongni1/articles/5522704.html
from __future__ import print_function, unicode_literals
import sys
sys.path.append("../")
import jieba
import jieba.posseg as pseg

# 载入自定义词典，一个词一行，每一行三部分：词语，词频(可省略)，词性(可省略),用空格隔开
jieba.load_userdict("userdict.txt")
# 动态修改词典
jieba.add_word('石墨烯')
jieba.add_word('凱特琳')
jieba.add_word('自定义词')
# jieba.del_word()

# 开启并行分词，不支持Windows
jieba.enable_parallel(4)


def default_dict():
    # 全模式
    seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
    print('Full Mode: ' + '/ '.join(seg_list))

    # 精确模式
    seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
    print('Default Mode: ' + '/ '.join(seg_list))
    # 默认为精确模式 (杭研不再词典中，是被viterbi算法识别出来的)
    seg_list = jieba.cut("他来到了网易杭研大厦")
    print(",".join(seg_list))

    # 搜索引擎模式
    seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")
    print(",".join(seg_list))

# 返回的是可迭代的generator，使用for循环获取，也可直接使用lcut，lcut_for_search返回list

def custom_dict():
    test_sent = ("李小福是创新办主任也是云计算方面的专家; 什么是八一双鹿\n"
        "例如我输入一个带“韩玉赏鉴”的标题，在自定义词库中也增加了此词为N类\n"
        "「台中」正確應該不會被切開。mac上可分出「石墨烯」；此時又可以分出來凱特琳了。")
    words = jieba.cut(test_sent)
    print('/'.join(words))

    print("="*40)

    # 词性标注
    result = pseg.cut(test_sent)
    for w in result:
        print(w.word, '/', w.flag, ',', end=' ')

    print('\n' + "="*40)

    terms = jieba.cut('easy_install is great')
    print('/'.join(terms))
    terms=jieba.cut('python 的正则表达式是好用的')
    print('/'.join(terms))

    print('='*40)

def frequency_tune():
    testlist = [
        ('今天天气不错', ('今天', '天气')),
        ('如果放到post中将出错。', ('中', '将')),
        ('我们中出了一个叛徒', ('中', '出')),
    ]

    for sent, seg in testlist:
        print('/'.join(jieba.cut(sent, HMM=False)))
        word = ''.join(seg)
        # 使用suggest_freq()调节单个词语的词频，使其能被分出来
        print('%s before: %s, After: %s' % (word, jieba.get_FREQ(word), jieba.suggest_freq(seg, True)))
        print('/'.join(jieba.cut(sent, HMM=False)))
        print('-'*40)

if __name__ == '__main__':
    default_dict()
    # custom_dict()
    # frequency_tune()