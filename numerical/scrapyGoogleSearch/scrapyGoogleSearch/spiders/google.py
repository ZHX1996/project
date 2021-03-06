# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request, Spider
from urllib.parse import quote
from scrapyGoogleSearch.items import ScrapygooglesearchItem, linkBodyItem, facebookIntroItem, officialIntroItem
from scrapy.shell import inspect_response
import re
import json
import html
import time
import pandas as pd
import logging


class GoogleSpider(scrapy.Spider):
    name = 'google'
    allowed_domains = ['www.google.com']
    start_urls = 'https://www.google.com/search?q='


    def parse(self, response, key):
        # inspect_response(response, self)

        products = response.xpath('//div[@id="rso"]/div/div[contains(@class,"srg")]/div[contains(@class,"g")]')
        for product in products:
            address = product.xpath('//div[@class="rc"]/div[@class="r"]/a[1]/@href').extract()
            title = product.xpath('//div[@class="rc"]/div[@class="r"]/a[1]/h3/text()').extract()
            break

        title = [x.replace('.','') for x in title]
        title = [x.replace('"',"'") for x in title]
        item = ScrapygooglesearchItem()
        item['title'] = '$$'.join(title)
        item['address'] = '$$'.join(address)
        item['key'] = key
        yield item

        for i in range(min(len(title),len(address))):
            if not address[i].endswith(('pdf', 'PDF')):
                yield Request(url = address[i], callback=lambda response, key=key, title=title[i]: self.parse_body(response, key,  title), dont_filter=True)
            else:
                print("pdf file: " + address[i])

        

        # tmp = 'https://www.google.com/search?as_q=' + key + '&as_epq=&as_oq=关于+是&as_eq=中国发展简报+环球+twitter+facebook+百科+意思&as_nlo=&as_nhi=&lr=&cr=&as_qdr=all&as_sitesearch=&as_occt=title&safe=images&as_filetype=&as_rights='
        # # tmp = 'https://www.google.com/search?as_q=' + key + '+关于我们&as_epq=&as_oq=关于+是&as_eq=中国发展简报+环球+twitter+facebook+百科+意思&as_nlo=&as_nhi=&lr=&cr=&as_qdr=all&as_sitesearch=&as_occt=any&safe=active&as_filetype=&as_rights='
        # yield Request(url=tmp, callback=lambda response,key=key,title=title,address=address: self.getFirstResult(response,key,title,address), dont_filter=True)

    

    def getFirstResult(self, response, key, title, address):
        # link = response.xpath("//div[@id='main']//div[3]//a[1]//@href").extract()
        link = response.xpath('//div[@class="rc"]/div[@class="r"]/a[1]/@href').extract()
        # res =  '/url?q=https://www.salvationarmy.org.hk/cn/about_us&sa=U&ved=2ahUKEwjXuMW416LlAhVIqZ4KHUD7Dp8QFjAAegQIARAB&usg=AOvVaw2_IWZuQk5duHOt7hzTrUER'

        # pattern = re.compile(r'.*?\?q=(.*?)&sa=.*?')
        # m = pattern.match(''.join(link)).group(1)

        m = link[0]
        # print("m: ", m)

        pattern1 = re.compile(r'.*?www\.(.*)\..*?')
        target = pattern1.match(m).group(1)
        # print("target: ", target)
        

        for i in range(len(address)):
            # tmp = 'https://www.salvationarmy.org.hk/cn/about_us'
            try:
                source = pattern1.match(address[i]).group(1)
                # print("source: ", source)
                if source == target:
                    # print(key, title[i])
                    yield Request(url=m, callback=lambda response,key=key,title=title[i]: self.parse_officialIntro(response,key,title), dont_filter=True)
            except:
                pass


    def parse_officialIntro(self, response, key, title):
        # print(2)
        officialItem = officialIntroItem()
        # tmp = response.text
        # print(response.url)
        officialItem['intro'] = response.url
        # print(title, response.url)
        # item['address'] = response.url
        # item['category'] = '官网介绍'
        # officialItem['key'] = key
        officialItem['title'] = title
        officialItem['category'] = '官网'
        # print(title, response.url)
        yield officialItem


    def processInfo(self, tmp):
        # tmp = re.sub(r'\n', '', tmp)
        tmp = re.sub(r'\r', '', tmp)
        tmp = re.sub(r'\t', '', tmp)
        tmp = re.sub(r'"', "'", tmp)
        tmp = html.unescape(tmp)
        # tmp = re.sub(r'gb2312', 'utf-8', tmp)

        pattern = re.compile(r'<script.*?</script>', re.DOTALL)
        tmp = pattern.sub(r'', tmp)
        pattern = re.compile(r'<scip.*?</scip>', re.DOTALL)
        tmp = pattern.sub(r'', tmp)
        pattern = re.compile(r'<style.*?</style>', re.DOTALL)
        tmp = pattern.sub(r'', tmp)
        # pattern = re.compile(r'<.*?</[\w\W]*?>', re.DOTALL)
        # tmp = pattern.sub(r'', tmp)
        pattern = re.compile(r'<[\w\W]*?>')
        tmp = pattern.sub(r'', tmp)

        # 去除4字节字符
        try:
            pattern = re.compile(u'[\U00010000-\U0010ffff]')
        except re.error:
            pattern = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
        tmp = pattern.sub(u'',tmp)

        tmp = re.sub(r'\n+', '\n', tmp)
        tmp = " ".join(tmp.split())
        return tmp


    def parse_body(self, response, key, title):
        contentItem = linkBodyItem()
        # body:二进制类型   text:string类型      包含' \r \n \t \
        tmp = response.text

        tmp = self.processInfo(tmp)

        contentItem['content'] = tmp
        contentItem['key'] = key
        contentItem['title'] = title
        contentItem['address'] = response.url
        contentItem['intro'] = ' '

        str2 = ""
        if "baike.baidu.com" in response.url:
            contentItem['category'] = '百度百科'
            contentItem['intro'] = self.processInfo(''.join(response.xpath('//div[@class="lemma-summary"]//div//text()').extract()))
        elif "wikipedia.org" in response.url:    
            contentItem['category'] = '维基百科'               
            contentItem['intro'] = self.processInfo(''.join(response.xpath('//div[@id="mw-content-text"]/div/p[1]//text()').extract()))
        elif 'facebook.com' in response.url:
            str1 = response.url
            k = str1.find('/', 25)
            m = str1.find('/', 8)
            str2 = str1[:m+1] + 'pg' + str1[m:k+1] + 'about/'
            contentItem['category'] = '脸书'
            contentItem['intro'] = str2
        elif 'twitter.com' in response.url:
            # //*[@id="react-root"]/div/div/div/main/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div//text()  登录
            # //*[@id="page-container"]/div[2]/div/div/div[1]/div/div/div/div[1]/p//text()   未登录
            contentItem['category'] = '推特'
            contentItem['intro'] = self.processInfo(''.join(response.xpath('//*[@id="page-container"]/div[2]/div/div/div[1]/div/div/div/div[1]/p//text()').extract()))
        elif 'linkedin' in response.url:
            contentItem['category'] = '领英'
        elif 'weibo' in response.url:
            contentItem['category'] = '微博'
        elif 'blog' in response.url:
            contentItem['category'] = '博客'
        elif self.isContain(['zhaopin','kanzhun'], response.url):
            contentItem['category'] = '招聘'
        elif self.isContain(['youku','tudou'], response.url):
            contentItem['category'] = '视频'
        elif self.isContain(['ifeng', 'finance.sina', 'business.sohu', 'new.qq','dooo'], response.url):
            contentItem['category'] = '新闻'
        else:
            contentItem['category'] = '其它'

        yield contentItem
        if str2 !="":
            yield Request(url = str2, callback=lambda response, key=key, title = title,address=str1: self.parse_facebook_intro(response,key,title,address), dont_filter=True)


    def parse_facebook_intro(self, response, key, title, address):
        facebookintroItem = facebookIntroItem()
        facebookintroItem['key'] = key
        facebookintroItem['title'] = title
        facebookintroItem['address'] = address
        facebookintroItem['intro'] = self.processInfo(' '.join(response.xpath('//div[@role="main"]//text()').extract()))
        yield facebookintroItem


    def isContain(self, ic_li, ic_url):
        for i in ic_li:
            if i in ic_url:
                return True
        return False
        
        
    def start_requests(self):
        logger = logging.getLogger(__name__)
        # logger.error("the log level is error")
        logger.warn("the log level is warning")

        import os
        # print(os.path.abspath("./"))
        f = open("./scrapyGoogleSearch/spiders/NGO.txt", 'r', encoding='utf-8')
        li = f.readlines()
        li = list(map(lambda x: x.strip(), li))
        f.close()

        f = open("./scrapyGoogleSearch/spiders/alread.txt", 'r', encoding='utf-8')
        alread = f.readlines()
        alread = list(map(lambda x: x.strip(), alread))
        last = [x for x in li if x not in alread]

        # print(len(last))

        # file = pd.read_excel(self.settings.get('NGO_FILE'),sheet_name='Sheet1', names=self.settings.get('COLUMNS_NAME') )
        # df = pd.DataFrame(file)
        # df['中文名称'].fillna(df['外文名称'], inplace=True)
        # for keyword in df['中文名称'].tolist():
        # for keyword in self.settings.get('KEYWORDS'):

        for keyword in last:
            for page in range(0, self.settings.get('MAX_PAGE')):
                url = self.start_urls + quote(keyword) + '&start=' + quote(str(page*10))
                yield Request(url=url, callback=lambda response, key=keyword :self.parse(response, key),dont_filter=True)