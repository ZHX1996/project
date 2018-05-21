#coding:utf-8
import os
import sys

def dirList(path):
	filelist = os.listdir(path)
	fpath = os.path.abspath(path)
	allfile = []
	for filename in filelist:
		filepath = os.path.join(fpath, filename)
		if os.path.isdir(filepath):
			dirList(filepath)
		allfile.append(filepath)
	return allfile

	
list1 = dirList('F:\\C的教程')
for i in list1:
	print i