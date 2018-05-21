import random, time, Queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

task_queue = Queue.Queue()
result_queue = Queue.Queue()

class QueueManager(BaseManager):
	pass
	
def return_task_queue():
    global task_queue
    return task_queue

def return_result_queue():
    global result_queue
    return result_queue
	
def test():
	QueueManager.register('Get task_queue', callable = return_task_queue)
	QueueManager.register('Get result_queue', callable = return_result_queue)

	manager = QueueManager(address=('127.0.0.1',5000), authkey=b'abc')
	manager.start()
	
	task = manager.get_task_queue()
	result = manager.get_result_queue()

	for i in range(10):
		n = random.randint(0, 10000)
		print('Put task %d...' % n)
		task.put(n)

	print('Try get results...')
	for i in range(10):
		try:
			r = result.get(timeout=10)
			print('Result: %s' % r)
		except Queue.Empty:
			print('result queue is empty.')

	manager.shutdown()
	print('master exit.')
	
if __name__ == '__main__':
	freeze_support()
	test()


