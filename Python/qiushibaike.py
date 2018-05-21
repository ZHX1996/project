import requests
from bs4 import BeautifulSoup

#url='http://www.qiushibaike.com/'
def get(page):
    url='http://www.qiushibaike.com/8hr/page/'+ str(page) + '/?s=4964851'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'
    headers = {'User_Agent':user_agent}
    try:
        html = requests.get(url, headers=headers)
        soup = BeautifulSoup(html.text,'lxml');
        all_a = soup.select('.content span');
        for a in all_a:
            print(a);
    except requests.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

if __name__ == '__main__':
    page = 1
    flag = True
    while flag:
        get(page)
        input = input()
        if input == "Q":
            flag = False
        elif input == "\r":
            page += 1







