#-*-coding:utf-8-*-
import sys
sys.path.append('../')

import jieba
import jieba.analyse
from optparse import OptionParser

# USAGE = "usage: python extract_tags.py [qishu.txt] -k [20]"
#
# parser = OptionParser(USAGE)
# parser.add_option("-k", dest='topK')
# opt, args = parser.parse_args()
#
# if len(args) < 1:
#     print(USAGE)
#     sys.exit(1)
#
# file_name = args[0]
#
# if opt.topK is None:
#     topK = 10
# else:
#     topK = int(opt.topK)
file_name = 'qishu.txt'
topK = 20

content = open(file_name, 'rb').read()
tags = jieba.analyse.extract_tags(content, topK=topK, withWeight=True)
for tag in tags:
    print('tag:%s\t\t weight:%f' % (tag[0], tag[1]))
# print(','.join(tags))