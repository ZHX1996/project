from multiprocessing import Pool
import os, time, random

def long_time_task(name):
	print('%s (%s)...' % (name, os.getpid()))
	start = time.time()
	time.sleep(random.random() * 3)
	sleep(1)
	end = time.time()
#	print('Task %s runs %0.2f seconds.' % (name, (end - start)))
	
if __name__ == '__main__':
	print('Parent process %s.'  % os.getpid())
	p = Pool(processes = 4)
	for i in range(0,5):
		result = p.apply_async(long_time_task, args = (i,))
	p.close()
#	p.terminate()
	p.join()
	
	if result.successful():
		print 'successful'