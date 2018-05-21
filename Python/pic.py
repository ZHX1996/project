#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from mongodb_queue import MongoQueue
import re
import os
import time
import threading
import multiprocessing

SLEEP_TIME = 1
local = threading.local()
def mzi_crawler(max_threads=10):
    crawl_queue = MongoQueue('mzi', 'crawl')
    def pageurl_crawler():
        while True:
            try:
                url = crawl_queue.pop()
                print(url)
            except KeyError:
                print('队列中没有数据')
                break
            else:
                title = crawl_queue.pop_title(url)
                local.title = title
                isExist = os.path.exists(os.path.join("F:\pic", title))
                if not isExist:
                    os.makedirs(os.path.join("F:\pic", title))
                os.chdir("F:\pic\\" + local.title)
                page_html = requests.get(url)
                page_html.encoding = 'utf-8'
                reg = r'<img src="(.*?.jpg)"'
                imgre = re.compile(reg)
                img_list = re.findall(imgre, page_html.text)
                for img_url in img_list:
                    name = img_url[-11:-4]
                    img = requests.get(img_url)
                    f = open(name+'.jpg', 'ab')
                    f.write(img.content)
                    f.close()
                crawl_queue.complete(url)

    threads = []
    while threads or crawl_queue:
        for thread in threads:
            if not thread.is_alive():
                threads.remove(thread)
        while len(threads) < max_threads or crawl_queue.peek():
            thread = threading.Thread(target=pageurl_crawler)
            thread.setDaemon(True)
            thread.start()
            threads.append(thread)
        time.sleep(SLEEP_TIME)

def process_crawler():
    process = []
    num_cpus = multiprocessing.cpu_count()
    print('进程数为：', num_cpus)
    for i in range(num_cpus):
        p = multiprocessing.Process(target = mzi_crawler)
        p.start()
        process.append(p)
        for p in process:
            p.join()

if __name__ == '__main__':
    process_crawler()








