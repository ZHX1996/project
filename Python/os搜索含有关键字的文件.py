#coding:utf-8  
import os,stat
#修改权限要以管理员权限运行
def print_files(word, path):
	os.chmod(path, stat.S_IREAD|stat.S_IWRITE)
	
	s = [x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))]
	for i in s:
		if x.__contains__(word):
			print(i)
	
	a = [x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]
	for i in a:
		child_path = os.path.join(path, i)
		files = [os.path.join(child_path, x) for x in os.listdir(child_path)
			if os.path.isfile(os.path.join(child_path, x)) and x.__contains__(word)]
		if len(files) >= 1:
			for file in files:
				print(file)
		print_files(word, child_path)
		
print_files('.py', 'E:\Python Project')