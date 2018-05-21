# coding=utf-8
import requests
from bs4 import BeautifulSoup
import re
import os

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
        isExist = os.path.exists(os.path.join("F:\pic", path))
        if not isExist:
            os.makedirs(os.path.join("F:\pic", path))
        os.chdir("F:\pic\\" + path)
        href = a['href']
        href = root_url + href
        page_html = requests.get(href)
        page_html.encoding = 'utf-8'
        reg = r'<img src="(.*?.jpg)"'
        imgre = re.compile(reg)
        img_list = re.findall(imgre, page_html.text)
        for img_url in img_list:
            # print(img)
            name = img_url[-11:-4]
            img = requests.get(img_url)
            f = open(name+'.jpg', 'ab')
            f.write(img.content)
            f.close()

if __name__ == '__main__':
    for i in range(1,10):
        url = '/htm/piclist1/' + str(i) + '.htm'
        start(url)