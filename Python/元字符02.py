# coding:utf-8
# 重复{次数} {最小次数,最大次数} *0次或多次  +一次或多次  ？0次或1次  （前一个字符）

import re
s1 = '010-12345678 010-87654321 01012347658'
n1 = r'010-\d{8}'
print re.findall(n1, s1)

n2 = r'010-?\d{8}'
print re.findall(n2, s1)