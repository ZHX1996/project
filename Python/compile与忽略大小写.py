#coding:utf-8
import re
#re.I 忽略大小写 ignorecase
abc = re.compile(r'abc', re.I)
print(abc.findall('abc'))
print(abc.findall('aBc'))
print(abc.findall('ABC'))