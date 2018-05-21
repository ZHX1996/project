#coding:utf-8
from multiprocessing import Process
import os 

def run_proc(name):
	print ("Run child process %s (%s)..." % (name, os.getpid()))
	
if __name__ == '__main__':
	print('Parent process %s.' % os.getpid())
	p = Process(target = run_proc, args = ('test',))
	print('child process will start')
	p.start()
	p.join()  #子进程结束再向下执行
	print('child process end')