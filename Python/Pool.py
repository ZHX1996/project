from multiprocessing import Pool
from time import sleep


def f(x):
	for i in range(0,5):
		print '%s --- %s' % (i, x)
		sleep(1)


def main():
	pool = Pool(processes=3)
	for i in range(1,4):
		result = pool.apply_async(f, (i,))
	pool.close()
	pool.join()
	if result.successful():
		print 'successful'


if __name__ == "__main__":
	main()