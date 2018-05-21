#coding:utf-8
import os

def func(target):
	list1 = []
	for path ,d, filelist in os.walk(target):
		for filename in filelist:
			ele = os.path.join(path, filename)
			list1.append(ele)
	return list1

g = func('F:\C的教程')
for i in g:
	print i