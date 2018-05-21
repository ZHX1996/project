# coding=utf-8
from  multiprocessing import Process
import time

class MyProcess(Process):
    def __init__(self, loop):
        Process.__init__(self)
        self.loop = loop

    def run(self):
        for count in range(self.loop):
            time.sleep(1)
            print('PID: ' + str(self.pid) + ' loopCount: ' + str(count))

if __name__ == '__main__':
    for i in range(2,5):  # 2,3,4
        p = MyProcess(i)
        p.daemon = True # 父进程结束，子进程自动终止
        p.start()
        p.join()  # 子进程执行完父进程唉终止

    print('main process ended!')