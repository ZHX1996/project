# _*_ coding:utf-8 _*_

#s = u'am I an unicode?'
#print isinstance(s, unicode)

from __future__ import unicode_literals

s = 'am I an unicode?'
print isinstance(s, unicode)

#在Python 3.x中，字符串统一为unicode，不需要加前缀 u，而以字节存储的str则必须加前缀 b