# coding=utf-8
import requests
from bs4 import BeautifulSoup
from mongodb_queue import MongoQueue

crawl_queue = MongoQueue('mzi', 'crawl')
root_url = 'https://www.susu98.com'
def start(url):
    start_url = root_url + url
    html = requests.get(start_url)
    html.encoding = 'utf-8'
    Soup = BeautifulSoup(html.text, 'lxml')
    a_list = Soup.find('ul', class_ = 'textList').find_all('a')
    for a in a_list:
        title = a.get_text()
        path = str(title).strip()
        href = a['href']
        href = root_url + href
        crawl_queue.push(href, title)
        print(1)

if __name__ == '__main__':
    for i in range(1,10):
        url = '/htm/piclist1/' + str(i) + '.htm'
        start(url)
