# coding=utf-8
from multiprocessing import Process, Queue, Semaphore, Lock
import time
from random import random

class Consumer(Process):
    def __init__(self, buffer, lock, empty, full):
        Process.__init__(self)
        self.buffer = buffer
        self.empty = empty
        self.full = full
        self.lock = lock

    def run(self):
        while True:
            self.full.acquire()
            self.lock.acquire()

            # self.buffer.get()
            # print('Consumer pop an element!')
            print('consumer get', self.buffer.get())
            
            time.sleep(1)
            self.lock.release()
            self.empty.release()

class Producer(Process):
    def __init__(self, buffer, lock, empty, full):
        Process.__init__(self)
        self.buffer = buffer
        self.empty = empty
        self.full = full
        self.lock = lock

    def run(self):
        while True:
            self.empty.acquire()
            self.lock.acquire()

            # self.buffer.put(1)
            # print('Producer append an element!')
            num = random()
            print('producer put', num)
            self.buffer.put(num)

            time.sleep(1)
            self.lock.release()
            self.full.release()

if __name__ == '__main__':
    buffer = Queue(10)
    empty = Semaphore(2)
    full = Semaphore(0)
    lock = Lock()
    p = Producer(buffer,lock, empty, full)
    c = Consumer(buffer,lock, empty, full)
    p.daemon = c.daemon = True
    p.start()
    c.start()
    p.join()
    c.join()
    print('End')
